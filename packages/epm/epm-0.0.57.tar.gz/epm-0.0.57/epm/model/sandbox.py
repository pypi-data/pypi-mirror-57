import sys
import os
import subprocess
import yaml
import re
import collections
import stat
import glob
import paramiko
import ftplib
import logging
import fnmatch
from string import Template
from jinja2 import PackageLoader, Environment, FileSystemLoader

import epm
from epm.errors import EException
from epm.client.output import Output
from epm.paths import normalize_path, conan_storage_path
from epm.utils.files import mkdir

from epm.utils import system_info, is_elf, XSym
from epm.enums import Platform, Architecture

from conans.client.generators.text import TXTGenerator
from conans.util.files import load
from conans.model.info import ConanInfo

from epm.utils.log import project_logger as logger
log = logger()


PLATFORM, ARCH = system_info()


# http://www.pixelbeat.org/programming/linux_binary_compatibility.html

def conanbuildinfo(folder):
    path = os.path.join(os.path.join(folder, 'conanbuildinfo.txt'))
    if os.path.exists(path):
        cpp, _, _ = TXTGenerator.loads(load(path))
        return cpp
    return None


def conaninfo(folder):
    return ConanInfo.load_from_package(folder)


def remove_path_prefix(path, prefix):
    assert(os.path.isabs(path) and os.path.isabs(path))
    tokens = normalize_path(path).split('/')
    parts = normalize_path(prefix).split('/')
    size = len(parts)

    import operator
    if operator.eq(parts, tokens[:size]):
        tail = tokens[size:]
        return "/".join(tail) if tail else ''
    return None


def semantic_path(path, prefixs):
    for name, prefix in prefixs:
        tail = remove_path_prefix(path, prefix)
        if tail is None:
            continue
        return '%s/%s' % (name, tail)
#    log.error('semantic path error:\n path=%s\n prefixs=%s\n' % (path, str(prefixs)))
    return None


P_PATH = re.compile(r'(?P<folder>(build|package|test_package))/(?P<relpath>\S+)')

import epm

# Join two (or more) paths.
def join(path, *paths):
    path = os.path.join(path, *paths)
    path = os.path.normpath(path)
    path = path.replace('\\', '/')
    return path


