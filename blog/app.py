from flask import Flask, redirect, url_for
from blog.users.views import user_blueprint
from blog.articles.views import article_blueprint
from blog.authors.views import author_blueprint
from blog.extensions import db, migrate, csrf, login_manager, admin
from blog.auth import auth
from blog.models import User
from blog import commands


def create_app():
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login'))


def register_blueprints(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(article_blueprint)
    app.register_blueprint(author_blueprint)
    app.register_blueprint(auth, url_prefix="/auth")
    from blog import admin

    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_tags)
