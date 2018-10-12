from django.conf.urls import include, url
from Api.views import *
from django.views.decorators.csrf import csrf_exempt
from Service.views import *

urlpatterns = [
    url(r"^CMDBApi/", csrf_exempt(CMDBApi.as_view())),
    url(r"^$",server),
    url(r"^(?P<page>\d+)", server),
    url(r"^ajax_server/$", AjaxServer),
    url(r"^ajax_server/(?P<page>\d+)/$", AjaxServer),
    url(r"^sj/$", ServerList_ajax),
    url(r"^getConnect/$",getConnect),
    url(r"^gateValid/$",gateValid)
]
