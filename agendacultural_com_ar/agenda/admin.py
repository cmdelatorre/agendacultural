# -*- coding: utf-8 -*-

from django.contrib import admin
from agenda.models import (Address, Artist, Event, Group, Link, Phone, Venue)

admin.site.register(Address)
admin.site.register(Artist)
admin.site.register(Group)
admin.site.register(Phone)



class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description','start_time','venue', 'status')
    list_filter = ['venue', 'start_time', 'status']
    search_fields = ['name', 'short_description', 'description']
    date_hierarchy = 'start_time'
    fieldsets = [
        (None, {'fields': ['name', 'short_description', 'description']}),
        ('¿Dónde y cuándo?', {'fields': ['venue', 'start_time', 'end_time']}),
        ('Más información', 
         {'fields': ['photo', 'tickets', 'email', 'artists', 'responsable'],
          'classes': ['collapse', 'extrapretty'],
          'description': 'Información complementaria sobre el evento.'}),
        ('Admin', {'fields': ['status']}),
    ]
    inlines = [LinkInline]

admin.site.register(Event, EventAdmin)


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'has_parking', 'can_eat',
                    'can_dance')
    list_filter = ['has_parking', 'can_eat', 'can_dance']
    search_fields = ['name', 'description']
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Más información', 
         {'fields': ['photo', 'email', 'responsable', 'has_parking', 'can_eat', 'can_dance'],
          'classes': ['collapse'],
          'description': 'Información complementaria sobre el lugar.'}),
    ]
    inlines = [LinkInline, PhoneInline, AddressInline]

admin.site.register(Venue, VenueAdmin)

