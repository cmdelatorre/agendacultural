from rest_framework import viewsets

from agenda.models import Address
from agenda.api.serializers import AddressSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
