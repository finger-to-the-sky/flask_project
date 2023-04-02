from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound
from blog.extensions import db
from blog.models import Articles, Author, Tag
from blog.forms.article import CreateArticleForm

article_blueprint = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article_blueprint.route('/', methods=['GET'])
def articles_list():
    articles = Articles.query.all()
    return render_template('articles/list.html', articles=articles)


@article_blueprint.route('/<int:article_id>')
def get_article(article_id: int):
    article: Articles = Articles.query.filter_by(
        id=article_id).options(
        joinedload(Articles.tags)).one_or_none()

    if article is None:
        raise NotFound

    return render_template('articles/detail.html', article=article)


@article_blueprint.route('/create/', methods=['GET'])
@login_required
def get_create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    return render_template('articles/create.html', form=form)


@article_blueprint.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        _article = Articles(title=form.title.data.strip(), text=form.text.data)

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.get_article', article_id=_article.id))

    return render_template('articles/create.html', form=form)


@article_blueprint.route('/tags', methods=['GET'])
def tags_list():
    tags = Tag.query.all()
    return render_template('articles/tags/list.html', tags=tags)


@article_blueprint.route('/filter_by_tag/<int:tag_id>', methods=['GET'])
def get_article_by_tag(tag_id):
    articles = Articles.query.filter(Articles.tags.any(id=tag_id)).all()
    if not articles:
        raise NotFound
    return render_template('articles/tags/get_articles.html', articles=articles)
