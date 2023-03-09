from flask import Blueprint, render_template

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = ['Ударила молния', 'Спасли кота', 'Инопланетяне']
@article.route('/')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)
