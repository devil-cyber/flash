from http import HTTPStatus


class HTTPError(Exception):
    def __init__(self, status: int):
        assert isinstance(status, int), "Status should be an integer"
        self.__http_status = HTTPStatus(status)

    @property
    def status(self):
        return self.__http_status.value

    @property
    def status_phrase(self):
        return self.__http_status.phrase

    def __str__(self):
        return f"{self.status} {self.status_phrase}"
