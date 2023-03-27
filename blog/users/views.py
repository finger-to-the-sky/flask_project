from flask import Blueprint, render_template
from flask_login import login_required
from blog.models import User


user_blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user_blueprint.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user_blueprint.route('/<int:pk>')
@login_required
def profile(pk: int):
    _user = User.query.filter_by(id=pk).one_or_none()
    return render_template('users/profile.html', user=_user)
