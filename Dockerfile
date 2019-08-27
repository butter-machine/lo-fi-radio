FROM debian

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		#curl \
        #apt-utils \
        #python3 \
        #python3-pip \
		ca-certificates \
		libgl1-mesa-dri \
		libgl1-mesa-glx \
		pulseaudio \
		alsa-utils \
		dbus* \
		vlc && \
	apt-get -y -f install && \
	useradd -m vlc && \
	usermod -a -G audio,video vlc && \
	rm -rf /var/lib/apt/lists/*

#COPY requirements.txt ./
#RUN pip3 install --no-cache-dir -r requirements.txt
#CMD gunicorn lo_fi_radio.wsgi:application --bind 0.0.0.0:$PORT

COPY runstream.sh ./
COPY web_player/static/web_player/audio ./audio
COPY web_player/static/web_player/playlists ./playlists

USER vlc
WORKDIR /home/vlc/media
EXPOSE 8040
ENTRYPOINT ["/runstream.sh"]