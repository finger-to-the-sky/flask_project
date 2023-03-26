# from flask import Blueprint, render_template
# from flask_login import login_required
# from werkzeug.exceptions import NotFound
# from .models import User
#
# article_blueprint = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')
#
#
# ARTICLES = {1: 'Ударила молния', 2: 'Спасли кота', 3: 'Инопланетяне'}
#
#
#
# @article_blueprint.route('/')
# def articles_list():
#     return render_template('articles/list.html', articles=ARTICLES)
#
#
# @article_blueprint.route('/<int:pk>')
# def get_article(pk: int):
#     try:
#         article_data = ARTICLES[pk]
#     except KeyError:
#         raise NotFound(f'User with id {pk} not found!')
#
#     return render_template('articles/profile.html', article_data=article_data)
