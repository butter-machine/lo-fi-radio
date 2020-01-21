from .downloader import Downloader
from .metadata import Parser, HTTPResponse
from .playlist import Playlist

class Icecast():
    def __init__(self):
        self._downloader = Downloader()
        self._parser = Parser()
        self._http_response = HTTPResponse()
        self._playlist = Playlist()
    
    def get_sign_HTTP(self):
        return self._http_response.get_sign()
    
    def get_sign_XSPF(self):
        self._downloader.download()
        return self._parser.get_sign()

    def get_listeners_count(self):
        self._downloader.download()
        return self._parser.get_listeners_count()

    def get_playlist(self):
        return self._playlist.get_playlist()
