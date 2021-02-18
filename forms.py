from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class Album(FlaskForm):
    album_name = StringField('album_name', validators=[DataRequired()])
    author_name = StringField('author_name')
    genre = StringField('genre')
    release_year = IntegerField('release_year')
