from .settings import MOUNTPOINT_URL, M3U_URL

def api_urls(request):
    api_urls = {
        'stream': MOUNTPOINT_URL,
        'm3u': M3U_URL,
    }
    return api_urls