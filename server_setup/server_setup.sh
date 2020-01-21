#!/bin/bash

DIRECTORY=$(cd `dirname $0` && pwd)
LIQ=$DIRECTORY/"radio.liq"
PLAYLIST_SERVER=$DIRECTORY/"playlist_server.py"

sudo apt-get install icecast2
sudo chown icecast2:icecast /etc/icecast2/icecast.xml
sudo systemctl enable icecast2
sudo systemctl start icecast2

sudo apt-get install liquidsoap -y
sudo cp $LIQ /etc/liquidsoap/radio.liq
cd /etc/liquidsoap
sudo chown -R liquidsoap:liquidsoap .
sudo systemctl enable liquidsoap
sudo systemctl start liquidsoap

sudo apt-get install python3
sudo apt-get install python-pip -y
pip install requests
pip install python-daemon
sudo cp $PLAYLIST_SERVER ~/server/playlist_server.py
~/server/playlist_server.py start
