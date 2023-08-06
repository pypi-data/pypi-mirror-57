
import os
import subprocess
import paramiko
from epm.errors import EException, EProgramNotExists, InvalidNameException
from epm.paths import conan_storage_path

from epm.utils import system_info
from epm.enums import Platform, Architecture

from epm.model.register import Register

from epm.utils.log import project_logger as logger
log = logger('sandbox')


PLATFORM, ARCH = system_info()


# http://www.pixelbeat.org/programming/linux_binary_compatibility.html

from epm.paths import normalize_path


def decode(text, encoding=None):
    import codecs
    if encoding:
        return text.decode(encoding)

    encodings = {codecs.BOM_UTF8: "utf_8_sig",
                 codecs.BOM_UTF16_BE: "utf_16_be",
                 codecs.BOM_UTF16_LE: "utf_16_le",
                 codecs.BOM_UTF32_BE: "utf_32_be",
                 codecs.BOM_UTF32_LE: "utf_32_le",
                 b'\x2b\x2f\x76\x38': "utf_7",
                 b'\x2b\x2f\x76\x39': "utf_7",
                 b'\x2b\x2f\x76\x2b': "utf_7",
                 b'\x2b\x2f\x76\x2f': "utf_7",
                 b'\x2b\x2f\x76\x38\x2d': "utf_7"}
    for bom in sorted(encodings, key=len, reverse=True):
        if text.startswith(bom):
            try:
                return text[len(bom):].decode(encodings[bom])
            except UnicodeDecodeError:
                continue

    decoders = ["utf-8", "Windows-1252", "Windows-936"]
    for decoder in decoders:
        try:
            return text.decode(decoder)
        except UnicodeDecodeError:
            continue
    return text.decode("utf-8", "ignore")  # Ignore not compatible characters


