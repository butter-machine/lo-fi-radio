from .downloader import Downloader
from .parser import Parser

class IcecastInterface():
    @classmethod
    def getSign(self):
        Downloader.download()
        return Parser.parseSign()

    @classmethod
    def getListenersCount(self):
        Downloader.download()
        return Parser.parseListenersCount()
