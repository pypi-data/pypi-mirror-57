import os
import yaml


from conans.client.profile_loader import read_profile

from conans.model.options import OptionsValues

from epm.paths import get_epm_user_home, conan_storage_path

from epm.utils import system_info

from epm.errors import EException

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


class Profile(object):

    def __init__(self, name, worker):
        self._name = name
        self._scheme = None  # options name
        self._manifest = None
        self._profile = None
        self._filename = None
        self._worker = worker

        if name:
            tokens = name.split('@')
            if len(tokens) == 1:
                self._name = tokens[0]
                self._scheme = 'default'
            else:
                self._name = tokens[0]
                self._scheme = tokens[1]

    @property
    def name(self):
        return self._name

    @property
    def profile(self):
        if self._profile is None:
            if self.manifest:
                cwd = os.path.join(self._worker.conf.profile_folder)
                self._profile, _ = read_profile(self.name, cwd, cwd)
        return self._profile

    @property
    def manifest(self):

        if self._manifest is None and self._name:
            manifests = self._worker.profiles

            for name, m in manifests.items():
                if self._name in m.keys():
                    self._manifest = m[self._name]
                    self._filename = os.path.join(
                        os.path.dirname(m['__file__']), self._name)
                    break

            if self._manifest is None:
                raise EException('profile name %s not installed in epm system.' % self._name)

        return self._manifest

    @property
    def settings(self):
        return self.profile.settings

    @property
    def filename(self):
        if self._filename is None:
            self.manifest
        return self._filename
