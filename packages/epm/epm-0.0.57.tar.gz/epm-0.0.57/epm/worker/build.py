import os
import glob
import fnmatch

from conans.client.generators.text import TXTGenerator
from conans.util.files import load


from epm.utils.files import remove, rmdir

from epm.errors import EException
from conans.client.conan_api import Conan

from conans.paths import get_conan_user_home

from epm.model.sandbox import Program
from epm.utils import is_elf
from pathlib import Path
from epm.paths import conan_storage_path, normalize_path, get_epm_user_home
from epm.utils.log import project_logger as logger
log = logger()


#def _docker_pre_command(docker):
#    return ''
#    path = os.environ.get('EPM_EDITABLE_PATH')
#    if path:
#        epm = '%s/project/epm-project' % docker.home
#        docker.volume[path] = epm
#        return 'pip install -e %s && ' % epm
#    return ''


class Base(object):

    def __init__(self, project, conan):
        self.project = project
        self.conan = conan
        self.out = conan.out
        self._command = None
        self._storage_path = conan_storage_path()

    def _sandbox(self, folder=None, id=None):

        folders = [folder] if folder else ['build', 'package', 'test_package']
        for folder in folders:
            for name, command in self.project.manifest.get('sandbox', {}).items():
                if command.startswith(folder):
                    program = Program(self.project, command, self._storage_path, self._command == 'create', id=id)
                    program.generate(name)

    def _editable_clear(self):
        for i in self.conan.editable_list():
            self.conan.editable_remove(i)

    @staticmethod
    def load_docker(api, cache=None):
        conan_home = get_conan_user_home()
        epm_home = get_epm_user_home()
        storage_path = conan_storage_path()
        worker = api.worker
        configuration = api.worker.configuration
        profile = configuration.profile
        config = profile.manifest.get('docker', {}).get('builder')
        if not config:
            raise EException('profile not support docker build')
        from epm.utils.docker import Docker

        docker = Docker(config)

        project = worker.project

        docker_wd = '%s/project/%s' % (docker.home, project.name)

        docker_storage = '%s/project/.conan' % docker.home
        docker_conan_home = '%s/project/.conan.home' % docker.home
        docker_epm_home = '%s/project/.epm.home' % docker.home

        if cache:
            from epm.utils.files import mkdir
            mkdir('.conan')
            storage_path = os.path.abspath('.conan')

        cwd = normalize_path(os.path.abspath('.'))

        docker.volume[docker_wd] = cwd
        docker.volume[docker_storage] = storage_path
        docker.volume[docker_conan_home] = conan_home
        docker.volume[docker_epm_home] = epm_home

        docker.env['CONAN_STORAGE_PATH'] = docker_storage
        docker.env['CONAN_USER_HOME'] = docker_conan_home
        docker.env['EPM_USER_HOME'] = docker_epm_home
        docker.WD = docker_wd
        return docker


