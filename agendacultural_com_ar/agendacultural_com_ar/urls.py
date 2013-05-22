from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agendacultural_com_ar.views.home', name='home'),
    # url(r'^agendacultural_com_ar/', include('agendacultural_com_ar.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
