from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_update/$', views.sign_update, name='sign_update'),
    url(r'^playlist_update/$', views.playlist_update, name='playlist_update'),
    url(r'^listeners_count_update/$', views.listeners_count_update, name='listeners_count_update'),
]
