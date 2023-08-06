

from epm.model.profile import Profile
from epm.model.scheme import Scheme
from epm.errors import EException


class Configuration(object):

    def __init__(self, fullname, worker):
        if fullname.endswith('@default'):
            fullname = fullname.replace('@default', '')
        self._fullname = fullname
        self._worker = worker
        self._profile = None
        self._scheme = None

    def _get_profile_name(self):
        if self._fullname:
            tokens = self._fullname.split('@')
            return tokens[0]
        return None

    def _get_scheme_name(self):
        if self._fullname:
            tokens = self._fullname.split('@')
            return 'default' if len(tokens) < 2 else tokens[1]
        return 'default'

    @property
    def profile(self):
        if self._profile is None:
            name = self._get_profile_name()
            if not name:
                raise EException('Can not load profile with the empty profile name: %s' % name)
            self._profile = Profile(name, self._worker)
        return self._profile

    @property
    def scheme(self):
        if self._scheme is None:
            name = self._get_scheme_name()
            self._scheme = Scheme(name, self._worker)
        return self._scheme

    @property
    def name(self):
        return self._fullname

