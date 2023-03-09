from flask import Blueprint

article = Blueprint('article', __name__, url_prefix='/article', static_folder='../static')


@article.route('/')
def user_list():
    return 'articles'
