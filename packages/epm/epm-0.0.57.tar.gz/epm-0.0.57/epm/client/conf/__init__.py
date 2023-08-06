import os

from configparser import ConfigParser, NoSectionError

from epm.errors import EException
from epm.model.env_info import unquote
from epm.utils.env_reader import get_env
from epm.utils.files import load
import logging

default_client_conf = """
[log]
run_to_output = True        # environment EPM_LOG_RUN_TO_OUTPUT
run_to_file = False         # environment EPM_LOG_RUN_TO_FILE
level = 50                  # environment EPM_LOGGING_LEVEL
# trace_file =              # environment EPM_TRACE_FILE
print_run_commands = False  # environment EPM_PRINT_RUN_COMMANDS

[general]
sysrequires_sudo = True               # environment EPM_SYSREQUIRES_SUDO
request_timeout = 60                  # environment EPM_REQUEST_TIMEOUT (seconds)
# non_interactive = False             # environment EPM_NON_INTERACTIVE

[profile]
# This is the default path, but you can write your own. It must be an absolute path or 
# relative to the epm user home, not to the working directory)
# if the directory not exists epm will copy build-in profiles
folder = ./profiles

[register]
# This is the default path, but you can write your own. It must be an absolute path or 
# relative to the epm user home, not to the working directory)
path = ./regster.yml

[sandbox]
log_level = 50
log_to_output = False
log_to_file = True

[hooks]    # environment EPM_HOOKS
placeholder

"""


