from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {1: 'Ударила молния', 2: 'Спасли кота', 3: 'Инопланетяне'}


@article.route('/')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_data = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'User with id {pk} not found!')

    return render_template('articles/detail.html', article_data=article_data)
