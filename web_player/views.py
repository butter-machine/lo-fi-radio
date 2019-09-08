from django.shortcuts import render, render_to_response
from .icecast_api.icecast_interface import IcecastInterface
# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

def sign_update(request):
    result = IcecastInterface.getSign()
    response_dict = {'artist': result[0], 'track': result[1]}
    return render(
        request,
        'sign.html',
        context=response_dict
    )

def listeners_count_update(request):
    result = IcecastInterface.getListenersCount()
    response_dict = {'listeners_count': result}
    return render(
        request,
        'listeners_count.html',
        context=response_dict
    )
