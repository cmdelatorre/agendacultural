# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db.models import (Model, CharField, TextField, URLField, EmailField,
                              DateField, ForeignKey, DateTimeField, ImageField,
                              NullBooleanField, IntegerField, ManyToManyField)


class Address(Model):
    related_entity = ForeignKey('BasicEntity')
    street = CharField("calle", max_length=128)
    number = IntegerField("número", blank=True, null=True)
    extra = CharField("extra", max_length=128, blank=True, null=True)
    neighbourhood = CharField("barrio/zona", max_length=128, blank=True,
                              null=True)
    city = CharField("ciudad", max_length=128)
    code = CharField("código postal", max_length=128, blank=True, null=True)
    province = CharField("provincia", max_length=128, blank=True, null=True)
    country = CharField("país", max_length=128, blank=True, null=True)
    geo_map = CharField("mapa", max_length=128, blank=True, null=True)


class BasicEntity(Model):
    name = CharField("nombre", max_length=128, db_index=True, error_messages=
                     {'blank':'Por favor ingrese un nombre o título.',
                      'null':'Por favor ingrese un nombre o título.',})
    description = TextField("descripción", blank=True, db_index=True)
    email = EmailField(max_length=254, blank=True)
    created = DateField("fecha de creación", auto_now_add=True, editable=False)
    photo = ImageField(upload_to='/tmp/', max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Artist(BasicEntity):
    last_name = CharField("apellido", max_length=128, null=True, blank=True)


class Event(BasicEntity):
    CREATED = "created"
    PUBLISHED =  "published"
    CANCELED =  "canceled"

    STATUS_CHOICES = (
        (CREATED, "Creado"),
        (PUBLISHED, "Publicado"),
        (CANCELED, "Cancelado"),
        )

    short_description = TextField("descripción corta", null=True, blank=True)
    start_time = DateTimeField("inicio", db_index=True)
    end_time = DateTimeField("fin", null=True, blank=True)
    # duration se calcula
    artists = ManyToManyField(Artist, null=True, blank=True)
    responsable = ForeignKey(User, null=True, blank=True,
                             related_name='own_events')
    venue =  ForeignKey('Venue')
    tickets = TextField("entrada", null=True, blank=True)
    #tags
    status = CharField("estado", max_length=16, choices=STATUS_CHOICES,
                       default=CREATED)
    #public = ManyToManyField(User, blank=True, related_name='events_participation')


class Group(Artist):
    integrants = ManyToManyField(Artist, null=True, blank=True,
                                 related_name='groups')


class Link(Model):
   related_entity = ForeignKey(BasicEntity, related_name='links')
   url = URLField(max_length=254)


class Phone(Model):
    LANDLINE = 'landline'
    MOBILE = 'mobile'
    PHONE_TYPE_CHOICES = (
        (LANDLINE, 'Fijo'),
        (MOBILE, 'Celular'),
    )

    related_entity = ForeignKey(BasicEntity)
    number = CharField(max_length=30)
    phone_type = CharField(
        max_length=16,
        choices=PHONE_TYPE_CHOICES, 
        default=MOBILE,
    )

    def __unicode__(self):
        return self.number    


class Venue(BasicEntity):
    responsable = ForeignKey(User, null=True, blank=True)
    has_parking = NullBooleanField("tiene estacionamiento?", default=False,
                               blank=True)
    can_eat = NullBooleanField("se puede comer?", default=False, blank=True)
    can_dance = NullBooleanField("se puede bailar?", default=False, blank=True)