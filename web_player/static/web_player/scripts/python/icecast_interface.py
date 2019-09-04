import os
import urllib.request
from django.conf import settings
from xml.dom import minidom


class IcecastInterface():
    URL = 'http://52.36.229.29:8000/main.ogg.xspf'
    FILE_PATH = os.path.join(settings.BASE_DIR, 'static/data.xspf')

    def __parse(self):
        urllib.request.urlretrieve(self.URL, self.FILE_PATH)
        xmldoc = minidom.parse(self.FILE_PATH)
        return xmldoc
        
    @classmethod
    def getSign(self):
        xmldoc = self.__parse(self)
        artist = xmldoc.getElementsByTagName('creator')[1].firstChild.nodeValue
        track = xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue
        return [artist, track]

    @classmethod
    def getListenersCount(self):
        LISTENERS_COUNT_STRING = 'Current Listeners: '
        xmldoc = self.__parse(self)
        annotation = xmldoc.getElementsByTagName('annotation')[0].firstChild.nodeValue
        listeners_count_index = annotation.find(LISTENERS_COUNT_STRING)
        listeners_count = annotation[listeners_count_index + len(LISTENERS_COUNT_STRING)]
        return listeners_count
