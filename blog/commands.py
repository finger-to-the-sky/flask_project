import click
from werkzeug.security import generate_password_hash
from app import app
from models import User
from blog.database import db


@click.command('create-init-user')
def create_init_user():
    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()
