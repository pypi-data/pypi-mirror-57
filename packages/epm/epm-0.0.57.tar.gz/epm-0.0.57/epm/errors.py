"""
    Exceptions raised and handled in Conan server.
    These exceptions are mapped between server (as an HTTP response) and client
    through the REST API. When an error happens in server its translated to an HTTP
    error code that its sent to client. Client reads the server code and raise the
    matching exception.

    see return_plugin.py

"""

from subprocess import CalledProcessError


#from epm.utils.files import decode_text
#
#
#class CalledProcessErrorWithStderr(CalledProcessError):
#    def __str__(self):
#        ret = super(CalledProcessErrorWithStderr, self).__str__()
#        if self.output:
#            ret += "\n" + decode_text(self.output)
#        return ret

def decode_text(text):
    import codecs
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
    decoders = ["utf-8", "Windows-1252"]
    for decoder in decoders:
        try:
            return text.decode(decoder)
        except UnicodeDecodeError:
            continue
    return text.decode("utf-8", "ignore")  # Ignore not compatible characters


def exception_message_safe(exc):
    try:
        return str(exc)
    except Exception:
        return decode_text(repr(exc))

class EException(Exception):
    """
         Generic EPM exception
    """
    def __init__(self, *args, **kwargs):
        super(EException, self).__init__(*args, **kwargs)


    def __str__(self):
        from conans.util.files import exception_message_safe
        msg = super(EException, self).__str__()

        return exception_message_safe(msg)

class EProgramNotExists(EException):
    pass


class InvalidNameException(EException):
    pass


class ConanConnectionError(EException):
    pass


class ConanOutdatedClient(EException):
    pass


class EExceptionInUserConanfileMethod(EException):
    pass


class EInvalidConfiguration(EExceptionInUserConanfileMethod):
    pass


class EMigrationError(EException):
    pass


# Remote exceptions #
class InternalErrorException(EException):
    """
         Generic 500 error
    """
    pass


class RequestErrorException(EException):
    """
         Generic 400 error
    """
    pass


class AuthenticationException(EException):  # 401
    """
        401 error
    """
    pass


class ForbiddenException(EException):  # 403
    """
        403 error
    """
    pass


class NotFoundException(EException):  # 404
    """
        404 error
    """

    def __init__(self, *args, **kwargs):
        self.remote = kwargs.pop("remote", None)
        super(NotFoundException, self).__init__(*args, **kwargs)


class RecipeNotFoundException(NotFoundException):

    def __init__(self, ref, remote=None, print_rev=False):
        from conans.model.ref import ConanFileReference
        assert isinstance(ref, ConanFileReference), "RecipeNotFoundException requires a " \
                                                    "ConanFileReference"
        self.ref = ref
        self.print_rev = print_rev
        super(RecipeNotFoundException, self).__init__(remote=remote)

    def __str__(self):
        tmp = self.ref.full_str() if self.print_rev else str(self.ref)
        return "Recipe not found: '{}'".format(tmp, self.remote_message())


class PackageNotFoundException(NotFoundException):

    def __init__(self, pref, remote=None, print_rev=False):
        from conans.model.ref import PackageReference
        assert isinstance(pref, PackageReference), "PackageNotFoundException requires a " \
                                                   "PackageReference"
        self.pref = pref
        self.print_rev = print_rev

        super(PackageNotFoundException, self).__init__(remote=remote)

    def __str__(self):
        tmp = self.pref.full_str() if self.print_rev else str(self.pref)
        return "Binary package not found: '{}'{}".format(tmp, self.remote_message())


class UserInterfaceErrorException(RequestErrorException):
    """
        420 error
    """
    pass


EXCEPTION_CODE_MAPPING = {InternalErrorException: 500,
                          RequestErrorException: 400,
                          AuthenticationException: 401,
                          ForbiddenException: 403,
                          NotFoundException: 404,
                          RecipeNotFoundException: 404,
                          PackageNotFoundException: 404,
                          UserInterfaceErrorException: 420}
