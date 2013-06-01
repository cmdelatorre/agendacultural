from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import RedirectView



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^agenda/', include('agenda.urls')),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/agenda/')),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        	{'document_root': settings.MEDIA_ROOT}),
        )