from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^shop/$', views.index, name='index')#SINCE APPEND SLASH IS SET TO TRUE BY DEFUALT (MEANING IT'S NOT IN THE settings.py) A SLASH WILL BE APPENDED IF NO SUITABLE URL IS FOUND
                                                 #AFTER FINDING A URL BROWSERS JUST KEEP ADDING THE SLASH, WELL AT LEAST EDGE DOESNT DO IT
]