class Builder(Base):

    def __init__(self, project, conan):
        super(Builder, self).__init__(project, conan)

    def exec(self, steps):
        self._editable_clear()

        if isinstance(steps, str):
            steps = [steps]

        self.project.initialize('configure' in steps)

        if 'configure' in steps:
            self._configure()
            self.project.save(private={'command': 'build'})

        if 'package' in steps:
            self._package()

        if 'install' in steps:
            self._install()

        if 'test_package' in steps:
            self._test_package()

    def _configure(self):
        self.out.highlight('[configure ......]')
        project = self.project
        configuration = project.configuration
        profile = configuration.profile
        scheme = configuration.scheme

        settings = ['%s=%s' % (k, v) for k, v in profile.settings.items()]
        options = ['%s=%s' % (k, v) for (k, v) in scheme.options.as_list()]

        info = self.conan.install(path='.',
                                  name=project.name,
                                  version=project.version,
                                  user=project.user,
                                  channel=project.channel,
                                  settings=settings,
                                  options=options,
                                  profile_names=['%s/profile' % project.out_folder],
                                  install_folder=project.build_folder)

        if info['error']:
            raise EException('configure project %s failed' % project.name)

        info = self.conan.source('.')
        return info

    def _package(self):
        self.out.highlight('[build ......]')

        self.conan.build(conanfile_path='.',
                         package_folder=self.project.package_folder,
                         build_folder=self.project.build_folder,
                         install_folder=self.project.build_folder)

        self._sandbox('build')
        return {}

    def _install(self):
        self.out.highlight('[install ......]')
        self.conan.package(path='.',
                           build_folder=self.project.build_folder,
                           package_folder=self.project.package_folder,
                           install_folder=self.project.build_folder)
        self._sandbox('package')
        return {}

    def _test_package(self):
        self.out.highlight('[package testing  ......]')
        project = self.project
        configuration = project.configuration
        profile = configuration.profile
        scheme = configuration.scheme

        self.conan.editable_add(path='.',
                                reference=project.reference,
                                layout=project.layout,
                                cwd=os.getcwd())

        settings = ['%s=%s' % (k, v) for k, v in profile.settings.items()]
        options = ['%s=%s' % (k, v) for k, v in scheme.link_options.as_list()]

        self.conan.test(path='./test_package',
                        reference=project.reference,
                        settings=settings,
                        options=options,
                        test_build_folder=project.test_folder,
                        profile_names=['%s/profile' % project.out_folder])
        self._sandbox('test_package')
        return {}

    @staticmethod
    def shell(api, steps):
        conan = api.conan or Conan.factory()
        builder = Builder(api.worker.project, conan)
        return builder.exec(steps)

    @staticmethod
    def docker(api, steps):
        docker = Base.load_docker(api)
        configuration = api.worker.project.configuration
        cmd = 'epm -c %s build --runner shell' % configuration.name

        for i in steps:
            cmd += ' --%s ' % i

        docker.run(cmd)

    @staticmethod
    def docker_(api, steps):
        conan_home = get_conan_user_home()
        epm_home = get_epm_user_home()
        storage_path = conan_storage_path()
        project = api.worker.project
        configuration = project.configuration
        profile = configuration.profile
        config = profile.manifest.get('docker', {}).get('builder')
        if not config:
            raise EException('profile not support docker build')
        from epm.utils.docker import Docker

        docker = Docker(config)

        wd = '%s/project/%s' % (docker.home, project.name)
        storage = '%s/project/conan' % docker.home
        home = '%s/project/.home' % docker.home
        storage_path = conan_storage_path()

        cwd = normalize_path(os.path.abspath('.'))

        docker.volume[cwd] = wd
        docker.volume[storage_path] = storage
        docker.volume[Path.home()] = home
        docker.env['CONAN_USER_HOME'] = home
        docker.env['EPM_USER_HOME'] = home
        docker.WD = wd

        cmd = _docker_pre_command(docker)
        cmd += 'epm -c %s build --runner shell' % configuration.name

        for i in steps:
            cmd += ' --%s ' % i

        docker.run(cmd)
        return {}



class Creator(Base):

    def __init__(self, project, conan):
        super(Creator, self).__init__(project, conan)
        self._command = 'create'

    def exec(self, cache=False, clear=False):
        project = self.project
        configuration = project.configuration
        profile = configuration.profile
        scheme = configuration.scheme

        if cache:
            storage_path = '.conan'
            self._storage_path = os.path.abspath(storage_path)
            os.environ['CONAN_STORAGE_PATH'] = self._storage_path

        self.project.initialize(True)

        self.conan.editable_remove(self.project.reference)

        settings = ['%s=%s' % (k, v) for k, v in profile.settings.items()]
        options = ['%s=%s' % (k, v) for (k, v) in scheme.link_options.as_list()]

        self._editable_clear()

        info = self.conan.create('.',
                                 name=project.name,
                                 version=project.version,
                                 user=project.user,
                                 channel=project.channel,
                                 settings=settings,
                                 options=options,
                                 profile_names=['%s/profile' % project.out_folder],
                                 test_build_folder=project.test_folder)
        if info['error']:
            raise EException('create failed')

        if clear:
            self._clear_cache(self._storage_path)

        id = info.get('installed')[0].get('packages')[0]['id']
        self._sandbox(id=id)
        with open('{}/package.json'.format(project.out_folder), 'w') as f:
            import json
            json.dump({'id': id}, f)

        return {}

    @staticmethod
    def shell(api, clear, cache):
        conan = api.conan or Conan.factory()
        creator = Creator(api.worker.project, conan)
        return creator.exec(clear, cache)

    @staticmethod
    def docker(api, clear, cache):
        docker = Base.load_docker(api, cache)
        configuration = api.worker.project.configuration
        cmd = 'epm -c %s create --runner shell' % configuration.name
        cmd += ' --cache' if cache else ''
        cmd += ' --clear' if clear else ''
        docker.run(cmd)
        return {}

    @staticmethod
    def docker_(api, clear, cache):
        conan_home = get_conan_user_home()
        epm_home = get_epm_user_home()
        storage_path = conan_storage_path()
        worker = api.worker
        configuration = api.worker.configuration
        profile = configuration.profile
        config = profile.manifest.get('docker', {}).get('builder')
        if not config:
            raise EException('profile not support docker build')
        from epm.utils.docker import Docker

        docker = Docker(config)

        project = worker.project

        docker_wd = '%s/project/%s' % (docker.home, project.name)

        docker_storage = '%s/project/.conan' % docker.home
        docker_conan_home = '%s/project/.conan.home' % docker.home
        docker_epm_home = '%s/project/.epm.home' % docker.home

