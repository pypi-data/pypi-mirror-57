
import time
import platform
import subprocess
from epm.worker.runner import Runner
from epm.utils.log import project_logger as logger
log = logger()


class Docker(object):

    def __init__(self, config):
        self.config = config
        self.volume = {}
        self.volumes = []
        self.env = {}
        self.WD = None
        self.home = config['home']

    def run(self, cmd, out=None):

        image = self.config['image']
        shell = self.config['shell']

        script = []

        if 'Ubuntu' in platform.platform():
            script = ['sudo']

        script += ['docker', 'run', '--rm', '--name', 'epm-%s' % time.monotonic()]
        if self.WD:
            script += ['-w', self.WD]

        for docker_path, host_path in self.volume.items():
            script += ['-v', '%s:%s' % (host_path, docker_path)]

        for k, v in self.env.items():
            script += ['-e', '%s=%s' % (k, v)]
        script += ['-e', 'EPM_EXEC_WITH_DOCKER=Yes']
        script += [image, shell, '-c', cmd]
        log.info("run docker with command: {}\n".format("\n  ".join(script)))

        runner = Runner(out)
        return runner(script, out)

        #subprocess.run(script, check=True)

