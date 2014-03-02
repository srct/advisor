from django.conf.urls import patterns, include, url
from compare.views import compare, analytics

urlpatterns = patterns('',
    url(r'^compare/$', compare, name = 'compare'),
    url(r'^analytics/$', analytics, name = 'analytics'),
)
