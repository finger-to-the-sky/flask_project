from flask_admin import Admin
from flask_combo_jsonapi import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from blog.admin.views import CustomAdminIndexView

migrate = Migrate()
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)
api = Api()
