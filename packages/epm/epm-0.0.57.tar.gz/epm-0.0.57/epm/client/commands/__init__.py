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


__all__ = ['Command', 'register_command', 'run', 'Extender']

import os
import argparse


from epm.errors import EException


class Command:
    """Base class for Command objects"""

    doc = ''
    name = None

    def __init__(self, arguments=[]):
        self.arguments = arguments

    def run(self, context, args):
        """The body of the command"""
        raise NotImplementedError

    def add_parser(self, subparsers):
        self.parser = subparsers.add_parser(self.name, help=self.doc)

        if isinstance(self.arguments, dict):
            actions = self.parser.add_subparsers(dest='_action', help=' {} action command help'.format(self.name))
            for name, cmd in self.arguments.items():

                help = cmd.get('help', '')
                args = cmd.get('arguments', [])

                action = actions.add_parser(name, help=help)
                for arg in args:
                    arg.add_to_parser(action)
        else:
            for arg in self.arguments:
                arg.add_to_parser(self.parser)


# dictionary with the list of commands
# command_name -> command_instance
_commands = {}


def register_command(command_class):
    command = command_class()
    _commands[command.name] = command


def load_commands(subparsers):
    import os
    commands_dir = os.path.abspath(os.path.dirname(__file__))

    for name in os.listdir(commands_dir):
        name, extension = os.path.splitext(name)
        if extension != '.py':
            continue
        try:
            __import__('epm.client.commands.%s' % name)
        except ImportError as e:
            print("Error importing command %s:\n %s" % (name, e))
    for command in _commands.values():
        command.add_parser(subparsers)


def run(command, args, params, worker_api):
    # if the command hasn't been registered, load a module by the same name
    
    if command not in _commands:
        raise EException('command <%s> not found' % command)

    if command in ['run', 'sandbox']:
        return _commands[command].run(worker_api, args, params)

    return _commands[command].run(worker_api, args)


class Extender(argparse.Action):
    """Allows to use the same flag several times in a command and creates a list with the values.
    For example:
        conan install MyPackage/1.2@user/channel -o qt:value -o mode:2 -s cucumber:true
      It creates:
          options = ['qt:value', 'mode:2']
          settings = ['cucumber:true']
    """
    def __call__(self, parser, namespace, values, option_strings=None):  # @UnusedVariable
        # Need None here incase `argparse.SUPPRESS` was supplied for `dest`
        dest = getattr(namespace, self.dest, None)
        if not hasattr(dest, 'extend') or dest == self.default:
            dest = []
            setattr(namespace, self.dest, dest)
            # if default isn't set to None, this method might be called
            # with the default as `values` for other arguments which
            # share this destination.
            parser.set_defaults(**{self.dest: None})

        if isinstance(values, str):
            dest.append(values)
        elif values:
            try:
                dest.extend(values)
            except ValueError:
                dest.append(values)


