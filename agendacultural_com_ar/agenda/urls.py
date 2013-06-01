from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

urlpatterns = patterns('agenda.views',
    url(r'^$', 'index', name='home'),
    url(r'^events/$', 'events', name='events'),
    url(r'^event/(?P<event_pk>\d+)$', 'event_details', name='event_details'),

    #
    url(r'^venue/(?P<venue_pk>\d+)$', 'venue_details', name='venue_details'),
    )