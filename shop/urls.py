from django.urls import path, re_path
from . import views
from .apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^store/$', views.store, name='store'),#SINCE APPEND SLASH IS SET TO TRUE BY DEFUALT (MEANING IT'S NOT IN THE settings.py) A SLASH WILL BE APPENDED IF NO SUITABLE URL IS FOUND
    #AFTER FINDING A URL BROWSERS JUST KEEP ADDING THE SLASH, WELL AT LEAST EDGE DOESNT DO IT
    re_path(r'^cart/add/$', views.cart_add_detail),
    re_path(r'^cart/detail/delete/$', views.cart_delete_detail),
    re_path(r'^cart/get/$', views.cart_get_cart),
    re_path(r'^cart/detail/update/$', views.cart_update_detail),
    re_path(r'^cart/update/$', views.cart_update_cart),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    
    #path('login/<str:username>-<str:password>', views.login, name='login')
    #re_path(r'login/(?P<username>[\w]+)-(?P<password>[\d]+)', views.login, name='login')#IT SEEM WE CAN'T USE CONVERTERS ON re_path
    
]