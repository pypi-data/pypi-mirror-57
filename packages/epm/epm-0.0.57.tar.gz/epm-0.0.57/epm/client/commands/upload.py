import os
import yaml
import subprocess
from epm.utils import ArgparseArgument, get_channel
from epm.paths import  conan_storage_path
from epm.client.commands import Command, register_command
from epm.errors import EException


class Upload(Command):
    doc = 'Upload build package to conan server.'
    name = 'upload'

    def __init__(self):
        args = [
            ArgparseArgument("-r", "--remote", default=None,
                             help="the remote to be upload the package, if not set use the of user in package.yml."),
            ArgparseArgument("--conan", default=False, action="store_true",
                             help="upload the local conan cache or package in project .conan"),

        ]

        Command.__init__(self, args)

    def run(self, api, args):
        with open('package.yml') as f:
            package = yaml.safe_load(f)
        remote = args.remote or package.get('user')
        channel = get_channel()
        reference = '{name}/{version}@'.format(**package)
        reference += '{}/{}'.format(remote, channel)
        if args.conan:
            storage_path = conan_storage_path()
        else:
            storage_path = os.path.abspath('.conan')
        env = os.environ
        env['CONAN_STORAGE_PATH'] = storage_path

        configuration = args.epm_configuration
        if not configuration:
            proc = subprocess.run(['conan', 'upload', '--all',  '--force', '--remote', remote, reference],
                                  env=env, check=True)
            return proc.returncode

        # upload specified package
        with open(os.path.join('.epm', configuration, 'package.json')) as f:
            import json
            pkg = json.load(f)

        id = pkg['id']
        if not id:
            raise EException('[upload] Invalid id:', id)

        proc = subprocess.run(['conan', 'upload', '--force', '--remote', remote,
                               '{}:{}'.format(reference, id)], env=env, check=True)
        return proc.returncode




# -------------------------------------
# Register command
#
register_command(Upload)
