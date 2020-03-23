from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Welcome to my game!'

    from . import auth
    hello.register_blueprint(hello.bp)

    return app
