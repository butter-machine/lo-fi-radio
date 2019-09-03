from django.shortcuts import render, render_to_response
from .static.web_player.scripts.python import parse_xspf as parser
# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

def sign_update(request):
    result = parser.parse()
    response_dict = {'artist': result[0], 'track': result[1]}
    return render(
        request,
        'sign.html',
        context=response_dict
    )
