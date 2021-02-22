from os import path
import json

DATA_DIR_PATH = path.join(path.dirname(path.abspath(__file__)), 'data')


class PseudoDataBase:
    def __init__(self):
        self.DB_NAME = 'default_db.json'
        self.DB_FILE_PATH = path.join(DATA_DIR_PATH, self.DB_NAME)

        self.albums = {}
        self.load_all()

    def add_album(self, data: dict):
        self.albums[data.get('id')] = data
        self.save_all()

    def change_db_name(self, name: str):
        self.DB_NAME = name
        self.DB_FILE_PATH = path.join(DATA_DIR_PATH, name)
        self.load_all()

    def delete_by_id(self, album_id: int) -> bool:
        if album_id in self.albums.keys():
            del self.albums[album_id]
            self.save_all()
            return True
        return False

    def delete_all(self) -> bool:
        try:
            del self.albums
            self.albums = {}
            self.save_all()
            return True
        except NameError:
            return False

    def get_all(self) -> dict:
        return self.albums

    def get_available_id(self) -> int:
        try:
            return sorted(self.albums.keys())[-1] + 1
        except IndexError:
            return 0

    def get_by_id(self, album_id: int) -> dict:
        if album_id in self.albums.keys():
            return self.albums[album_id]
        return {}

    def get_number_of_entries(self):
        return len(self.albums.keys())

    def get_stats(self) -> dict:
        return_dict = {
            'library_name': self.DB_NAME,
            'entries_count': self.get_number_of_entries()
        }
        return return_dict

    def load_all(self):
        try:
            with open(self.DB_FILE_PATH, 'r') as file:
                self.albums = {}
                temp_albums = json.load(file)
                for key in temp_albums:
                    key_int = int(key)
                    self.albums[key_int] = temp_albums[key]
                del temp_albums
        except FileNotFoundError:
            self.albums = {}
            self.save_all()

    def save_all(self):
        with open(self.DB_FILE_PATH, 'w') as file:
            json.dump(self.albums, file)

    def update_by_id(self, album_id: int, **kwargs):
        album = self.get_by_id(album_id)
        for arg in kwargs:
            if arg in album.keys():
                album[arg] = kwargs[arg]
        self.save_all()


db = PseudoDataBase()
