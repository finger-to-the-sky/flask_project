from flask import render_template

from blog.app import create_app
from blog.models import Articles

app = create_app()


@app.route("/")
def main_page():
    articles = Articles.query.all()
    return render_template('articles/list.html', articles=articles)