class EPMClientConfigParser(ConfigParser, object):

    def __init__(self, filename):
        ConfigParser.__init__(self, allow_no_value=True)
        self.read(filename)
        self.filename = filename

    # So keys are not converted to lowercase, we override the default optionxform
    optionxform = str

    @property
    def env_vars(self):
        ret = {"EPM_LOG_RUN_TO_OUTPUT": self._env_c("log.run_to_output", "EPM_LOG_RUN_TO_OUTPUT", "True"),
               "EPM_LOG_RUN_TO_FILE": self._env_c("log.run_to_file", "EPM_LOG_RUN_TO_FILE", "False"),
               "EPM_LOGGING_LEVEL": self._env_c("log.level", "EPM_LOGGING_LEVEL", "50"),
               "EPM_TRACE_FILE": self._env_c("log.trace_file", "EPM_TRACE_FILE", None),
               "EPM_PRINT_RUN_COMMANDS": self._env_c("log.print_run_commands", "EPM_PRINT_RUN_COMMANDS", "False"),
               "EPM_NON_INTERACTIVE": self._env_c("general.non_interactive", "EPM_NON_INTERACTIVE", "False"),

               "EPM_SANDBOX_LOG_TO_OUTPUT": self._env_c("sandbox.log_to_output", "EPM_SANDBOX_LOG_TO_OUTPUT", "False"),
               "EPM_SANDBOX_LOG_TO_FILE": self._env_c("sandbox.log_to_file", "EPM_SANDBOX_LOG_TO_FILE", "True"),
               "EPM_SANDBOX_LOGGING_LEVEL": self._env_c("sandbox.log_level", "EPM_SANDBOX_LOGGING_LEVEL", "10"),

               "EPM_HOOKS": self._env_c("hooks", "EPM_HOOKS", None),

               }

        # Filter None values
        return {name: value for name, value in ret.items() if value is not None}

    def _env_c(self, var_name, env_var_name, default_value):
        env = os.environ.get(env_var_name, None)
        if env is not None:
            return env
        try:
            return unquote(self.get_item(var_name))
        except EException:
            return default_value

    def get_item(self, item):
        if not item:
            return load(self.filename)

        tokens = item.split(".", 1)
        section_name = tokens[0]
        try:
            section = self.items(section_name)
        except NoSectionError:
            raise EException("'%s' is not a section of conan.conf" % section_name)
        if len(tokens) == 1:
            result = []
            if section_name == "hooks":
                for key, _ in section:
                    result.append(key)
                return ",".join(result)
            else:
                for section_item in section:
                    result.append(" = ".join(section_item))
                return "\n".join(result)
        else:
            key = tokens[1]
            try:
                value = dict(section)[key]
                if " #" in value:  # Comments
                    value = value[:value.find(" #")].strip()
            except KeyError:
                raise EException("'%s' doesn't exist in [%s]" % (key, section_name))
            return value

    def set_item(self, key, value):
        tokens = key.split(".", 1)
        section_name = tokens[0]
        if not self.has_section(section_name):
            self.add_section(section_name)

        if len(tokens) == 1:  # defining full section
            raise EException("You can't set a full section, please specify a key=value")

        key = tokens[1]
        try:
            super(ConanClientConfigParser, self).set(section_name, key, value)
        except ValueError:
            # https://github.com/conan-io/conan/issues/4110
            value = value.replace("%", "%%")
            super(ConanClientConfigParser, self).set(section_name, key, value)

        with open(self.filename, "w") as f:
            self.write(f)

    def rm_item(self, item):
        tokens = item.split(".", 1)
        section_name = tokens[0]
        if not self.has_section(section_name):
            raise EException("'%s' is not a section of conan.conf" % section_name)

        if len(tokens) == 1:
            self.remove_section(tokens[0])
        else:
            key = tokens[1]
            if not self.has_option(section_name, key):
                raise EException("'%s' doesn't exist in [%s]" % (key, section_name))
            self.remove_option(section_name, key)

        with open(self.filename, "w") as f:
            self.write(f)

    def get_conf(self, varname):
        """Gets the section from config file or raises an exception"""
        try:
            return self.items(varname)
        except NoSectionError:
            raise EException("Invalid configuration, missing %s" % varname)

    @property
    def profile_folder(self):
        # Try with EPM_PROFILE_FOLDER
        result = get_env('EPM_PROFILE_FOLDER', None)
        if not result:
            # Try with epm.conf "path"
            try:
                current_dir = os.path.dirname(self.filename)
                result = dict(self.get_conf("profile"))["folder"]
                if result.startswith("."):
                    result = os.path.abspath(os.path.join(current_dir, result))
            except (KeyError, EException):  # If storage not defined, to return None
                pass

        if result:
            if not os.path.isabs(result):
                raise EException("EPM Profile path has to be an absolute path")
        return result

    @property
    def register(self):
        # Try with EPM_DEVICE_REGISTER
        result = get_env('EPM_REGISTER', None)

        if not result:
            # Try with epm.conf "path"
            try:

                current_dir = os.path.dirname(self.filename)
                result = dict(self.get_conf("register"))["path"]

                if result.startswith("."):
                    result = os.path.abspath(os.path.join(current_dir, result))
            except (KeyError, EException):  # If storage not defined, to return None
                pass

        if result:
            if not os.path.isabs(result):
                raise EException("Conan storage path has to be an absolute path")

        return result

    @property
    def hooks(self):
        hooks = get_env("EPM_HOOKS", list())
        if not hooks:
            try:
                hooks = self.get_conf("hooks")
                hooks = [k for k, _ in hooks]
            except EException:
                hooks = []
        return hooks

    @property
    def non_interactive(self):
        try:
            non_interactive = get_env("EPM_NON_INTERACTIVE")
            if non_interactive is None:
                non_interactive = self.get_item("general.non_interactive")
            return non_interactive.lower() in ("1", "true")
        except EException:
            return False

    @property
    def logging_level(self):
        try:
            level = get_env("EPM_LOGGING_LEVEL")
            if level is None:
                level = self.get_item("log.level")
            try:
                level = int(level)
            except Exception:
                level = logging.CRITICAL
            return level
        except EException:
            return logging.CRITICAL

    @property
    def logging_file(self):
        return get_env('EPM_LOGGING_FILE', None)

    @property
    def print_commands_to_output(self):
        try:
            print_commands_to_output = get_env("EPM_PRINT_RUN_COMMANDS")
            if print_commands_to_output is None:
                print_commands_to_output = self.get_item("log.print_run_commands")
            return print_commands_to_output.lower() in ("1", "true")
        except EException:
            return False

    @property
    def generate_run_log_file(self):
        try:
            generate_run_log_file = get_env("EPM_LOG_RUN_TO_FILE")
            if generate_run_log_file is None:
                generate_run_log_file = self.get_item("log.run_to_file")
            return generate_run_log_file.lower() in ("1", "true")
        except EException:
            return False

    @property
    def log_run_to_output(self):
        try:
            log_run_to_output = get_env("EPM_LOG_RUN_TO_OUTPUT")
            if log_run_to_output is None:
                log_run_to_output = self.get_item("log.run_to_output")
            return log_run_to_output.lower() in ("1", "true")
        except EException:
            return True

    @property
    def sandbox_logging_level(self):
        try:
            level = get_env("EPM_SANDBOX_LOGGING_LEVEL")
            if level is None:
                level = self.get_item("sandbox.log_level")
            try:
                level = int(level)
            except Exception:
                level = logging.CRITICAL
            return level
        except EException:
            return logging.CRITICAL

