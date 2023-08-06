import os
import yaml
import subprocess
from string import Template
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from scp import SCPClient

from epm.utils import ArgparseArgument, get_channel
from epm.paths import  conan_storage_path
from epm.client.commands import Command, register_command
from epm.errors import EException

from urllib.parse import urlparse

class MKDocs(Command):
    doc = 'mkdocs.'
    name = 'mkdocs'

    def __init__(self):
        args = [

            ArgparseArgument("--build", default=False, action="store_true",
                             help="build docs"),
            ArgparseArgument("--serve", default=False, action="store_true",
                             help="start mkdocs server"),
            ArgparseArgument("--config-file", default=None,
                             help="Provide a specific MkDocs config, otherwise try ./mkdocs.yml and ./docs/mkdocs.yml"),

            ArgparseArgument("--site-dir", default=".epm/site",
                             help="The directory to output the result of the documentation build." \
                                  "${name}, ${version} can be used which will be read from package.ym." \
                                  "for example .epm/site/${name}/${version}"),

            ArgparseArgument("--upload", default=False, action="store_true",
                             help="upload --site_dir specifed directory docs to remote"),

            ArgparseArgument("--remote-url", default=None,
                             help="location to upload, if not set read from ${EPM_DOCS_URL}"\
                             "only support ssh for now. example ssh://vss.kedacom.com/docs"),

            ArgparseArgument("--username", default=None,
                             help="upload username"),

            ArgparseArgument("--token", default=None,
                             help="upload password or RSAKey"),

        ]

        Command.__init__(self, args)

    def run(self, api, args):
        with open('package.yml') as f:
            package = yaml.safe_load(f)

        config_file = args.config_file
        params = args.site_dir
        for i in ['name', 'version']:
            params = params.replace('@{%s}' % i, package[i])

        site_dir = Template(params).substitute(package)

        if args.build or args.serve:
            if config_file:
                if not os.path.exists(config_file):
                    raise EException('mkdocs config file {} not exists.'.format(config_file))
            else:
                for i in ['mkdocs.yml', 'docs/mkdocs.yml']:
                    if os.path.exists(i):
                        config_file = i
                        break
                if not config_file:
                    raise EException("Not able to find mkdocs.yml or docs/mkdocs.yml")

        if args.build:
            config_dir = os.path.dirname(config_file) or '.'
            site_dir = os.path.relpath(site_dir, config_dir)
            subprocess.run(['mkdocs', 'build', '-f', config_file, '-d', site_dir], check=True)

        if args.serve:
            subprocess.run(['mkdocs', 'serve', '-f', config_file, '--dirtyreload'], check=True)

        if args.upload:
            self.upload(args, site_dir)
        return 0

    def upload(self, args, folder):
        url = args.remote_url or os.environ.get('EPM_DOCS_URL')
        username = args.username or os.environ.get('EPM_DOCS_USERNAME')
        token = args.token or os.environ.get('EPM_DOCS_TOKEN')
        private_key = None
        password = None
        if not username or not token:
            raise EException('No valid username {} or token {}'.format(
                username if username else 'NONE',
                '***' if token else 'NONE'))

        if os.path.exists(token):
            private_key = RSAKey.from_private_key_file(token)
        else:
            password = token

        ssh = SSHClient()

        ssh.set_missing_host_key_policy(AutoAddPolicy())

        remote = urlparse(url)
        if remote.scheme != 'ssh':
            raise EException("only ssh supported for now.")

        ssh.connect(remote.netloc, username=username, password=password, pkey=private_key)
        scp = SCPClient(ssh.get_transport())
        scp.put(folder, recursive=True, remote_path=remote.path)
#        with open('package.yml') as f:
        # SCPCLient takes a paramiko transport as an argument#            package = yaml.safe_load(f)
#
#        if os.path.exists('.epm/upload-docs'):
#            import shutil
#            shutil.rmtree('.epm/upload-docs')
#
#        name = package['name']
#        version = package['version']
#
#        cache = '.epm/upload-docs/{}'.format(name)
#        os.makedirs(cache)
#        os.rename('.epm/site/{}'.format(version), '{}/{}'.format(cache, version))
#        scp.put(cache, recursive=True, remote_path=remote.path)






# -------------------------------------
# Register command
#
register_command(MKDocs)
