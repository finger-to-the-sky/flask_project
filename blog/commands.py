import click
from werkzeug.security import generate_password_hash
from blog.database import db


@click.command('create-init-user')
def create_init_user():
    from blog.app import app
    from models import User
    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()


@click.command('create-init-tags')
def create_init_tags():
    from blog.app import app
    from models import Tag

    with app.app_context():
        tags = ('flask', 'django', 'python', 'sqlite')
        for tag in tags:
            db.session.add(Tag(name=tag))
        db.session.commit()
    click.echo(f'Created tags {", ".join(tags)}')
