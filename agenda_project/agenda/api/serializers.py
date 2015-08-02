from rest_framework import serializers

from agenda.models import Address, Artist, BasicEntity, Event, Group

BASIC_ENTITY_FIELDS = tuple(BasicEntity.get_field_names()) + ('url',)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('street', 'number', 'extra', 'neighbourhood', 'city', 'code',
                  'province', 'country', 'geo_map', 'related_entity',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = BASIC_ENTITY_FIELDS + ('last_name',)


class EventSerializer(serializers.ModelSerializer):
    artists = serializers.HyperlinkedIdentityField(view_name='artists-list',
                                                   many=True, format='json')
    owner = serializers.ReadOnlyField(source='owner.username')
    venue = serializers.HyperlinkedIdentityField(view_name='venue-list',
                                                 format='json')

    class Meta:
        model = Event
        fields = BASIC_ENTITY_FIELDS + ('short_description', 'start_time',
        	'end_time', 'artists', 'owner', 'venue', 'tickets', 'status',)


class GroupSerializer(serializers.ModelSerializer):
    artists = serializers.HyperlinkedIdentityField(view_name='artists-list',
                                                   many=True, format='json')
    class Meta:
        model = Group
        fields = BASIC_ENTITY_FIELDS + ('artists',)


# class Artist(BasicEntity):
# class Event(BasicEntity):
# class Group(Artist):

# class Link(Model):
#    related_entity = ForeignKey(BasicEntity, related_name='links')
#    url = URLField(max_length=254)


# class Phone(Model):
# class Venue(BasicEntity):


