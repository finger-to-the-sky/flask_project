from flask import Flask
from blog.views import user_blueprint
from blog.views import article_blueprint
from blog.database import db


def register_blueprints(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(article_blueprint)


app = Flask(__name__)
app.config['SECRET_KEY'] = '#w^_krs-1me#bly9)sn_7u3f&7&grjdhn^vd2kiu1!2ay7pc$x'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
register_blueprints(app)





