
import os
import yaml
import urllib
import shutil
import tarfile
import zipfile
import tempfile
from jinja2 import PackageLoader, Environment
import subprocess

from epm.utils.files import rmdir, mkdir, tar_extract
from urllib.parse import urlparse
from jinja2 import Environment, BaseLoader
from epm.client.output import Output
from epm.utils import system_info

PLATFORM, ARCH = system_info()


_Banner = '''
                 
      __________  __  ___
     / ____/ __ \/  |/  / VIRTUAL ENVIROMENT {name}
    / __/ / /_/ / /|_/ /  
   / /___/ ____/ /  / /   Channel: {channel}
  /_____/_/   /_/  /_/    
                               
@{instd}

'''

_SetupHint = '''
{name} virtual environment setup done, run active script to startup
In Windows
   $ active.bat
In Linux
   $ source ./active.sh

or use epm
   $ epm venv active {name}
  
 
'''
class VirtualEnviron(object):

    def __init__(self, name=None, directory=None, out=None):
        self._name = name or os.environ.get('EPM_VENV_NAME')
        self._directory = directory or os.environ.get('EPM_VENV_DIR')
        self._reg_filename = os.path.expanduser('~/.epm/venv.yml')
        print('******', self._reg_filename)
        self._jinja2 = Environment(loader=PackageLoader('epm', 'data/venv'))
        self._venv = None
        import sys
        self._out = out or Output(sys.stdout)

    def register(self):
        if not os.path.exists(self._reg_filename):
            return {}

        with open(self._reg_filename) as f:
            return yaml.safe_load(f)

    def update(self, venv, name=None):
        name = name or self._name
        reg = self.register()
        reg[name] = venv
        with open(self._reg_filename, 'w') as f:
            yaml.safe_dump(reg, f, default_flow_style=False, indent=2)

    def install_source(self, path):
        url = urlparse(path)
        config_folder = path

        if url.scheme in ['http', 'https']:
            download_dir = tempfile.mkdtemp(suffix='epm.download')
            filename = os.path.join(download_dir, os.path.basename(path))
            urllib.request.urlretrieve(path, filename)
            config_folder = os.path.join(download_dir, 'venv.config')
            zfile = zipfile.ZipFile(filename)
            zfile.extractall(config_folder)

        if not os.path.exists(config_folder):
            raise Exception('Invalid install path {}'.format(path))
        return config_folder

    def setup(self, url):
        reg = self.register()
        if self._name and reg.get(self._name) is not None:
            raise Exception('{} venv already installed, clear it try again.'.format(self._name))

        if os.path.exists('.conan'):
            raise Exception('current directory is dirty .conan is exits.')

        instd = self.install_source(url)
        path = os.path.join(instd, 'config.yml')
        with open(path) as f:
            conf = yaml.safe_load(f)

        name = self._name or conf['name']
        if reg.get(name) is not None:
            raise Exception('{} venv already installed, clear it try again.'.format(self._name))

        wd = os.path.abspath('.')
        channel = conf.get('channel', 'testing')
        self._venv = {
            'install-source': url,
            'name': name,
            'install-dir': wd,
            'config': conf
        }

        self.update(self._venv, name)


        env = os.environ.copy()
        env['CONAN_USER_HOME'] = wd
        env['EPM_USER_HOME'] = wd
        venv = self._venv
        try:
            subprocess.run(['conan', 'remote', 'clean'], env=env)

            remotes = conf.get('conan', {}).get('remotes', [])
            for remote in remotes:
                for name, url in remote.items():
                    proc = subprocess.run(['conan', 'remote', 'add', name, url], env=env)
                    if proc.returncode:
                        self._out.error('setup conan remote {} failed, cancel setup.'.format(self._name))
                        raise Exception('setup failed')
        except Exception as e:
            if os.path.exists('.conan'):
                shutil.rmtree('.conan')
            raise e

        def render(template, filename):
            tmpl = self._jinja2.get_template(template)
            content = tmpl.render(name=self._venv['name'],
                                  path=self._venv['install-dir'],
                                  channel=channel)

            with open(filename, 'w') as f:
                f.write(content)

        render('active.bat', 'active.bat')
        render('active.sh', 'active.sh')
        self._out.info(_SetupHint.format(name=name))

    def active(self):
        env = os.environ.copy()
        if env.get('EPM_VENV_NAME') or env.get('EPM_VENV_DIR'):
            self._out.error('venv can not be active in a venv shell.')
            return

        reg = self.register()
        venv = reg.get(self._name)
        if not venv:
            self._out.error('{} venv not setup.'.format(self._name))
            return

        instd = venv.get('install-dir')
        if not instd or not os.path.exists(instd) or \
                not os.path.isdir(instd + '/.conan') or \
                not os.path.isdir(instd + '/.epm') or \
                not os.path.isfile(instd + '/active.bat') or\
                not os.path.isfile(instd + '/active.sh'):
            self._out.error('{} install dir({}) was destroyed.'.format(self._name,instd))
            return

        script = os.path.join(instd, 'active.{}'.format('bat' if PLATFORM == 'Windows' else 'sh'))

        if PLATFORM == 'Windows':
            subprocess.run(['cmd.exe', '/k', script], env=env)
        else:
            # TODO:
            pass
            #subprocess.run(['/bin/bash','-i', script)

    @staticmethod
    def banner():
        return _Banner.format(name=os.environ.get('EPM_VENV_NAME'),
                              channel=os.environ.get('EPM_CHANNEL'),
                              instd=os.environ.get('EPM_VENV_DIR'))






