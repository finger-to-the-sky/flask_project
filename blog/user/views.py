from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {1: 'Max', 2: 'George', 3: 'Richard'}


@user.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'User with id {pk} not found!')

    return render_template('users/detail.html', user_name=user_name)
