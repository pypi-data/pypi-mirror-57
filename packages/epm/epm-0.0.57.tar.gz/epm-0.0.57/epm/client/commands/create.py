
import os

from epm.utils import ArgparseArgument
from epm.client.commands import Command, register_command


class Create(Command):
    doc = 'Create your local package according conanfile.py, package.yml.'
    name = 'create'

    def __init__(self):
        args = [

            ArgparseArgument("--runner", default='auto', help=""),

            ArgparseArgument("--clear", default=False, action="store_true",
                            help="Execute the clean action for the build intermediate files"),

            ArgparseArgument("--cache", default=False, action="store_true",
                            help="Take project .conan as conan_storage_path")

            ]
        
        Command.__init__(self, args)

    def run(self, api, args):

        api.create(args.clear, args.cache, args.runner)

        return 0


# -------------------------------------
# Register command
#
register_command(Create)
