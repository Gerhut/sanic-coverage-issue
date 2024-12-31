def test_app():
    from sanic import Sanic

    app = Sanic(__name__)
    client = app.test_client
    _, response = client.get("/")
    assert response is not None
    assert response.status == 500
