import os
import sys
import yaml
import subprocess

from epm.errors import EException
from epm.client.commands import Command, register_command
from epm.utils import ArgparseArgument



import re

from epm.utils import system_info
from epm.enums import Platform, Architecture
PLATFORM, ARCH = system_info()


class Script(object):
    P_COMMAND = re.compile(r'((\$\{(?P<sandbox>sandbox)\})|\.)/(?P<program>\S+)')
    P_ARGV = re.compile(r'\$(?P<value>[0-9\*])$')
    P_KEY = re.compile(r'\$\{(?P<value>profile)\}$')

    def __init__(self, name, params, configuration=None, platform=None):
        self._name = name
        self._configuration = configuration or 'None'
        self._params = params or []
        self._platform = platform or PLATFORM

    def commands(self):
        cmds = []
        for expr in self._load():
            cmds.append(self._parse(expr))
        return cmds

    def _load(self):
        with open('package.yml', 'r') as f:
            package = yaml.safe_load(f)

        scripts = package.get('script', {})
        script = scripts.get(self._name)

        if not isinstance(script, (str, list)):
            raise EException('Invalid command name %s (package.yml script section)' % self._name)

        return [script] if isinstance(script, str) else script

    def _parse(self, expr):
        expr = expr.replace('${configuration}', self._configuration)
        tokens = expr.split(' ')
        program = tokens[0]
        EXTs = ['.exe', '.cmd', '.bat'] if self._platform == Platform.LINUX else ['.sh']
        argv = tokens[1:]

        if os.path.exists(program):
            if program.endswith('.py'):
                return 'python', program, argv

        for ext in EXTs:
            if os.path.exists(program + ext):
                program += ext
                break
        return 'shell', program, argv


class Run(Command):
    doc = 'run package command'
    name = 'run'

    def __init__(self):
        args = [
            ArgparseArgument('name', nargs=1, help='Project directory (that is conan recipe folder)')
            ]
        
        Command.__init__(self, args)

    def run(self, api, args, params):
        name = args.name[0]
        script = Script(name, params, args.epm_configuration)
        env = os.environ.copy()
        if args.epm_configuration:
            env['EPM_CONFIGURATION'] = args.epm_configuration
        else:
            env['EPM_CONFIGURATION'] = 'None'
        timeout = 60*20
        for runner, program, argv in script.commands():
            if runner == 'python':
                proc = subprocess.run(['python', program] + argv + params, env=env, timeout=timeout)

            else:
                proc = subprocess.run([program] + argv + params, env=env, timeout=timeout)

            if proc.returncode:
                return proc.returncode
        return 0


# -------------------------------------
# Register command
#
register_command(Run)
