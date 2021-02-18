from flask import Flask
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


@app.route('/')
def display_list():
    return handlers.display_all_albums()


if __name__ == '__main__':
    app.run(debug=True)
