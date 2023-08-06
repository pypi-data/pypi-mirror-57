# coding=utf-8
# ported from conans/paths
import os
import platform
from conans.client.conan_api import Conan

if platform.system() == "Windows":
    from epm.utils.windows import epm_expand_user
else:
    from epm.utils.files import rmdir

    epm_expand_user = os.path.expanduser


def get_epm_user_home():
    user_home = os.getenv("EPM_USER_HOME", "~")
    tmp = epm_expand_user(user_home)
    if not os.path.isabs(tmp):
        raise Exception("Invalid EPM_USER_HOME value '%s', "
                        "please specify an absolute or path starting with ~/ "
                        "(relative to user home)" % tmp)
    return os.path.abspath(tmp)


def normalize_path(path):
    return os.path.normpath(path).replace('\\', '/')

def conan_storage_path():
    conan, _, _ = Conan.factory()
    conan.create_app()
    return normalize_path(conan.app.config.storage_path)


# Files and Folers
CONANFILE = 'conanfile.py'
EPMFILE = "package.yml"
BUILDMETAFILE= "build-meta.yml"

BUILDFOLDER = 'build'
TESTBUILDFOLDER = 'test_build'
PACKAGEFOLDER = 'package'


