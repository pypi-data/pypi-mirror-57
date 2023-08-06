
import sys
import os
import shutil
import yaml
import glob

import epm
from epm import __version__
from epm.client.output import Output, colorama_initialize
from epm.client.userio import UserIO

from epm.client import tools
from epm.paths import get_epm_user_home

from epm.utils.files import exception_message_safe, mkdir, save_files, load, normalize, save
from epm.utils.log import configure_logger
from epm.utils.tracer import log_command, log_exception
from epm.client.conf import EPMClientConfigParser, default_client_conf
from epm.model.profile import Profile
from epm.model.project import Project
from epm.model.configuration import Configuration
from epm.errors import EException
from conans.client.conan_api import Conan

import logging
import epm

from epm.worker.build import Builder, Creator
from epm.worker.sandbox import Sandbox


def _setup(api):
    #api.worker.profile = Profile(api.profile_, api.worker)
    #api.worker.project = Project(api.worker.profile, api.worker)
    #config = api.worker.config

    api.worker._vars = {
    }



def _teardown(api):
    vars = getattr(api.worker, '_vars')
    if not vars:
        return


def api_method(f):
    def wrapper(*args, **kwargs):
        api = args[0]
        api.create_app()
        try:
            curdir = os.getcwd()
            log_command(f.__name__, kwargs)
            with tools.environment_append(api.worker.conf.env_vars):
                _setup(api)
                return f(*args, **kwargs)
        except Exception as exc:
            msg = exception_message_safe(exc)
            try:
                log_exception(exc, msg)
            except BaseException:
                pass
            raise
        finally:
            _teardown(api)
            os.chdir(curdir)
    return wrapper


def _make_abs_path(path, cwd=None, default=None):
    """convert 'path' to absolute if necessary (could be already absolute)
    if not defined (empty, or None), will return 'default' one or 'cwd'
    """
    cwd = cwd or os.getcwd()
    if not path:
        abs_path = default or cwd
    elif os.path.isabs(path):
        abs_path = path
    else:
        abs_path = os.path.normpath(os.path.join(cwd, path))
    return abs_path


class Worker(object):
    def __init__(self, cache_folder, user_io, conan, context):
        self._context = context or {}
        self._profile_manifests = None
        self._conf = None  # epm config file items
        self._configuration = None  # project configuration
        self._project = None

        # User IO, interaction and logging
        self.user_io = user_io
        self.out = self.user_io.out
        self.cache_folder = cache_folder
        self.conan = conan
        interactive = not self.conf.non_interactive
        if not interactive:
            self.user_io.disable_input()


    @property
    def conf(self):
        if self._conf is None:
            if not os.path.exists(self.epm_conf_path):
                save(self.epm_conf_path, normalize(default_client_conf))

            self._conf = EPMClientConfigParser(self.epm_conf_path)
        return self._conf

    @property
    def configuration(self):
        if self._configuration is None:
            name = self._context.get('configuration') or \
                   os.environ.get('EPM_CONFIGURATION')

            self._configuration = Configuration(name, self)
        return self._configuration

    @property
    def project(self):
        if self._project is None:
            self._project = Project(self.configuration, self)
        return self._project

    @property
    def epm_conf_path(self):
        return os.path.join(self.cache_folder, 'epm.conf')

    @property
    def profiles(self):
        if self._profile_manifests is None:
            config = self.conf
            if not os.path.exists(config.profile_folder):
                src = os.path.join(os.path.dirname(epm.__file__), 'data', 'profiles')
                shutil.copytree(src, config.profile_folder)

            manifests = {}
            for filename in glob.glob('%s/*.yml' % config.profile_folder):
                name = os.path.basename(filename)[:-4]
                with open(filename) as f:
                    manifests[name] = yaml.safe_load(f)
                manifests[name]['__file__'] = os.path.abspath(filename)

            self._profile_manifests = manifests

        return self._profile_manifests


def _determine_runner(profile, policy, type):
    if policy == 'shell':
        return policy

    docker = profile.manifest.get('docker', {}).get('builder')

    if policy == 'docker' and not docker:
        raise EException('profile <%s> without %s docker configuration.' % type)

    if policy == 'auto':
        return 'docker' if docker else 'shell'

    raise EException('unsupported %s-policy  %s' % (type, policy))


class WorkerAPI(object):
    @classmethod
    def factory(cls):
        return cls()

    def __init__(self, cache_folder=None, output=None, user_io=None, conan=None, context={}):
        color = colorama_initialize()
        self.out = output or Output(sys.stdout, sys.stderr, color)
        self.user_io = user_io or UserIO(out=self.out)
        self.cache_folder = cache_folder or os.path.join(get_epm_user_home(), ".epm")
        self.worker = None  # Api calls will create a new one every call

        self.conan = conan
        self.context = context

    def create_app(self):
        self.worker = Worker(self.cache_folder, self.user_io, self.conan, self.context)
        return self.worker

    @api_method
    def build(self, steps, runner):

        runner = _determine_runner(self.worker.configuration.profile, runner, 'builder')

        if runner == 'shell':
            return Builder.shell(self, steps)
        elif runner == 'docker':
            return Builder.docker(self, steps)
        raise EException('unsupported runner %s' % runner)

    @api_method
    def create(self, clear, cache, runner):

        runner = _determine_runner(self.worker.configuration.profile, runner, 'builder')

        if runner == 'shell':
            return Creator.shell(self, clear, cache)
        elif runner == 'docker':
            return Creator.docker(self, clear, cache)
        raise EException('unsupported runner %s' % runner)

    @api_method
    def sandbox_(self, program, params=[]):
        commands = self.worker.project.manifest.get('sandbox', {}).keys()
        if program not in commands:
            raise Exception('Invalid sandbox command <{}>.\nsandbox command as below:\n    {}'.format(
                program, "\n    ".join(commands)))

        sandbox = Sandbox(self.worker.project,
                          self.worker.conf.register,
                          self.out)
        return sandbox.exec(program, params)

    @api_method
    def sandbox(self, verbose=True):
        out = None
        if verbose:
            out = self.worker.out or Output(sys.stdout)

        sandbox = Sandbox(self.worker.project,
                          self.worker.conf.register,
                          out)
        return sandbox




