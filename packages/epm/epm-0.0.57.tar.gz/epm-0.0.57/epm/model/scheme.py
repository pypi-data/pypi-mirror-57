import os
import yaml
import pprint

from conans.client.profile_loader import read_profile

from conans.model.options import OptionsValues

from epm.paths import get_epm_user_home, conan_storage_path

from epm.utils import system_info, get_channel

from epm.errors import EException

from epm.utils.log import project_logger as logger
log = logger()


class Scheme(object):

    def __init__(self, name, worker):
        self._name = name
        self._scheme = None  # options name
        self._worker = worker


    @property
    def name(self):
        return self._name

    @property
    def options(self):
        return self._options(False)

    @property
    def link_options(self):
        return self._options(True)

    def _parse(self, name, manifest=None):
        ''' parse the package (manifest) scheme (options) information

        :param name: name of scheme to be parsed
        :param manifest: manifest (package.yml)
        :return:
        '''

        manifest = manifest or self._worker.project.manifest
        configuration = manifest.get('configuration', {})
        scheme = configuration.get('scheme', {}).get(name, {})
        dependencies = manifest.get('dependencies', {})

        # pick up options of this package.yml
        options = {k: v for k, v in scheme.items() if k[0] != '.'}
        deps = {}

        for pkg, sch in scheme.get('.dependencies', {}).items():

            info = dependencies.get(pkg)  # get dependent package info
            if not info:
                raise EException('less information of %s, miss dependencies in package.yml ' % name)

            deps[pkg] = {**info, 'scheme': sch}

        return options, deps

    def _load_dep_schemes(self, libs, deps, storage=None):

        for name, info in deps.items():
            if name in libs.keys():
                continue

            scheme = info['scheme']
            version = info['version']
            user = info['user']

            channel = info.get('channel', 'stable')

            conan = self._worker.conan
            reference = '%s/%s@%s/%s' % (name, version, user, channel)
            recipe = conan.inspect(reference, [], user)
            storage = storage or conan_storage_path()
            path = os.path.join(storage, name, version, user, channel, 'export', 'package.yml')
            with open(path) as f:
                manifest = yaml.safe_load(f)

            options, deps = self._parse(scheme, manifest)

            libs[name] = {'manifest': manifest, 'recipe': recipe, 'options': options, 'scheme.deps': deps}

            log.info('scheme of {} reference={} loaded: \n{}'.format(
                name, reference, pprint.pformat(libs[name], indent=2)))

            self._load_dep_schemes(libs, deps, storage)

    def _options(self, link):
        log.info('{} scheme.option link={}'.format(self._name, link))

        options, deps = self._parse(self.name)
        libs = {}
        self._load_dep_schemes(libs, deps)

        items = {}
        for k, v in options.items():
            key = '%s:%s' % (self._worker.project.name, k) if link else k
            items[key] = v

        for name, info in libs.items():
            for k, v in info['options'].items():
                key = '%s:%s' % (name, k)
                items[key] = v

        log.info('{} scheme.options link={}\n{}'.format(self._name, link, pprint.pformat(items, indent=2)))
        return OptionsValues(items)

