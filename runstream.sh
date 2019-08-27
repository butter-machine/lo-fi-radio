#!/bin/bash
cvlc /playlists/pl1.xspf --sout-keep --sout='#transcode{acodec=mp3,channels=2} :standard{mux=mp3,access=http,dst=:8040}'