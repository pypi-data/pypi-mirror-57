import os
import sys
import yaml


from epm.client.commands import Command, register_command
from epm.utils import ArgparseArgument
from epm.utils import system_info
from epm.client.output import Output

PLATFORM, ARCH = system_info()


class Sandbox(Command):
    doc = 'run sandbox command'
    name = 'sandbox'

    def __init__(self):
        args = [
            ArgparseArgument('name', nargs=1, help='Project directory (that is conan recipe folder)')
            ]
        
        Command.__init__(self, args)

    def run(self, api, args, params):
        name = args.name[0]

        sandbox = api.sandbox()
        program = sandbox.excutor(name, params)
        program.run()
        out = Output(sys.stdout, sys.stderr, True)
        #print(program.stdout())
        out.write(program.stdout())
        return program.returncode


# -------------------------------------
# Register command
#
register_command(Sandbox)
