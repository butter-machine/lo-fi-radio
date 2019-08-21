#!/bin/bash
vlc ../../../../web_player/static/web_player/playlists/$1.xspf --sout-keep --sout='#transcode{acodec=mp3,channels=2} :standard{mux=mp3,access=http,dst=localhost:8040}'