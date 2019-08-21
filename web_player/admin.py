from django.contrib import admin
from .models import Track, Playlist

# Register your models here.

admin.site.register(Playlist)
admin.site.register(Track)