from sanic import Sanic, text, Request

app = Sanic(__name__)

@app.get('/')
def index(_):
    return text('Hello, World!')

__all__ = ['app']
