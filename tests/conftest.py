import pytest

import flash


@pytest.fixture
def app():
    return flash.Flash(templates_dir="tests/templates", debug=True)


@pytest.fixture
def client(app):
    return app.session()