from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

ARTIST_TITLE_FILE = '/home/pavel/.local/share/vlc/np_artist_title.txt'

def sign_update(request):
    artist_title_file_content = open(ARTIST_TITLE_FILE, 'r').read()
    artist_content = artist_title_file_content.split('-')[0]
    track_content = artist_title_file_content.split('-')[1]
    track_content = track_content.replace('.mp3', '')
    response_dict = {'artist': artist_content, 'track': track_content}
    return render(
        request,
        'sign.html',
        context=response_dict
    )
