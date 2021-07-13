import inspect
from http import HTTPStatus
from parse import parse
from Flash.constants import ALL_HTTP_METHODS
from Flash.exceptions import HTTPError


class Route:
    def __init__(self, path_pattern, handler, methods=None):
        if methods is None:
            methods = ALL_HTTP_METHODS
        self.__path_pattern = path_pattern
        self.__handler = handler
        self.__methods = methods

    def match(self, request_path):
        result = parse(self.__path_pattern, request_path)
        if result is not None:
            return True, result.named
        return False, None

    def handle_request(self, request, response, **kwargs):
        if inspect.isclass(self.handler):
            handler = getattr(self.__handler(), request.method.lower(), None)
            if handler is None:
                raise HTTPError(status=HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            if request.method not in self.__methods:
                raise HTTPError(status=HTTPStatus.METHOD_NOT_ALLOWED)
            handler = self.__handler
        handler(request, response, **kwargs)
