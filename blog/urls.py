from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^ind', views.latest, name='latest'),
]
