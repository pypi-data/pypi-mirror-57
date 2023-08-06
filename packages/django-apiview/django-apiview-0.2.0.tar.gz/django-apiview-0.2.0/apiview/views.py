import time
import functools
import logging
from fastutils.funcutils import get_inject_params
from django.http import JsonResponse
from .utils import SimpleJsonEncoder
from .utils import get_request_data
from .pack import SimpleJsonResultPacker

logger = logging.getLogger(__name__)

simple_json_result_packer = SimpleJsonResultPacker()


def apiview(view):
    def wrapper(request, **kwargs):
        package = {}
        try:
            data = get_request_data(request, kwargs)
            params = get_inject_params(view, data)
            result = view(**params)
            package = simple_json_result_packer.pack_result(result)
        except Exception as error:
            logger.exception("Error on getting result in @apiview...")
            package = simple_json_result_packer.pack_error(error)
        return JsonResponse(package, encoder=SimpleJsonEncoder, json_dumps_params={"ensure_ascii": False, "allow_nan": True, "sort_keys": True})
    wrapper.csrf_exempt = True
    return functools.wraps(view)(wrapper)
