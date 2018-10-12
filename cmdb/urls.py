"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Users.views import *
from cmdb.views import *
from Api.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include("ckeditor_uploader.urls")),
    url(r'^index/', index,name='index'),
    url(r'^$', index),
    url(r'^echart/', echartExample),
    url(r'^user/', include("Users.urls")),
    url(r'^login/', login,name='login'),
    url(r'^api/',include("Api.urls")),
    url(r'^server/', include("Api.urls")),
    url(r'^vue/',vueExample),
    url(r'^gate/',gate),
]
