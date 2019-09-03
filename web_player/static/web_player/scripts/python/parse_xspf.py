import os
import urllib.request
from django.conf import settings
from xml.dom import minidom

def parse():
    url = 'http://52.36.229.29:8000/main.ogg.xspf'
    file_path = os.path.join(settings.BASE_DIR, 'static/data.xspf')
    urllib.request.urlretrieve(url, file_path)
    
    xmldoc = minidom.parse(file_path)
    artist = xmldoc.getElementsByTagName('creator')[1].firstChild.nodeValue
    track = xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue

    return [artist, track]
