from .downloader import Downloader
from .metadata import Parser, HTTPResponse

class Icecast():
    def __init__(self):
        self._downloader = Downloader()
        self._parser = Parser()
        self._http_response = HTTPResponse()
    
    def getSignHTTP(self):
        return self._http_response.getSign()
    
    def getSignXSPF(self):
        self._downloader.download()
        return self._parser.getSign()

    def getListenersCount(self):
        self._downloader.download()
        return self._parser.getListenersCount()
