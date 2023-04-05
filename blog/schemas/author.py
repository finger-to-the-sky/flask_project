from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class AuthorSchema(Schema):
    class Meta:
        type_ = 'author'
        self_url = 'author_detail'
        self_url_kwargs = {'id': "<id>"}
        self_url_many = 'author_list'

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False, required=True)
    text = fields.String(allow_none=False, required=True)
    created_at = fields.DateTime(allow_none=False)
    updated_at = fields.DateTime(allow_none=False)

    article = Relationship(
        nested='ArticleSchema',
        attribute='article',
        related_url='article_detail',
        related_url_kwargs={'id': "<id>"},
        schema='ArticleSchema',
        type='article',
        many=True
    )
    user = Relationship(
        nested='UserSchema',
        attribute='user',
        related_url='user_detail',
        related_url_kwargs={'id': "<id>"},
        schema='UserSchema',
        type='user',
        many=False
    )
