import os
import urllib.parse

BASE_URL = 'http://52.36.229.29:8000'
MOUNTPOINT_URL = urllib.parse.urljoin(BASE_URL, '/lo-fi-radio')
XSPF_URL = MOUNTPOINT_URL + '.xspf'
M3U_URL = MOUNTPOINT_URL + '.m3u'

XSPF_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.xspf')
