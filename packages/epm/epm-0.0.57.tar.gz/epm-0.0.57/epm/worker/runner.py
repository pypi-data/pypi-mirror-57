import io
import os
import sys
from contextlib import contextmanager
from subprocess import PIPE, Popen, STDOUT
from epm.errors import EException

from conans.util.files import decode_text

from epm.utils.log import project_logger as logger
log = logger()

class _UnbufferedWrite(object):
    def __init__(self, stream):
        self._stream = stream

    def write(self, *args, **kwargs):
        self._stream.write(*args, **kwargs)
        self._stream.flush()


class Runner(object):

    def __init__(self, output=None, env=None):
        self._output = output
        self._env = env

    def __call__(self, command, output=None, cwd=None):
        """
        @param command: Command to execute
        @param output: Instead of print to sys.stdout print to that stream. Could be None
        @param log_filepath: If specified, also log to a file
        @param cwd: Move to directory to execute
        """

        stream_output = output if output and hasattr(output, "write") else self._output or sys.stdout
        if hasattr(output, "flush"):
            # We do not want output from different streams to get mixed (sys.stdout, os.system)
            stream_output = _UnbufferedWrite(stream_output)

        with pyinstaller_bundle_env_cleaned():
            return self._pipe_os_call(command, stream_output, cwd)

    def _pipe_os_call(self, command, stream_output, cwd):

        try:
            # piping both stdout, stderr and then later only reading one will hang the process
            # if the other fills the pip. So piping stdout, and redirecting stderr to stdout,
            # so both are merged and use just a single get_stream_lines() call
            proc = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, cwd=cwd, env=self._env)
        except Exception as e:
            raise EException("Error while executing '%s'\n\t%s" % (command, str(e)))

        def get_stream_lines(the_stream):
            while True:
                line = the_stream.readline()
                if not line:
                    break
                decoded_line = decode_text(line)
                if stream_output:
                    try:
                        stream_output.write(decoded_line)
                    except UnicodeEncodeError:  # be aggressive on text encoding
                        decoded_line = decoded_line.encode("latin-1", "ignore").decode("latin-1",
                                                                                       "ignore")
                        stream_output.write(decoded_line)

        get_stream_lines(proc.stdout)
        # get_stream_lines(proc.stderr)

        proc.communicate()
        ret = proc.returncode
        return ret

#    def _simple_os_call(self, command, cwd):
#        if not cwd:
#            return os.system(command)
#        else:
#            try:
#                old_dir = get_cwd()
#                os.chdir(cwd)
#                result = os.system(command)
#            except Exception as e:
#                raise ConanException("Error while executing"
#                                     " '%s'\n\t%s" % (command, str(e)))
#            finally:
#                os.chdir(old_dir)
#            return result
#

if getattr(sys, 'frozen', False) and 'LD_LIBRARY_PATH' in os.environ:

    # http://pyinstaller.readthedocs.io/en/stable/runtime-information.html#ld-library-path-libpath-considerations
    pyinstaller_bundle_dir = os.environ['LD_LIBRARY_PATH'].replace(
        os.environ.get('LD_LIBRARY_PATH_ORIG', ''), ''
    ).strip(';:')

    @contextmanager
    def pyinstaller_bundle_env_cleaned():
        """Removes the pyinstaller bundle directory from LD_LIBRARY_PATH

        :return: None
        """
        ld_library_path = os.environ['LD_LIBRARY_PATH']
        os.environ['LD_LIBRARY_PATH'] = ld_library_path.replace(pyinstaller_bundle_dir,
                                                                '').strip(';:')
        yield
        os.environ['LD_LIBRARY_PATH'] = ld_library_path

else:
    @contextmanager
    def pyinstaller_bundle_env_cleaned():
        yield
