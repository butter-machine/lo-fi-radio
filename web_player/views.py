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
    artist, track = icecast.getSignHTTP()
    response_dict = {'artist': artist, 'track': track}
    return render(
        request,
        'sign.html',
        context=response_dict
    )

def listeners_count_update(request):
    result = icecast.getListenersCount()
    response_dict = {'listeners_count': result}
    return render(
        request,
        'listeners_count.html',
        context=response_dict
    )