class Program(object):

    def __init__(self, project, commandline, storage, is_create=False, id=None):
        self._project = project

        self._commandline = commandline
        argv = commandline.split(' ')
        self._path = argv[0]
        self._argv = argv[1:]

        m = P_PATH.match(self._path)

        self._folder = m.group('folder')
        self._relpath = m.group('relpath')
        self._middle = " ".join(self._relpath.split('/')[:-1])
        self._name = os.path.basename(self._path)
        self._fullname = self._name + self._ext
        self._storage_path = storage
        self._is_create = is_create
        self._id = id
        self._wd = normalize_path(os.path.abspath('.'))
        self._build_dir = None

        self._initialize()
        log.debug("storage_path: %s\nfilename:%s\n" % (self._storage_path, self._filename))

    @property
    def storage_path(self):
        return self._storage_path

    @property
    def _ext(self):
        return '.exe' if self._project.profile.settings['os'] == Platform.WINDOWS else ''

    @property
    def _is_windows(self):
        return self._project.profile.settings['os'] == Platform.WINDOWS

    @property
    def _is_linux(self):
        return self._project.profile.settings['os'] == Platform.LINUX

    def _initialize(self):
        where = 'project'
        if self._is_create and self._folder in ['build', 'package']:
            where = 'conan'

        self._filename, self._build_dir = self._locate(where)

    def _is_program(self, path):
        filename = path + self._ext
        if os.path.exists(filename):
            if os.path.isfile(filename):
                return filename
            elif os.path.islink(filename):
                real = os.path.realpath(filename)
                if os.path.isfile(real):
                    return filename
        return None

    def _template(self, filename):
        path = os.path.join(os.path.dirname(epm.__file__), 'data', 'sandbox')
        env = Environment(loader=FileSystemLoader(path))
        env.trim_blocks = True
        template_file = os.path.basename(filename)
        template = env.get_template(template_file)
        return template

    def _locate(self, where='project'):
        ''' return the program path with ${project} or ${conan}  prefix

        :param where: where to locate the porgram
        :return:
        '''
        project = self._project

        def ppath(m):
            root = join(project.out_folder, self._folder)
            return join(root, m, self._name), root

        def cpath(m, storage=None):
            rpath = project.reference.replace('@', '/')
            storage = storage or self.storage_path
            root = join(storage, rpath, self._folder, self.id)
            return join(root, m, self._name), root

        folders = ['bin'] if self._folder == 'package' else ['bin', '']
        folders = [self._middle] if self._middle else folders

        for m in folders:
            vpath, root = ppath(m) if where == 'project' else cpath(m)
            if self._is_program(vpath):
                if where == 'project':
                    return '${project}/%s' % vpath, root
                else:
                    prefix = semantic_path(self.storage_path,
                                           [('${project}', os.path.abspath('.'))])
                    prefix = '${storage}' if prefix is None else prefix
                    vpath, _ = cpath(m, storage=prefix)
                    return vpath, root
        raise EException('can not locate program <{}> in {}'.format(self._name, where))

    @property
    def id(self):
        return self._id

    @property
    def libpath(self):
        project = self._project

        dirs = []
        out_folder = self._project.out_folder
        prefix = semantic_path(self.storage_path, [('${project}', os.path.abspath('.'))])
        prefix = '${storage}' if prefix is None else prefix

        sub_folder = 'bin' if self._is_windows else 'lib'

        if self._is_create and self._folder in ['build', 'package']:
            rpath = project.reference.replace('@', '/')
            # <reference>/package/<id>/<lib|bin>
            path = join(prefix, rpath, self.id, sub_folder)
            dirs.append(path)
        else:
            root = join(out_folder, self._folder)
            libpath_dir = join(root, sub_folder)

            if os.path.exists(libpath_dir):
                dirs += ['${project}/' + libpath_dir]

            if os.path.exists(libpath_dir):
                dirs += ['${project}/' + root]

        # build command will use editable info which saved in conanbuildinfo.txt
        # create command use conaninfo.txt
        if self._is_create or self._folder in ['package']:
            info = conaninfo(self._build_dir)
            for i in info.full_requires.serialize():
                folder = i.replace('@', '/').replace(':', '/package/')
                dirs.append(join(prefix, folder, sub_folder))
        else:
            print(self._build_dir, '<------------')
            cpp = conanbuildinfo(self._build_dir)
            libdirs = cpp.bindirs if self._is_windows else cpp.libdirs
            for i in libdirs:
                vpath = semantic_path(i, [('${project}', os.path.abspath('.')),
                                           ('${storage}', self.storage_path)])
                dirs.append(vpath)



        return dirs

    @property
    def dynamic_libs(self):
        libs = {}

        for libd in self.libpath:
            d = Template(libd).substitute(project=self._wd, storage=self.storage_path)
            if not os.path.exists(d):
                continue

            for name in os.listdir(d):
                filename = normalize_path('%s/%s' % (libd, name))
                path = normalize_path(os.path.join(d, name))
                if os.path.isdir(path):
                    continue

                if self._is_windows and fnmatch.fnmatch(name, "*.dll"):
                    libs[name] = {'target': filename, 'symbol': False, 'origin': filename, 'host': PLATFORM}
                    continue  # only for debug

                if not fnmatch.fnmatch(name, '*.so*') or not self._is_linux:
                    continue

                if os.path.islink(path):
                    p = os.readlink(path)
                    if os.path.isabs(p):
                        target = self._path(p)
                    else:
                        target = normalize_path('%s/%s' % (libd, p))
                    assert(target)
                    libs[name] = {'target': target, 'symbol': True, 'origin': filename, 'host': PLATFORM}
                else:
                    if is_elf(path):
                        libs[name] = {'target': filename, 'symbol': False, 'origin': filename, 'host': PLATFORM}
                        continue
        return libs

    @property
    def _docker_image(self):
        docker = self._project.profile.manifest.get('docker', {})
        return docker.get('runner', {}).get('image')

    @property
    def _docker_shell(self):
        docker = self._project.profile.manifest.get('docker', {})
        return docker.get('runner', {}).get('shell', '/bin/bash')

    def _windows(self, name):
        def _(path):
            s = Template(path).substitute(project=r'%EPM_SANDBOX_PROJECT%', storage=r'%EPM_SANDBOX_STORAGE%')
            return normalize_path(s).replace('/', '\\')

        filename = _(self._filename)

        libdirs = [_(x) for x in self.libpath]

        template = self._template('windows.j2')
        return template.render(libdirs=libdirs, filename=filename, name=name,
                               configuration=self._project.configuration.name,
                               arguments=" ".join(self._argv))

    def _linux(self, name):
        libdirs = []

        filename = self._filename

        template = self._template('linux.j2')

        return template.render(libdirs=libdirs, filename=filename, name=name,
                               dylibs=self.dynamic_libs,
                               image=self._docker_image,
                               shell=self._docker_shell,
                               configuration=self._project.configuration.name,
                               arguments=" ".join(self._argv))

    def _linux_windows_docker(self, name):
        def _(path):
            s = Template(path).substitute(project=r'$EPM_SANDBOX_PROJECT', storage=r'$EPM_SANDBOX_STORAGE')
            return normalize_path(s)

        filename = _(self._filename)

        libdirs = [_(x) for x in self.libpath]

        template = self._template('linux.cmd.j2')
        return template.render(libdirs=libdirs, filename=filename, name=name,
                               image=self._docker_image,
                               shell=self._docker_shell,
                               configuration=self._project.configuration.name,
                               arguments=" ".join(self._argv))

    def generate(self, name):

        if not self._filename:
            print('WARN: can not find <%s>, skip generate sandbox.' % self._path)
            return

        filename = os.path.join(self._project.out_folder, 'sandbox', name)
        mkdir(os.path.dirname(filename))

        if self._is_windows:
            script = self._windows(name).encode('utf-8')
            with open(filename + '.cmd', 'wb') as f:
                f.write(script)
        else:
            script = self._linux(name).encode('utf-8')
            with open(filename, 'wb') as f:
                f.write(script)
            #    f.close()
            mode = os.stat(filename).st_mode
            os.chmod(filename, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

            script = self._linux_windows_docker(name).encode('utf-8')
            with open(filename + '.cmd', 'wb') as f:
                f.write(script)

        with open(filename + '-dynamic-libs.yaml', 'w') as f:

            yaml.safe_dump(self.dynamic_libs, f, default_flow_style=False, indent=2)










