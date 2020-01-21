import requests
from .settings import PLAYLIST_SERVER_URL


class Playlist:
    def get_playlist(self):
        response = requests.get(PLAYLIST_SERVER_URL)
        return response.content