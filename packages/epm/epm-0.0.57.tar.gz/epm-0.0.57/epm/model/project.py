import os
import yaml
import shutil
from string import Template

from conans.client.profile_loader import read_profile

from conans.model.options import OptionsValues

from epm.paths import normalize_path, conan_storage_path
from epm.utils.files import rmdir, mkdir
from epm.client.conf.detect import _get_default_compiler
from epm.utils.docker import Docker
from epm.utils import system_info, get_channel
from epm.enums import Platform, Architecture
from epm.client.output import Output

from epm.model.configuration import Configuration
PLATFORM, ARCH = system_info()

DEFALT_CONAN_LAYOUT = '''
[includedirs]
include

[builddirs]
${out_dir}/build

[libdirs]
${out_dir}/build/lib

[bindirs]
${out_dir}/build/bin

[resdirs]
${out_dir}/build/res
'''


class Project(object):

    def __init__(self, configuration, worker):
        self._manifest = None
        self.directory = normalize_path(os.path.abspath('.'))
        self._worker = worker
        self._out = worker.out
        self._configuration = configuration

    def initialize(self, create=True):
        if create:
            if os.path.exists(self.out_folder):
                rmdir(self.out_folder)
            mkdir(self.out_folder)
            shutil.copy(self.profile.filename, os.path.join(self.out_folder, 'profile'))
            self._generate_layout()

    def _generate_layout(self):
        manifest = self.manifest
        template = manifest.get('conan.layout', DEFALT_CONAN_LAYOUT)
        layout = Template(template)

        text = layout.substitute(out_dir=self.out_folder)
        with open(self.layout, 'w') as f:
            f.write(text)
            f.flush()

    def save(self, private={}):
        info = {'private': private}
        if os.environ.get('EPM_EXEC_WITH_DOCKER'):
            info['exec_with_docker'] = True
        info['project'] = self.directory
        storage = os.environ.get('CONAN_STORAGE_PATH', conan_storage_path())
        info['conan_storage_path'] = normalize_path(storage)

        with open(self.info_filename, 'w') as f:
            yaml.dump(info, f, default_flow_style=False)

    @property
    def name(self):
        return self.manifest['name']

    @property
    def version(self):
        return self.manifest['version']

    @property
    def user(self):
        return self.manifest['user']

    @property
    def channel(self):
        return get_channel()

    @property
    def reference(self):
        return '%s/%s@%s/%s' % (self.name, self.version, self.user, self.channel)

    @property
    def configuration(self):
        return self._configuration

    @property
    def profile(self):
        return self._configuration.profile

    @property
    def scheme(self):
        return self._configuration.scheme

    @property
    def out_folder(self):
        return '.epm/%s' % self.configuration.name

    @property
    def build_folder(self):
        return '%s/build' % self.out_folder

    @property
    def package_folder(self):
        return '%s/package' % self.out_folder

    @property
    def test_folder(self):
        return '%s/test_package' % self.out_folder

    @property
    def layout(self):
        return '%s/conan.layout' % self.out_folder

    @property
    def manifest(self):
        if self._manifest is None:
            with open('package.yml', 'r') as f:
                self._manifest = yaml.safe_load(f)

        return self._manifest

    @property
    def info_filename(self):
        return '%s/project.yml' % self.out_folder
