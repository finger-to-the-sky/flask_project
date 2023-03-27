import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class CreateArticleForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    text = wtforms.TextAreaField("Text", [validators.DataRequired()])
    submit = SubmitField("Create")
