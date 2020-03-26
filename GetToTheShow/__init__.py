import os

from flask import Flask, render_template, request, redirect, session, url_for


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def start():

        return render_template('/scenes/welcome.html')

    from . import scenes
    app.register_blueprint(scenes.bp)

    from . import deaths
    app.register_blueprint(deaths.bp)

    return app
