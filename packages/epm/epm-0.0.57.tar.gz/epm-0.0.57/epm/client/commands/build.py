
import os
import yaml

from epm.utils import ArgparseArgument
from epm.client.commands import Command, register_command
from epm.worker.build import Builder
# from epm.paths import normalize_path

class Build(Command):
    doc = 'Build your local package according conanfile.py, package.yml.'
    name = 'build'

    def __init__(self):
        args = [

            ArgparseArgument("--runner", default='auto', help=""),

            ArgparseArgument("-c", "--configure", default=None, action="store_true",
                             help="Execute the configuration step. "
                                  "When specified, package/install/test_package won't run unless "
                                  "--package/--install/--test specified"),

            ArgparseArgument("-p", "--package", default=None, action="store_true",
                             help="Execute the package build step. "
                                  "When specified, configure/install/test_package won't run unless "
                                  "--configure/--install/--test specified"),

            ArgparseArgument("-i", "--install", default=None, action="store_true",
                             help="Execute the install step (variable should_install=True). When "
                                  "When specified, configure/package/test_package won't run unless "
                                  "--configure/--package/--test_package specified"),

            ArgparseArgument("-t", "--test_package", default=None, action="store_true",
                             help="Execute the test step (variable should_test=True). When "
                                  "When specified, configure/package/install won't run unless "
                                  "--configure/--package/--install specified")
  
            ]
        
        Command.__init__(self, args)

    def run(self, api, args):

        steps = ['configure', 'package', 'install', 'test_package']
        selected = []
        for i in steps:
            if getattr(args, i, False):
                selected.append(i)
        steps = selected if selected else steps

        api.build(steps, args.runner)
        return 0

# -------------------------------------
# Register command
#
register_command(Build)