class SSH(object):

    def __init__(self, username, password, hostname, port=22, out=None):
        self._ssh = None
        self.out = out

        self._hostname = hostname
        self._port = port
        self._username = username
        self._password = password
        self._wd = '~'

        self.LD_LIBRARY_PATH = None

    def _info(self, msg):
        if self.out:
            self.out.info(msg)

    def open(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._info('SSH connecting %s:%d with <%s>' % (self._hostname, self._port, self._username))
        ssh.connect(hostname=self._hostname, port=self._port, username=self._username, password=self._password)
        self._ssh = ssh

    def close(self):
        if self._ssh:
            self._ssh.close()
            del self._ssh

    def set_wd(self, wd):
        self._wd = wd

    def call(self, cmd, cmd_dir=None, timeout=None, check=False):

        if isinstance(cmd, list):
            cmd = " ".join(cmd)
        script = ''
        if cmd_dir:
            script += "cd %s;" % cmd_dir

        if self.LD_LIBRARY_PATH:
            script += ' export LD_LIBRARY_PATH=%s:$LD_LIBRARY_PATH;' % self.LD_LIBRARY_PATH

        script += cmd

        _, stdout, stderr = self._ssh.exec_command(script, timeout=timeout)
        code = stdout.channel.recv_exit_status()
        if check and code:
            raise subprocess.CalledProcessError(code, 'failed command: {} '.format(cmd))

        out = stdout.read()
        if stderr:
            out += stderr.read()

        return code, out


class Remote(object):

    def __init__(self,  local):
        self.ssh = None
        self._local = local

    def open(self, hostname, ssh):

        self.ssh = SSH(username=ssh.username,
                       password=ssh.password,
                       hostname=hostname,
                       port=ssh.port)
        self.ssh.open()

    def close(self):
        self.ssh.close()

    def mount(self, source, directory, local=None):
        local = local or self._local

        src = source
        if source[1] == ':':
            src = source.replace(':', '')
        src = normalize_path(src)
        try:
            self.ssh.call('[[ -d {0} ]] && umount {0}'.format(directory))
        except:
            pass

        if local.mount == 'cifs':
            cmd = 'mount -t cifs -o user={username},pass={password},noserverino //{hostname}/{source} {directory}'.format(
                hostname=local.hostname, username=local.username, password=local.password,
                source=src, directory=directory)
        elif local.mount == 'nfs':
            cmd = 'mount -t nfs -o nolock {hostname}:{source} {directory}'.format(
                hostname=local.hostname, username=local.username, password=local.password,
                source=src, directory=directory)
        else:
            raise Exception('unsupported mount protocol %s' % local.mount)

        return self.ssh.call(cmd)


class Excutor(object):

   def __init__(self, name, args, sandbox):

       self._stdout = bytes()
       self._sandbox = sandbox
       self._args = args
       self._name = name
       self._returncode = None
       self._proc = None
       self._filename = normalize_path(self._sandbox.filename(name))

       if not os.path.exists(self._filename) and not os.path.exists(self._filename+'.cmd'):
           raise FileNotFoundError('program <{}> ({}) not exists.'.format(self._name, self._filename))

   def run(self, timeout=None, check=False):

       self._returncode, self._stdout = self._sandbox.run(self._filename, self._args, timeout)
       if check and self._returncode:
           raise subprocess.CalledProcessError(self._returncode, self._name)

   def stdout(self, encoding='auto'):
       '''decoding accoring encoding indicate

       :param decoding:
          - None  not decode (bytes)
          - auto try best
          - other
       :return:
       '''
       if encoding is None:
           return self._stdout
       encoding = None if encoding == 'auto' else encoding
       return decode(self._stdout, encoding)

   @property
   def returncode(self):
       return self._returncode


class Sandbox(object):

    _is_docker_startup = None

    def __init__(self, project, register=None, out=None):
        self._project = project
        self._register_filename = register
        self._out = out
        self._runner = None
        self._verbose = None
        self._device = None
        self._register = None

    def excutor(self, name, args=[]):

        self.initialize()
        commands = self._project.manifest.get('sandbox', {}).keys()
        if name not in commands:
            raise InvalidNameException('Invalid sandbox command <{}>.\n'
                                       'valid sandbox command (see package.yml):\n'
                                       '* {}'.format(name, "\n* ".join(commands)))

        return Excutor(name, args, self)

    def info(self, data):
        if self._out:
            self._out.info(data)

    @property
    def arch(self):
        return self._project.configuration.profile.settings['arch']

    @property
    def platform(self):
        return self._project.configuration.profile.settings['os']

    @property
    def _has_docker(self):
        if Sandbox._is_docker_startup is None:
            try:
                proc = subprocess.run(['docker', '--version'], capture_output=True)
                Sandbox._is_docker_startup = bool(proc.returncode == 0)
            except:
                Sandbox._is_docker_startup = False
        return Sandbox._is_docker_startup

    @property
    def register(self):
        if self._register is None:
            self._register = Register(self._register_filename)
        return self._register

    def initialize(self):
        if self._runner is None:
            self._runner = self.runner_type()

            if self._runner == 'remote':
                self._init_device()

    def runner_type(self):
        policy = os.environ.get('EPM_SANDBOX_RUNNER', 'auto')
        runners = self._get_runners()
        if policy == 'auto':
            return runners[0]

        if policy in runners:
            return policy

        raise subprocess.SubprocessError(
            'Not suitable runner for current policy {}(EPM_SANDBOX_RUNNER), supported runners [{}]'.format(
                policy, " ,".join(runners)))

    def _get_runners(self):

        if self.platform not in [Platform.WINDOWS, Platform.LINUX]:
            raise subprocess.SubprocessError('Unsupported OS %s' % self.platform)

        if self.arch not in [Architecture.ARMv7, Architecture.X86_64, Architecture.X86]:
            raise subprocess.SubprocessError('Unsupported CPU architecture %s' % self.arch)

        if self.platform == Platform.WINDOWS:
            if PLATFORM == Platform.WINDOWS:
                if self.arch in [Architecture.X86_64, Architecture.X86]:
                    if self.arch == ARCH or \
                            (self.arch == Architecture.X86 and ARCH == Architecture.X86_64):
                        return ['shell']
            raise subprocess.SubprocessError('Windows {} program can not run under {} platform'.format(
                self.arch, ARCH))

        if self.platform == Platform.LINUX and self.arch in [Architecture.X86_64, Architecture.X86]:
            if PLATFORM == Platform.WINDOWS:
                if self._has_docker:
                    return ['docker']
                raise subprocess.SubprocessError(
                    'Linux program could not run without docker on Windows')

            # host is Linux
            runners = ['shell'] if self.arch == ARCH else []

            if self._has_docker:
                if os.environ.get('EPM_SANDBOX_RUNNER') in [None, 'docker']:
                    runners += ['shell']
            if not runners:
                raise subprocess.SubprocessError(
                    "No suitable runners for Linux {} program in currernt {} {} system".format(
                        self.platform, PLATFORM, ARCH))
            return runners

        if self.platform == Platform.LINUX and self.arch in [Architecture.ARMv7]:
            return ['remote']

        subprocess.SubprocessError("No suitable runners for {} {} program in currernt {} {} system".format(
                PLATFORM, self.platform, PLATFORM, ARCH))

    def _init_device(self):

        remote = None
        for name, device in self.register.devices.items():
            if not device.system:
                continue
            if self.platform != device.system.os:
                continue
            if self.arch != device.system.arch:
                continue

            profile = self._project.configuration.profile
            if profile.settings.get('os.crt') == device.system.crt:
                remote = device
                break

        if not remote:
            raise subprocess.SubprocessError('No valid device')

        if not remote.ssh:
            raise subprocess.SubprocessError('No SSH configure for device.')

        device = Remote(self.register.local)
        device.open(remote.hostname, remote.ssh)

        project = normalize_path(os.path.abspath('.'))
        storage = conan_storage_path()
        for i in ['project', 'conan']:
            code, out = device.ssh.call('mkdir -p /mnt/epm/{}'.format(i))
            if code:
                self.info('mkdir {} on device failed.'.format(i))

        code, out = device.mount(project, '/mnt/epm/project')
        if code:
            self.info('mount {} on device failed.'.format(i))
            raise EException('mount project {} on device failed.')

        code, out = device.mount(storage, '/mnt/epm/conan')
        if code:
            self.info('mount {} on device failed.'.format(i))
            raise EException('mount conan storage {} on device failed.')

        self._device = device

    def _run_device(self, filename, args, env, timeout):
        exports = 'export EPM_SANDBOX_PROJECT=/mnt/epm/project;export EPM_SANDBOX_STORAGE=/mnt/epm/conan;'
        return self._device.ssh.call(exports + '/mnt/epm/project/%s %s' % (filename, " ".join(args)))

    def _run_shell(self, filename, args, env, timeout):

        filename = os.path.normpath(filename)
        if PLATFORM == Platform.WINDOWS:
            filename += '.cmd'

        docker_env = {
            'EPM_SANDBOX_PROJECT': self._project.directory,
            'EPM_SANDBOX_RUNNER': 'shell'
        }

        if env:
            docker_env = dict(docker_env, **env)

        try:
            proc = subprocess.run([filename] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  env=docker_env, timeout=timeout)
        except FileNotFoundError:
            raise EProgramNotExists('program {} not exists.'.format(filename))
        except Exception as e:
            raise e

        return proc.returncode, proc.stdout

    def _run_docker(self, filename, args, env, timeout):

        profile = self._project.configuration.profile
        docker = profile.manifest.get('docker', {}).get('runner')

        if not docker:
            raise EException('No docker configured')
        docker_env = {
            'EPM_SANDBOX_PROJECT': self._project.directory,
            'EPM_SANDBOX_RUNNER': 'docker',
            'EPM_SANDBOX_IMAGE': docker.get('image'),
            'EPM_SANDBOX_SHELL': docker.get('shell', '/bin/bash')
        }
        if env:
            docker_env = dict(docker_env, **env)
        return self._run_shell(filename, args, env=docker_env, timeout=timeout)

    def filename(self, name):
        return os.path.join(self._project.out_folder, 'sandbox', name)

    def run(self, filename, args, timeout, env=None):
        env = env if env else os.environ.copy()
        if self._runner == 'shell':
            return self._run_shell(filename, args, env, timeout)
        elif self._runner == 'docker':
            return self._run_docker(filename, args, env, timeout)
        elif self._runner == 'remote':
            return self._run_device(filename, args, env, timeout)
        else:
            raise EException('unsupported sandbox runner type <{}>'.format(self._runner))


