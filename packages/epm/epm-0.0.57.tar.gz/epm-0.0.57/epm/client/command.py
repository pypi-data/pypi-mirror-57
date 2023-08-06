

# cerbero - a multi-platform build system for Open Source software
# Copyright (C) 2012 Andoni Morales Alastruey <ylatuya@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.


import argparse
import os
import sys
import errno
import traceback

import yaml
from epm import __version__
from epm.client import commands
from epm.errors import EException
from epm.worker.api import WorkerAPI
from conans.client.conan_api import Conan
from epm.utils.log import project_logger as logger
from epm.client.output import Output, colorama_initialize

log = logger()


description = 'Enterprise package management for C/C++ development (base on conan).'


class Main(object):

    def __init__(self, args):
        color = colorama_initialize()
        self.out = Output(sys.stdout, sys.stderr, color)
        self.argv = args
        self.create_parser()
        self.load_commands()
        self.parse_arguments(args)
        self.run_command()

    def log_error(self, msg, print_usage=False, command=None):
        """ Log an error and exit

        :param msg:
        :param print_usage:
        :param command:
        :return:
        """

        if command is not None:
            self.out.error("***** Error running '%s' command:" % command)
        self.out.warn('%s' % msg)
        if print_usage:
            self.parser.print_usage()
        sys.exit(1)

    def create_parser(self):
        """ Creates the arguments parser
        :return:
        """
        self.parser = argparse.ArgumentParser(description=description)

        self.parser.add_argument('--version', default=False, action="store_true",
                dest='epm_version', help='Show version of this installed epm')

        self.parser.add_argument('-c', '--configuration', type=str, default=None,
                dest='epm_configuration', help='Configuration for the command')

    def parse_arguments(self, argv):
        """ Parse the command line argument
        :param args:
        :return:
        """
        # If no commands, make it show the help by default
        if len(argv) == 0:
            argv = ["-h"]

        self.params = None
        n = min(len(argv), 3)
        for i in range(n):
            if argv[i] in ['sandbox', 'run']:
                self.params = argv[i+2:]
                argv = argv[:i+2]
                break

        self.args = self.parser.parse_args(argv)

        if self.args.epm_version:
            print('EPM', __version__)
            sys.exit(0)

    def load_commands(self):
        subparsers = self.parser.add_subparsers(help='sub-command help',
                                                dest='command')
        commands.load_commands(subparsers)

    def run_command(self):
        command = self.args.command
        try:
            self._param_validate()
            os.environ['EPM_CONFIGURATION'] = self.args.epm_configuration or 'None'
            os.environ['CONAN_REVISIONS_ENABLED'] = '1'

            conan, _, _ = Conan.factory()
            api = WorkerAPI(conan=conan)
            res = commands.run(command, self.args, self.params, api)
#        except EException as exc:
#            log.info(traceback.format_exc())
#
#            self.log_error(exc, False, command)
        except KeyboardInterrupt:
            self.log_error('Interrupted')
        except IOError as e:
            if e.errno != errno.EPIPE:
                raise
            sys.exit(0)

        except BaseException as e:
            log.info(traceback.format_exc())

            detail = 'see .epm/project.log for details.'
            self.log_error('{}\n{}'.format(e, detail), False, command)

            sys.exit(127)

        if res:
            sys.exit(res)

    def _param_validate(self):
        if self.args.epm_configuration:
            with open('package.yml') as f:
                pkg = yaml.safe_load(f)

            configuration = pkg.get('configuration', {})
            tokens = self.args.epm_configuration.split('@')
            scheme = None

            if len(tokens) == 1:
                name = tokens[0]
            else:
                name = tokens[0]
                scheme = tokens[1]

            worker = WorkerAPI().create_app()
            profiles = []
            for name, profile in worker.profiles.items():
                profiles += profile.keys()
                profiles.remove('__file__')

            #profiles = configuration.get('profile', [])
            #profiles += [f+'.d' for f in profiles]

            if name not in profiles:
                raise EException('Unsupported profile <%s>, package.configuration support %d profiles:\n %s' %
                                 (name, len(profiles), "  \n".join(profiles)))

            if scheme in [None, 'default']:
                return

            schemes = configuration.get('scheme', {}).keys()
            if scheme not in schemes:
                raise EException('Invalid scheme name <{}>, please use below schemes:\n {}'.format(
                    scheme, "  \n".join(schemes)))

    def _profile_validate(self, profile):
        if not profile:
            return

        with open('package.yml') as f:
            pkg = yaml.safe_load(f)
        profiles = pkg.get('profile', {})
        tokens = profile.split('@')
        scheme = None
        if len(tokens) == 1:
            name = tokens[0]
        else:
            name = tokens[0]
            scheme = tokens[1]

        families = profiles.get('family', [])
        families += [f+'.d' for f in families]

        if name not in families:
            raise EException('Unsupported profile <%s>, it is not valid profile (%s).' %
                             (name, families))

        if scheme in [None, 'default']:
            return

        if scheme not in profiles.get('options', {}).keys():
            raise EException('Invalid options name <%s>' % scheme)


def main(args):
    Main(args)


if __name__ == '__main__':
    Main(sys.argv[1:])