#        from epm.paths import conan_storage_path, normalize_path

        if cache:
            from epm.utils.files import mkdir
            mkdir('.conan')
            storage_path = os.path.abspath('.conan')

        cwd = normalize_path(os.path.abspath('.'))

        docker.volume[docker_wd] = cwd
        docker.volume[docker_storage] = storage_path
        docker.volume[docker_conan_home] = conan_home
        docker.volume[docker_epm_home] = epm_home

        docker.env['CONAN_STORAGE_PATH'] = docker_storage
        docker.env['CONAN_USER_HOME'] = docker_conan_home
        docker.env['EPM_USER_HOME'] = docker_epm_home
        docker.WD = docker_wd

        cmd = _docker_pre_command(docker)
        cmd += 'epm -c %s create --runner shell' % configuration.name
        cmd += ' --cache' if cache else ''
        cmd += ' --clear' if clear else ''

        docker.run(cmd)
        return {}

    @staticmethod
    def _rm(path):
        if os.path.isfile(path):
            remove(path)
        elif os.path.isdir(path):
            rmdir(path)
        else:
            raise EException('can not delete unknown artifact %s' % path)

    @staticmethod
    def _clear(folder):
        for i in glob.glob('%s/*' % folder):
            Creator._rm(i)

    @staticmethod
    def _clear_non_runtime_artifact(path):

        name = os.path.basename(path)
        ext = os.path.splitext(name)[-1]
        if name in ['conanbuildinfo.txt', 'conaninfo.txt']:
            return
        if ext in ['.exe', '.so', '.dll']:
            return
        if fnmatch.fnmatch(ext, '.so.*'):
            return

        if os.path.islink(path):
            return

        if os.path.isfile(path):
            if is_elf(path):
                return
        Creator._rm(path)

    @staticmethod
    def _clear_builds(path):
        for p in glob.glob('%s/*' % path):
            n = os.path.basename(p)
            if n in ['bin', 'lib']:
                for l in glob.glob('%s/*' % p):
                    Creator._clear_non_runtime_artifact(l)
            else:
                Creator._clear_non_runtime_artifact(p)

    @staticmethod
    def _clear_conan_storage(storage, ref_path):
        base = '%s/%s' % (storage, ref_path)
        for i in glob.glob('%s/*' % base):
            name = os.path.basename(i)
            if name in ['package', 'metadata.json', 'export']:
                continue

            if name == 'build':
                for l in glob.glob('%s/*' % i):
                    Creator._clear_builds(l)
            elif name == 'export_source':
                Creator._clear(i)
            else:
                Creator._rm(i)

    def _clear_cache(self, storage_path):
        for i in glob.glob(self.project.test_folder):
            self._clear_builds(i)

        ref_path = self.project.reference.replace('@', '/')

        self._clear_conan_storage(storage_path, ref_path)

        def sizeof(folder):
            size = 0
            for root, dirs, files in os.walk(folder):
                for name in files:
                    path = os.path.join(root, name)
                    if os.path.isfile(path):
                        size += os.path.getsize(path)
            return size/(1024 * 1024)

        try:
            c = sizeof('.conan')
            e = sizeof('.epm')
            self.conan_.out.success('[.conan %.2fM] [.epm %.2fM]' % (c, e))
        except Exception as e:
            pass




