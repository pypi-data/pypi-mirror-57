from .utils import SimpleJsonEncoder

class AbstractResultPacker(object):
    
    def package_result(self, result):
        raise NotImplementedError()

    def package_error(self, error):
        raise NotImplementedError()

    def encode_package(self, package):
        raise NotImplementedError()


class SimpleJsonResultPacker(AbstractResultPacker):

    def pack_result(self, result):
        return {
            "success": True,
            "result": result,
        }

    def pack_error(self, error):
        return {
            "success": False,
            "error": error,
        }
