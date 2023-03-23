from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

migrate = Migrate()
db = SQLAlchemy()
csrf = CSRFProtect()

__all__ = [
    "db",
]