from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound
from blog.database import db
from blog.models import Articles, Author
from blog.forms.article import CreateArticleForm


article_blueprint = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article_blueprint.route('/', methods=['GET'])
def articles_list():
    articles = Articles.query.all()
    return render_template('articles/list.html', articles=articles)


@article_blueprint.route('/<int:article_id>')
def get_article(article_id: int):
    article = Articles.query.filter_by(id=article_id).one_or_none()

    if article is None:
        raise NotFound

    return render_template('articles/detail.html', article=article)


@article_blueprint.route('/create/', methods=['GET'])
@login_required
def get_create_article():
    form = CreateArticleForm(request.form)
    return render_template('articles/create.html', form=form)


@article_blueprint.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if form.validate_on_submit():
        _article = Articles(title=form.title.data.strip(), text=form.text.data)
        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.get_article', article_id=_article.id))

    return render_template('articles/create.html', form=form)
