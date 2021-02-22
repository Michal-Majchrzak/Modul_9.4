from flask import Flask, request
import api
import handlers

app = Flask(__name__)
app.config['SECRET_KEY'] = "50M3K3Y"
api.set_db_file_name('example.json')


@app.route('/api/library/albums/', methods=['GET'])
def get_albums():
    return api.get_all_albums()


@app.route('/api/library/albums/', methods=['POST'])
def add_album():
    return api.add_album()


@app.route('/api/library/albums/', methods=['DELETE'])
def delete_albums():
    return api.delete_all()


@app.route('/api/library/albums/<int:album_id>', methods=['GET'])
def get_album(album_id):
    return api.get_album_by_id(album_id)


@app.route('/api/library/albums/<int:album_id>', methods=['PUT'])
def update_album(album_id):
    return api.update_album_by_id(album_id)


@app.route('/api/library/albums/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    return api.delete_album_by_id(album_id)


@app.route('/', methods=['GET'])
def handle_main_display():
    return handlers.main_display()


@app.route('/add-album/', methods=['GET', 'POST'])
def handle_add_album():
    if request.method == 'POST':
        return handlers.add_album(request.form)
    return handlers.add_album_display()


@app.route('/albums-list/', methods=['GET'])
def handle_list_display():
    return handlers.list_display()


@app.route('/delete/<int:album_id>', methods=['GET'])
def handle_delete_album(album_id):
    return handlers.delete_album(album_id)


@app.route('/update-album/<int:album_id>', methods=['GET', 'POST'])
def handle_update_album(album_id):
    if request.method == 'POST':
        return handlers.update_album(album_id, request.form)
    return handlers.update_album_display(album_id)


if __name__ == '__main__':
    app.run(debug=True)
