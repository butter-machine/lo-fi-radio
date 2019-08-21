from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_update/$', views.sign_update, name='sign_update'),
]
