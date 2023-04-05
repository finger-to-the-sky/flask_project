from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models import Articles
from blog.schemas import ArticleSchema
from blog.extensions import db


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Articles,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Articles,
    }
