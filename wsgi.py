from blog.app import app, db
from blog.models import User
from werkzeug.security import generate_password_hash


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command('create-users')
def create_users():
    db.session.add(
        User(email='somebodyuser1@gmail.com', password=generate_password_hash('something_password1'))
    )
    db.session.commit()
