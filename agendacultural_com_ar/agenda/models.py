# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import (Model, CharField, TextField, URLField, EmailField,
                              DateField, ForeignKey, DateTimeField, ImageField,
                              NullBooleanField, IntegerField, ManyToManyField)
from django.utils.translation import ugettext_lazy as _


class Address(Model):
    related_entity = ForeignKey('BasicEntity')
    street = CharField(_("street"), max_length=128)
    number = IntegerField(_("number"), blank=True, null=True)
    extra = CharField("extra", max_length=128, blank=True, null=True)
    neighbourhood = CharField(_("neighborhood"), max_length=128, blank=True,
                              null=True)
    city = CharField(_("city"), max_length=128)
    code = CharField(_("postal code"), max_length=128, blank=True, null=True)
    province = CharField(_("province"), max_length=128, blank=True, null=True)
    country = CharField(_("country"), max_length=128, blank=True, null=True)
    geo_map = CharField(_("map"), max_length=128, blank=True, null=True)
    
    def __unicode__(self):
        addres_str = self.street
        if self.number:
            addres_str += ' %i, '%self.number
        aux_fields = [self.extra, self.code, self.city, self.province]
        addres_str += u', '.join(filter(None, aux_fields))
        return addres_str


    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _("addresses")

class BasicEntity(Model):
    name = CharField(_("name"), max_length=128, db_index=True, error_messages=
                     {'blank':'Por favor ingrese un nombre o título.',
                      'null':'Por favor ingrese un nombre o título.',})
    description = TextField(_("description"), blank=True, db_index=True)
    email = EmailField(max_length=254, blank=True)
    created = DateField(_("creation date"), auto_now_add=True, editable=False)
    photo = ImageField(upload_to='/tmp/', max_length=256, null=True, blank=True)

    def get_absolute_url(self):
        entity_class_name = self.__class__.__name__.lower()
        url_name = entity_class_name+'_details'
        return reverse(url_name, args=[str(self.id)])

    
    def __unicode__(self):
        return self.name
    
    class Meta:
        get_latest_by = "created"
        ordering = ['-created', 'name']


class Artist(BasicEntity):
    last_name = CharField(_("last name"), max_length=128, null=True, blank=True)
    
    class Meta:
        verbose_name = _('artist')
        verbose_name_plural = _("artists")

class Event(BasicEntity):
    CREATED, CREATED_TEXT = ("cre", "created")
    PUBLISHED, PUBLISHED_TEXT =  ("pub", "published")
    CANCELED, CANCELED_TEXT =  ("can", "canceled")
    WEB_PUBLISHED, WEB_PUBLISHED_TEXT =  ("wpub", "published (web)")
    WEB_WATCHLIST, WEB_WATCHLIST_TEXT =  ("wwat", "watchlist (web)")

    STATUS_CHOICES = (
        (CREATED, _(CREATED_TEXT)),
        (PUBLISHED, _(PUBLISHED_TEXT)),
        (CANCELED, _(CANCELED_TEXT)),
        (WEB_PUBLISHED, _(WEB_PUBLISHED_TEXT)),
        (WEB_WATCHLIST, _(WEB_WATCHLIST_TEXT)),
        )

    short_description = TextField(_("short description"), null=True, blank=True)
    start_time = DateTimeField(_("start time"), db_index=True)
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

    def get_address(self):
        return self.address_set.get()