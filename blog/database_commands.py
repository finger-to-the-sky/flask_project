from blog.app import app, db


@app.cli.command('init-db')
def init_db():
    db.create_all()

