import urllib.request
from .settings import XSPF_PATH, XSPF_URL


class Downloader():
    @classmethod
    def download(self):
        urllib.request.urlretrieve(XSPF_URL, XSPF_PATH)