import sys
import os
import logging
import logging.config
from logging import StreamHandler


class MultiLineFormatter(logging.Formatter):
    def format(self, record):
        str_ = logging.Formatter.format(self, record)
        separator = record.message if record.message else None
        if separator is None:
            return separator
        tmp = str_.split(separator)
        if len(tmp) == 2:
            header, _ = tmp
        else:
            header = tmp
        str_ = str_.replace('\n', '\n' + ' ' * len(header))
        return str_


def configure_logger(logging_level=logging.CRITICAL, logging_file=None, name='epm'):
    # #### LOGGER, MOVED FROM CONF BECAUSE OF MULTIPLE PROBLEM WITH CIRCULAR INCLUDES #####
    logger = logging.getLogger(name)
    if logging_file is not None:
        hdlr = logging.FileHandler(logging_file)
    else:
        hdlr = StreamHandler(sys.stderr)

    formatter = MultiLineFormatter('%(levelname)-6s:%(filename)-15s[%(lineno)d]: '
                                   '%(message)s [%(asctime)s]')
    hdlr.setFormatter(formatter)
    for hand in logger.handlers:
        logger.removeHandler(hand)
    logger.addHandler(hdlr)
    logger.setLevel(logging_level)
    return logger


logger = configure_logger()

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0


_PROJECT_LOG_CONF = '''
[loggers]
keys=root,flog

[handlers]
keys=console,file

[formatters]
keys=fmconsole, fmfile

[logger_root]
level=NOTSET
qualname=root
handlers=file

[logger_flog]
level=NOTSET
qualname=flog
handlers=file


[handler_console]
class=StreamHandler
level=INFO
formatter=fmconsole
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=DEBUG
formatter=fmfile
args=('.epm/project.log','a')

[formatter_fmfile]
#format=%(asctime)s %(filename)s %(levelname)s  %(message)s
format=[ %(asctime)s %(levelname)-6s %(filename)s:%(lineno)d ] %(message)s  
#datefmt=%Y-%m-%d %H:%M:%S
datefmt=%H:%M:%S

[formatter_fmconsole]
format=[%(levelname)s]  %(message)s
datefmt=%Y-%m-%d %H:%M:%S

'''

_project_logger_inited = False

_loggers = {}


def project_logger(name='root'):
    global _loggers
    global _project_logger_inited
    if not _project_logger_inited:
        if not os.path.exists('.epm'):
            os.makedirs('.epm')
        path = os.path.join('.epm', 'log.ini')
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write(_PROJECT_LOG_CONF)
        logging.config.fileConfig(path)
        _project_logger_inited = True
    return logging.getLogger(name)
