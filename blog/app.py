import os

from flask import Flask
from blog.user.views import user
from blog.article.views import article


# app = Flask(__name__)


# @app.get('/')
# def hello():
#     return 'Hello World'

def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
