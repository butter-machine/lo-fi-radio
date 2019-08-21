from django.db import models
from django.conf import settings
import os
from lxml import etree
import re

# Create your models here.

class Playlist(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def save(self):
        #creates new playlist's .xspf file
        file_path = settings.PLAYLISTS_DIR + self.name + '.xspf'
        NSMAP = {'vlc': 'http://www.videolan.org/vlc/playlist/ns/0/'}
        playlist = etree.Element('playlist', xmlns='http://xspf.org/ns/0/', nsmap=NSMAP)
        playlist.set('version', '1')
        
        title = etree.SubElement(playlist, 'title')
        title.text = self.name
        tracklist = etree.SubElement(playlist, 'trackList')
        tree =  etree.ElementTree(playlist)
        tree.write(file_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        super(Playlist, self).save()

    def delete(self):
        file_path = settings.PLAYLISTS_DIR + self.name + '.xspf'
        os.remove(file_path)
        super(Playlist, self).delete()

    def __str__(self):
        return self.name

class Track(models.Model):
    source_file = models.FileField(upload_to=settings.AUDIO_DIR)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def save(self):
        #adds this track to playlist's .xspf file

        super(Playlist, self).save()

    def __str__(self):
        return re.split(r'.*\/', self.source_file.name)[1]
