from __future__ import print_function
import re
import struct
import sys
import urllib.request as urllib2
from xml.dom import minidom
from .settings import XSPF_PATH, MOUNTPOINT_URL

class Parser:
    def __init__(self):
        self._LISTENERS_COUNT_STRING = 'Current Listeners: '

    def __parse(self):
        self.xmldoc = minidom.parse(XSPF_PATH)
        
    def getSign(self):
        self.__parse(self)
        sign = self.xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue
        return sign.split(' - ')

    def getListenersCount(self):
        self.__parse()
        annotation = self.xmldoc.getElementsByTagName('annotation')[0].firstChild.nodeValue
        listeners_count_index = annotation.find(self._LISTENERS_COUNT_STRING)
        listeners_count = annotation[listeners_count_index + len(self._LISTENERS_COUNT_STRING)]
        return listeners_count


class HTTPResponse:
    def __init__(self):
        self._ENCODING = 'latin1'

    def getSign(self):
        url = MOUNTPOINT_URL
        request = urllib2.Request(url, headers={'Icy-MetaData': 1})
        response = urllib2.urlopen(request)
        metaint = int(response.headers['icy-metaint'])

        for _ in range(10): # # title may be empty initially, try several times
            response.read(metaint)
            metadata_length = struct.unpack('B', response.read(1))[0] * 16
            metadata = response.read(metadata_length).rstrip(b'\0')
            m = re.search(br"StreamTitle='([^']*)';", metadata)
            if m:
                title = m.group(1)
                if title:
                    break

        return title.decode(self._ENCODING, errors='replace').split(' - ')




