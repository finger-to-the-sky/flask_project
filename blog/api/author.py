from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models import Author
from blog.schemas import AuthorSchema
from blog.extensions import db


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
