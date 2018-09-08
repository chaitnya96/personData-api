from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^person/$', PersonView.as_view(), name='person'),
    url(r'^location/$', LocationView.as_view(), name='location'),

    ]
