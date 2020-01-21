from django.shortcuts import render, render_to_response
from .icecast_api.icecast import Icecast
# Create your views here.


icecast = Icecast()


def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

def sign_update(request):
    artist, track = icecast.get_sign_HTTP()
    response_dict = {'artist': artist, 'track': track}
    return render(
        request,
        'sign.html',
        context=response_dict
    )

def playlist_update(request):
    playlist = icecast.get_playlist()
    response_dict = {'playlist': playlist}
    return render(
        request,
        'playlist.html',
        context=response_dict
    )

def listeners_count_update(request):
    result = icecast.get_listeners_count()
    response_dict = {'listeners_count': result}
    return render(
        request,
        'listeners_count.html',
        context=response_dict
    )
