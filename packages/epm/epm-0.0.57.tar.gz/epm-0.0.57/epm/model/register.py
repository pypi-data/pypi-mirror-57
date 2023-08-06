import yaml
from collections import namedtuple
from epm.enums import Platform, Architecture
from epm.utils import system_info
PLATFORM, ARCH = system_info()


class _REQUIRED(object):
    pass


def _section(name, prototype, data):
    obj = {}
    for k, v in prototype.items():
        value = data.get(k, v)  # prototype value is None means required filed.
        if isinstance(v, _REQUIRED):
            raise SyntaxError('Register missing filed on section %s %s.' % (name, k))
        obj[k] = value

    Section = namedtuple(name, obj.keys())
    return Section._make(obj.values())


class Register(object):

    def __init__(self, filename):
        self._filename = filename
        self._local = None
        self._devices = None
        self._sandbox = None
        self._data = {}

        with open(filename) as f:
            self._data = yaml.safe_load(f)


    @property
    def local(self):
        """local machine information. [local-machine] section

        .username
        .password
        .hostname
        .mount

        :return:
        """
        if not self._local:
            default = {
                'username': None,
                'password': None,
                'hostname': None,
                'mount': 'cifs' if PLATFORM == Platform.WINDOWS else 'nfs'
            }
            self._local = _section('local', default, self._data.get('local-machine'))
        return  self._local


    @property
    def devices(self):
        if self._devices is None:
            self._devices = {}
            for name, device in self._data.get('device', {}).items():
                prototype = {
                    'hostname': _REQUIRED,
                    'ssh': None,
                    'system': None
                }
                ssh = None
                system = None

                for k, v in device.items():
                    if k == 'ssh':
                        default = {
                        'username': None,
                        'password': None,
                        'port': 22,
                        }
                        ssh = _section('device_ssh', default, v)
                    if k == 'system':
                        default = {
                        'os': None,
                        'arch': None,
                        'crt': None,
                        }
                        system = _section('device_system', default, v)

                self._devices[name] = _section('device', prototype,
                                               {'ssh': ssh, 'system': system,
                                                'hostname': device.get('hostname')})
        return self._devices

    @property
    def sandbox(self):
        if self._sandbox is None:
            prototype = {
                'devices': [],
            }
            return _section('sandbox', property, self._data.get('sandbox'))
        return self._sandbox
