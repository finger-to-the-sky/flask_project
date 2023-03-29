from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager

migrate = Migrate()
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

__all__ = [
    "db",
]