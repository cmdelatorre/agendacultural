# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('street', models.CharField(verbose_name='street', max_length=128)),
                ('number', models.IntegerField(verbose_name='number', blank=True, null=True)),
                ('extra', models.CharField(verbose_name='extra', max_length=128, blank=True, null=True)),
                ('neighbourhood', models.CharField(verbose_name='neighborhood', max_length=128, blank=True, null=True)),
                ('city', models.CharField(verbose_name='city', max_length=128)),
                ('code', models.CharField(verbose_name='postal code', max_length=128, blank=True, null=True)),
                ('province', models.CharField(verbose_name='province', max_length=128, blank=True, null=True)),
                ('country', models.CharField(verbose_name='country', max_length=128, blank=True, null=True)),
                ('geo_map', models.CharField(verbose_name='map', max_length=128, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='BasicEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=128, error_messages={'blank': 'Por favor ingrese un nombre o título.', 'null': 'Por favor ingrese un nombre o título.'}, db_index=True)),
                ('description', models.TextField(verbose_name='description', db_index=True, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('created', models.DateField(verbose_name='creation date', auto_now_add=True)),
                ('last_modified', models.DateField(verbose_name='last modified', auto_now=True)),
                ('photo', models.ImageField(max_length=256, upload_to='/tmp/', blank=True, null=True)),
            ],
            options={
                'get_latest_by': 'created',
                'ordering': ['-created', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=30)),
                ('phone_type', models.CharField(max_length=16, default='mobile', choices=[('landline', 'Fijo'), ('mobile', 'Celular')])),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('basicentity_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='agenda.BasicEntity', parent_link=True, serialize=False)),
                ('last_name', models.CharField(verbose_name='last name', max_length=128, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'artist',
                'verbose_name_plural': 'artists',
            },
            bases=('agenda.basicentity',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('basicentity_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='agenda.BasicEntity', parent_link=True, serialize=False)),
                ('short_description', models.TextField(verbose_name='short description', blank=True, null=True)),
                ('start_time', models.DateTimeField(verbose_name='start time', db_index=True)),
                ('end_time', models.DateTimeField(verbose_name='end', blank=True, null=True)),
                ('tickets', models.TextField(verbose_name='entrada', blank=True, null=True)),
                ('status', models.CharField(verbose_name='estado', max_length=16, default='cre', choices=[('cre', 'created'), ('pub', 'published'), ('can', 'canceled'), ('wpub', 'published (web)'), ('wwat', 'watchlist (web)')])),
                ('artists', models.ManyToManyField(to='agenda.Artist')),
                ('owner', models.ForeignKey(related_name='own_events', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('agenda.basicentity',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('basicentity_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='agenda.BasicEntity', parent_link=True, serialize=False)),
                ('artists', models.ManyToManyField(related_name='groups', to='agenda.Artist')),
            ],
            bases=('agenda.basicentity',),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('basicentity_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='agenda.BasicEntity', parent_link=True, serialize=False)),
                ('has_parking', models.NullBooleanField(verbose_name='tiene estacionamiento?', default=False)),
                ('can_eat', models.NullBooleanField(verbose_name='se puede comer?', default=False)),
                ('can_dance', models.NullBooleanField(verbose_name='se puede bailar?', default=False)),
                ('responsable', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            bases=('agenda.basicentity',),
        ),
        migrations.AddField(
            model_name='phone',
            name='related_entity',
            field=models.ForeignKey(to='agenda.BasicEntity'),
        ),
        migrations.AddField(
            model_name='link',
            name='related_entity',
            field=models.ForeignKey(related_name='links', to='agenda.BasicEntity'),
        ),
        migrations.AddField(
            model_name='address',
            name='related_entity',
            field=models.ForeignKey(to='agenda.BasicEntity'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='agenda.Venue'),
        ),
    ]
