from flask import render_template
from forms import Album
from database import db


def display_all_albums():
    data = [album for album in db.get_all().values()]
    form = Album(data)
    error = form.errors

    return render_template('album-list.html', form=form, albums=data, error=error)
