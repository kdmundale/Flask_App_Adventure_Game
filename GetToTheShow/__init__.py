from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello_world():
        return 'Welcome to my game!'

    return app
