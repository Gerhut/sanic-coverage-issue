import pytest
from sanic_testing.testing import SanicTestClient


@pytest.fixture
def client():
    from app import app

    app.config.TOUCHUP = False

    return app.test_client


def test_app(client: SanicTestClient):
    _, response = client.get('/')

    assert response is not None
    assert response.status == 200
    assert response.text == 'Hello, World!'
