from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models import Articles
from blog.schemas import ArticleSchema
from blog.extensions import db


class ArticleListEvent(EventsResource):

    def event_get_count(self):
        return {'count': Articles.query.count()}


class ArticleDetailEvent(EventsResource):
    def event_get_count_by_author(self, **kwargs):
        return {'count': Articles.query.filter(Articles.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Articles,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Articles,
    }
