# -*- encoding: utf-8 -*

from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

urlpatterns = patterns(
    'project.contact.views',
    url(r'^contact/$', 'contact', name='contact'),
)
