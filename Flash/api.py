import os
from whitenoise import WhiteNoise
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from requests import Session as RequestsSession
from .exceptions import HttpError
from .route import Route
from .responses import Response
from .util import empty_wsgi_app

class Flash:
    def __init__(self, template_dir="templates",static_dir="static",debug=True):
        self.static_dir = os.path.abspath(static_dir)
        self._static_root = "/static"
        self._debug = debug
        self._routes = {}
        self._exception_handler = None

        # Cached request session
        self._session = None

