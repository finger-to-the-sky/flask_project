from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models import User
from blog.schemas import UserSchema
from blog.extensions import db


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }
