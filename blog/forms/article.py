import wtforms
from flask_wtf import FlaskForm


class CreateArticleForm(FlaskForm):
    title = wtforms.StringField("Title", [wtforms.validators.DataRequired()])
    text = wtforms.TextAreaField("Text", [wtforms.validators.DataRequired()])
    tags = wtforms.SelectMultipleField('Tags', coerce=int)
    submit = wtforms.SubmitField("Create")
