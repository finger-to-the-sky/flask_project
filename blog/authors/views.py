from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import Author


author_blueprint = Blueprint('author', __name__, url_prefix='/authors', static_folder='../static')


@author_blueprint.route('/')
def author_list():
    authors = Author.query.all()
    return render_template('authors/list.html', authors=authors)


# @author_blueprint.route('/<int:pk>')
# @login_required
# def profile(pk: int):
#     _user = User.query.filter_by(id=pk).one_or_none()
#     return render_template('users/profile.html', user=_user)
