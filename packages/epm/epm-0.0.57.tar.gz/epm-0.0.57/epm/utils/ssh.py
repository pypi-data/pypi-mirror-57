import sys
import subprocess
import paramiko

from epm.client.output import Output

class SSH(object):

    def __init__(self, username, password, hostname, port=22, out=None):
        self.ssh_ = None
        self.out = out or Output(sys.stdout)

        self.hostname_ = hostname
        self.port_ = port
        self.username_ = username
        self.password_ = password
        self.stdout_ = None
        self.stderr_ = None
        self._wd = '~'

        self.LD_LIBRARY_PATH = None

    def open(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.out.info('SSH connecting %s:%d with <%s>' % (self.hostname, self.port, self.username))
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
        self.ssh_ = ssh

    def close(self):
        if self.ssh_:
            self.ssh_.close()
            self.ssh_ = None

    def set_wd(self, wd):
        self._wd = wd

    @property
    def ssh(self):
        if not self.ssh_:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.out.info('SSH connecting %s:%d with <%s>' % (self.hostname_, self.port_, self.username_))
            ssh.connect(hostname=self.hostname_, port=self.port_, username=self.username_, password=self.password_)
            self.ssh_ = ssh
        return self.ssh_

    def exec(self, cmd, cmd_dir=None, timeout=None):

        if isinstance(cmd, list):
            " ".join(cmd)

        if cmd_dir is None:
            cmd_dir = self._wd
        code, out, err = self._call(cmd, cmd_dir, timeout)
        self.out.write(out.read())
        return code

    def call(self, cmd, cmd_dir=None, timeout=None, check=False):
        code, self.stdout_, self.stderr_ = self._call(cmd, cmd_dir, timeout)
        if check and code:
            def _(stream):
                return stream.read().decode('utf-8', errors='ignore')
            raise subprocess.SubprocessError(code, cmd, _(self.stdout_), _(self.stderr_))
        return code

    def _call(self, cmd, cmd_dir=None, timeout=None):

        if isinstance(cmd, list):
            cmd = " ".join(cmd)
        script = ''
        if cmd_dir:
            script += "cd %s;" % cmd_dir

        if self.LD_LIBRARY_PATH:
            script += ' export LD_LIBRARY_PATH=%s:$LD_LIBRARY_PATH;' % self.LD_LIBRARY_PATH

        script += cmd

        _, stdout, stderr = self.ssh.exec_command(script, timeout=timeout)
        code = stdout.channel.recv_exit_status()
#        o = stdout.decode('utf-8', errors='ignore')
#        e = stderr.decode('utf-8', errors='ignore')

#        self.out.info('SSH(%s:%s) %s (exit code %s) \n[out]:%s\n[err]:%s\n' % (self.hostname_, self.port_, cmd,
#                  code, o, e))
#        self.out.write(stdout.read())
#        if stderr:
#            self.out.write(stderr.read())


        return code, stdout, stderr

    @staticmethod
    def _stream(s, encoding):
        if s is None:
            return ''
        s = s.read()
        if encoding is None:
            return s
        return s.decode(encoding, errors='ignore')

    def stdout(self, encoding='utf-8'):
        return SSH._stream(self.stdout_, encoding)

    def stderr(self, encoding='utf-8'):
        return SSH._stream(self.stderr_, encoding)
