
import os
import yaml

from epm.utils import ArgparseArgument
from epm.client.commands import Command, register_command
from epm.client.tools.project import Initializer
from epm.errors import EException


class Init(Command):
    doc = 'Create epm project.'
    name = 'init'

    def __init__(self):
        args = [
            ArgparseArgument("--name", default=None,
                             help="When specified, create a epm package with the specified name."
                             "if this not set, it will read from package.yml@name field"
                             "if the package.yml not exists or no name filed"
                             "if not set and not exists in package.yml use folder name"),

            ArgparseArgument("--version", default=None,
                             help="When specified, create a epm package with the specified version."
                             "if this not set, it will read from package.yml@version field"
                             "if the package.yml not exists or no version filed, 0.0.1 will set"),

            ArgparseArgument("--type", default='app',
                             help="What kind of project created for this package."
                                  "'lib' - C/C++ library or `app` - executable application"),
            ]
        
        Command.__init__(self, args)

    def run(self, api, args):
        try:
            initializer = Initializer(args)
            initializer.generate()
        except EException as e:
            raise e
        except Exception as e:
            raise EException(str(e))
        return 0



# -------------------------------------
# Register command
#


register_command(Init)
