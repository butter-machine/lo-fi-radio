#!/bin/bash

DIRECTORY=$(cd `dirname $0` && pwd)
LIQ=$DIRECTORY/"radio.liq"

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
