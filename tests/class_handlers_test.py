import pytest

from flash.exceptions import HTTPError
from flash.util.tests import url


def test_class_based_handler_get(app, client):
    response_text = "this is a get request"

    @app.route("/book")
    class BookResource:
        def get(self, req, resp):
            resp.text = response_text

    assert client.get(url("/book")).text == response_text


def test_class_based_handler_post(app, client):
    response_text = "this is a post request"

    @app.route("/book")
    class BookResource:
        def post(self, req, resp):
            resp.text = response_text

    assert client.post(url("/book")).text == response_text


def test_class_based_handler_not_allowed_method(app, client):
    @app.route("/book")
    class BookResource:
        def post(self, req, resp):
            resp.text = "yolo"
    print(client.post(url("/book")).text)
    assert client.post(url("/book")).text == "yolo"


def test_cb_handlers_ignore_route_methods(app, client):
    response_text = "this is a get request"

    @app.route("/book", methods=["post"])
    class BookResource:
        def get(self, req, resp):
            resp.text = response_text

    assert client.get(url("/book")).text == response_text