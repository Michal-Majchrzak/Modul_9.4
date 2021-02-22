from flask import render_template, redirect, url_for, request
from forms import AddAlbumForm, UpdateAlbumForm
from database import db

URLS_DICT = {
    'Wyświetl wszystkie': 'handle_list_display',
    'Dodaj pozycję': 'handle_add_album'
}


def error_message(errors: dict) -> str:
    message = ""
    for key, value in errors.items():
        message += f"{key} : {value}; "
    return message


def add_album(form_data):
    form = AddAlbumForm()
    if form.validate_on_submit():
        keys = ['album_name', 'author_name', 'genre', 'release_year']
        data = {'id': db.get_available_id()}
        for key in keys:
            data[key] = form_data.get(key)
            if key == 'release_year':
                try:
                    data[key] = int(form_data.get(key))
                except ValueError:
                    data[key] = 0
        db.add_album(data)
        return redirect(url_for('handle_list_display'))
    else:
        error = error_message(form.errors)
        return render_template('add-album.html', error=error, form=form, urls=URLS_DICT, db_stat=db.get_stats())


def add_album_display():
    form = AddAlbumForm()
    return render_template('add-album.html', form=form, urls=URLS_DICT, db_stat=db.get_stats())


def delete_album(album_id: int):
    if db.delete_by_id(album_id):
        return redirect(url_for('handle_list_display'))
    else:
        return redirect(url_for('handle_main_display', error=f"Can't delete ID: {album_id} - does not exists."))


def list_display():
    albums = db.get_all().values()
    return render_template('list.html', albums=albums, urls=URLS_DICT, db_stat=db.get_stats())


def main_display():
    error = request.args.get('error', '')
    if error:
        return render_template('index.html', error=error, urls=URLS_DICT, db_stat=db.get_stats())
    return render_template('index.html', error=None, urls=URLS_DICT, db_stat=db.get_stats())


def update_album(album_id: int, **form_data):
    form = UpdateAlbumForm()
    if form.validate_on_submit():
        if db.get_by_id(album_id) == {}:
            return redirect(url_for('handle_add_album'))
        data = form_data
        if 'release_year' in data.keys():
            r_year = data.get('release_year', 0)
            data['release_year'] = int(r_year)
        db.update_by_id(album_id, **data)
        return redirect(url_for('handle_list_display'))
    else:
        error = error_message(form.errors)
        return render_template('update-album.html', error=error, form=form, item_id=album_id, urls=URLS_DICT, db_stat=db.get_stats())


def update_album_display(album_id: int):
    if db.get_by_id(album_id) == {}:
        return redirect(url_for('handle_add_album'))
    else:
        form = UpdateAlbumForm(data=db.get_by_id(album_id))
        return render_template('update-album.html', form=form, item_id=album_id, urls=URLS_DICT, db_stat=db.get_stats())
