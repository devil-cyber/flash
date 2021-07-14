import pytest

from flash.util.tests import url


def test_custom_error_handler(app, client):
    def on_exception(req, resp, exc):
        resp.text = "AttributeErrorHappened"

    app.add_exception_handler(on_exception)

    @app.route("/")
    def index(req, resp):
        raise AttributeError()

    response = client.get(url("/"))

    assert response.text == "AttributeErrorHappened"

