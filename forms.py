from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddAlbumForm(FlaskForm):
    album_name = StringField("Album title", validators=[DataRequired()])
    author_name = StringField("Author")
    genre = StringField("Genre")
    release_year = IntegerField("Release year", validators=[DataRequired()])
    button = SubmitField('Dodaj')


class UpdateAlbumForm(FlaskForm):
    album_name = StringField("Album title", validators=[DataRequired()])
    author_name = StringField("Author")
    genre = StringField("Genre")
    release_year = IntegerField("Release year", validators=[DataRequired()])
    button = SubmitField('Zaktualizuj')
