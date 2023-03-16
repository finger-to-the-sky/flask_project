from flask import Flask, redirect, url_for
from flask_login import LoginManager
from blog.views import user_blueprint
from blog.views import article_blueprint
from blog.database import db
from blog.auth import auth
from blog.models import User


def register_blueprints(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(article_blueprint)
    app.register_blueprint(auth, url_prefix="/auth")


app = Flask(__name__)
app.config['SECRET_KEY'] = '#w^_krs-1me#bly9)sn_7u3f&7&grjdhn^vd2kiu1!2ay7pc$x'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
register_blueprints(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))
