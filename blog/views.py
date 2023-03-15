from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from .models import User

user_blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
article_blueprint = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

USERS = {1: 'Max', 2: 'George', 3: 'Richard'}
ARTICLES = {1: 'Ударила молния', 2: 'Спасли кота', 3: 'Инопланетяне'}


@user_blueprint.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user_blueprint.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'User with id {pk} not found!')

    return render_template('users/detail.html', user_name=user_name)


@article_blueprint.route('/')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article_blueprint.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_data = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'User with id {pk} not found!')

    return render_template('articles/detail.html', article_data=article_data)
