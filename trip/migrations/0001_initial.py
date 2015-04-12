# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trip.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=trip.utils.get_trip_image_path)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_point', models.CharField(max_length=255, verbose_name='Endere\xe7o de inicio')),
                ('end_point', models.CharField(max_length=255, verbose_name='Endere\xe7o final')),
                ('distance', models.FloatField(verbose_name='Dist\xe2ncia')),
                ('duration', models.TimeField(verbose_name='Dura\xe7\xe3o')),
                ('difficult', models.CharField(default=b'easy', max_length=20, verbose_name='Dificuldade', choices=[(b'easy', 'F\xe1cil'), (b'medium', 'M\xe9dio'), (b'hard', 'Dif\xedcil')])),
                ('track_type', models.CharField(default=b'group', max_length=20, verbose_name='Tipo do pavimento', choices=[(b'group', b'Terra'), (b'asphalt', b'Asfalto'), (b'pave', b'Pavimento')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='descri\xe7\xe3o')),
                ('start_at', models.DateField(verbose_name='Data de inicio')),
                ('end_at', models.DateField(verbose_name='Date Final')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o')),
                ('is_public', models.BooleanField(default=True, verbose_name='\xc9 p\xfablico')),
                ('group', models.ForeignKey(verbose_name='Grupo', to='groups.Group')),
                ('owner', models.ForeignKey(verbose_name='Dono', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WayPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Endere\xe7o', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='trip',
            field=models.ForeignKey(verbose_name='Viagem', to='trip.Trip'),
            preserve_default=True,
        ),
    ]
