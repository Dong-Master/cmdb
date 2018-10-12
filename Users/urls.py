#coding:utf-8
#@mail:879995812@qq.com

from django.conf.urls import include, url
from Users.views import *

urlpatterns = [
    url(r'^register/',register),
]