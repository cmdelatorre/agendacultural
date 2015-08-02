from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from agenda.api.resources import (UserViewSet, ArtistViewSet, EventViewSet,
								  GroupViewSet,)


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'addresses', UserViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'events', EventViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
