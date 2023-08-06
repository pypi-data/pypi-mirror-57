import os
import yaml
import subprocess
import urllib
import tarfile
import zipfile
from subprocess import run
import  tempfile

from epm.utils import ArgparseArgument as Argument

from epm.client.commands import Command, register_command
from epm.utils.files import rmdir, mkdir, tar_extract
from urllib.parse import urlparse
from jinja2 import Environment, BaseLoader
from epm.utils import system_info
from epm.client.tools.venv import VirtualEnviron

PLATFORM, ARCH = system_info()


class VEnv(Command):
    doc = 'Setup EPM virtual development enviroment.'
    name = 'venv'

    def __init__(self):

        args = {
            'setup': {
                'help': 'Setup virtual development environment from a local or remote zip file.'
                        'The virtual environment installed in current work dir',
                'arguments': [
                    Argument('path', nargs=1,
                             help='virtual environment setup package/folder location path'),

                    Argument('--name', default=None,
                             help="virtual environment name. if not set, use config file's name")
                ]
            },

            'list': {
                'help': 'List all installed virtual environment.'
            },

            'banner': {
                'help': 'Show virtual enviroment banner.'
            },

            'clear': {
                'help': 'Clear setup virtual environments.',
                'arguments': [
                    Argument('name', nargs='*',
                             help='virtual environment to be clean')
                ]
            },

            'active': {
                'help': 'Active virtual environments.',
                'arguments': [
                    Argument('name', nargs=1,
                             help='The name of virtual environment to be actived.')
                ]
            }

        }

        Command.__init__(self, args)

    def run(self, api, args):
        print(args)
        action = getattr(self, '{}_action'.format(args._action))
        return action(args)

    def _register(self):
        filename = os.path.expanduser('.epm/venv.yml')
        venv = {}
        if os.path.exists(filename):
            with open(filename) as f:
                venv = yaml.safe_load(f)
        return venv

    def _save_register(self, venv):
        filename = os.path.expanduser('.epm/venv.yml')
        with open(filename, 'w') as f:
            yaml.safe_dump(venv, f, default_flow_style=False, indent=2)

    def setup_action(self, args):
        venv = VirtualEnviron(args.name)
        venv.setup(args.path[0])

    def active_action(self, args):
        venv = VirtualEnviron(args.name[0])
        venv.active()

    def list_action(self, args):
        venv = VirtualEnviron()
        print(" \n".join(venv.register().keys()))

    def banner_action(self, args):
        print(VirtualEnviron.banner())




# -------------------------------------
# Register command
#
register_command(VEnv)
