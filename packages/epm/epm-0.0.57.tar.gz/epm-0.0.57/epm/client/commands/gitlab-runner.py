import os
import yaml
import subprocess
from epm.utils import ArgparseArgument
from epm.client.commands import Command, register_command
from epm.errors import EException


import os
import sys
import stat
import yaml
import shutil
import urllib
import urllib.request
import argparse
import platform
import subprocess
import glob
from string import Template

from epm.utils import system_info
PLATFORM, ARCH = system_info()

_DIR = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

_GITLAB_RUNNER = 'http://vss.kedacom.com/downloads/software/Gitlab-Runner/gitlab-runner-linux-amd64'
if platform.system() == 'Windows':
    _GITLAB_RUNNER = 'http://vss.kedacom.com/downloads/software/Gitlab-Runner/gitlab-runner-windows-amd64.exe'


class GitlabRunner(object):

    def __init__(self, args):
        self._WD = os.path.normpath(os.path.abspath('.')).replace('\\', '/')
        self._suffix = ''
        self._config = None

    def _gitlab_runner(self, argv, retry=0, hint='', sudo=False):

        cmd = ['sudo'] if sudo else []
        if platform.system() == 'Windows':
            cmd += ['gitlab-runner.exe']
        else:
            cmd += ['./gitlab-runner']

        cmd += argv

        for i in range(retry+1):
            proc = subprocess.run(cmd)
            if not proc.returncode:
                return 0
            if i < retry:
                import time
                time.sleep(0.5)
                print('try %s %d times' % (hint, i))

        return proc.returncode

    def _install_runner(self, url):
        if isinstance(url, dict):
            url = url.get(platform.system().lower())

        ext = '.exe' if platform.system() == 'Windows' else ''
        filename = os.path.abspath('gitlab-runner' + ext)
        if os.path.exists(filename):
            return

        if not url:
            raise EException('No runner download url given.')

        try:

            with urllib.request.urlopen(url) as f:
                with open(filename, 'wb') as runner:
                    runner.write(f.read())
        except Exception as e:
            print('download gitlab runner %s failed\n %s' % (_GITLAB_RUNNER, str(e)))
            raise e
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

    def _argument(self, type, suffix=''):
        def _(s):
            return Template(s).substitute(WD=self._WD, suffix=suffix)

        if self._config is None:
            filename = os.path.join(self._WD, 'config.yml')
            if not os.path.exists(filename):
                raise EException("no register.yml in %s" % self._WD)

            with open(filename) as f:
                self._config = yaml.safe_load(f)
        runner = self._config.get(type)

        if not runner:
            raise Exception('no {} type runner for {} configured.'.format(type, name))

        items = []
        for option, value in runner.items():
            if value is None:
                items += ['--%s' % option]
            elif isinstance(value, str):
                items += ['--%s' % option, _(value)]
            elif isinstance(value, list):
                for i in value:
                    items += ['--%s' % option, _(i)]
            else:
                raise Exception('Invalid format of item %s.%s' % (name, value))

        return ['register', '--non-interactive', '--config', 'config.toml', '--locked=false'] + items


    def register(self, retry=10):

        def _(s, suffix=''):
            return Template(s).substitute(WD=self._WD, suffix=suffix)

        with open('register.yml') as f:
            reg = yaml.safe_load(f)

        prop = reg.get('.property', {})
        if '.property' in reg.keys():
            del reg['.property']

        self._install_runner(prop.get('gitlab-runner'))

        runners = []
        for name, value in reg.items():
            url = value['url']
            token = value['token']
            for type in value.get('runner', []):
                args = self._argument(type, '@'+name)
                args += ['--registration-token', token, '--url', url]
                runners.append(args)

        try:
            for runner in runners:
                if self._gitlab_runner(runner, 10):
                    raise EException('register {} failed.'.format(name))
        except:
            print('register <%s> failed, unregister all registered runner.' % name)
            self.unregister()
            return 1

        return 0

    def unregister(self):
        return self._gitlab_runner(['unregister', '--config', 'config.toml', '--all-runners'])

#    def run(self, sudo):
#        return self._gitlab_runner(['run', '--config', 'config.toml'], sudo=sudo)
#
#    def stop(self, sudo, abort=False):
#        cmd = ['sudo'] if sudo else []
#        if abort:
#            cmd += ['killall', '-SIGINT', '-SIGTERM', 'gitlab-runner']
#        else:
#            cmd += ['killall', '-SIGINT', 'gitlab-runner']
#        subprocess.run(cmd)


class GitlabRunnerCommand(Command):
    doc = 'Configure GitLab runner.'
    name = 'gitlab-runner'

    def __init__(self):
        args = {
            'register': {
                'help': 'Register gitlab runner according config.yml and register.yml.'
            },

            'unregister': {
                'help': 'Unregister all runners.'
            }
        }

        Command.__init__(self, args)

    def run(self, api, args):
        gitlab = GitlabRunner(args)

        action = args._action
        if action == 'register':
            ret = gitlab.register()
        elif action == 'unregister':
            ret = gitlab.unregister()
        return ret
#        elif action == 'stop':
#            gitlab.stop(args.sudo, args.abort)
#        else:
#            gitlab.run(args.sudo)
#        #return proc.returncode




# -------------------------------------
# Register command
#
register_command(GitlabRunnerCommand)
