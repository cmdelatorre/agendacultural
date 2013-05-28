from django.conf.urls import patterns, url

urlpatterns = patterns('agenda.views',
    url(r'^$', 'index', name='index'),
    )