from xml.dom import minidom
from .settings import XSPF_PATH 

class Parser():
    def __parse(self):
        self.xmldoc = minidom.parse(XSPF_PATH)
        
    @classmethod
    def parseSign(self):
        self.__parse(self)
        sign = self.xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue
        author, title = sign.split(' - ')
        return [author, title]

    @classmethod
    def parseListenersCount(self):
        LISTENERS_COUNT_STRING = 'Current Listeners: '
        self.__parse(self)
        annotation = self.xmldoc.getElementsByTagName('annotation')[0].firstChild.nodeValue
        listeners_count_index = annotation.find(LISTENERS_COUNT_STRING)
        listeners_count = annotation[listeners_count_index + len(LISTENERS_COUNT_STRING)]
        return listeners_count