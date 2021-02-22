from flask import jsonify, request, abort
from database import db


def add_album():
    if not request.json:
        abort(400)
    data = {
        'id': db.get_available_id(),
        'album_name': request.json.get('album_name', ''),
        'author_name': request.json.get('author_name', ''),
        'genre': request.json.get('genre', ''),
        'release_year': request.json.get('release_year', 0)
    }
    db.add_album(data)
    return jsonify({'album': data}), 201


def delete_album_by_id(album_id: int):
    if db.delete_by_id(album_id):
        return jsonify({'info': album_id})
    return jsonify({"error": f"Couldn't delete ID: {album_id} - doesn't exist"})


def delete_all():
    if db.delete_all():
        return jsonify({"info": 'library was cleared'})
    return jsonify({"error": "Library didn't existed"})


def set_db_file_name(file_name: str):
    db.change_db_name(file_name)


def get_album_by_id(album_id: int):
    return jsonify(db.get_by_id(album_id))


def get_all_albums():
    return jsonify(db.get_all())


def update_album_by_id(album_id: int):
    if not get_album_by_id(album_id) == {}:
        db.update_by_id(album_id, **request.json)
        return jsonify({"info": f"ID: {album_id} was updated"})
    return jsonify({"error": f"Can't update ID: {album_id} - does not exist"})
