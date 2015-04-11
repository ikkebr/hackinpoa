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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(blank=True, max_length=10, choices=[(b'Male', b'M'), (b'Female', b'F'), (b'Other', b'O')])),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2, choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maran\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernanbuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SE', b'Sergipe'), (b'SP', b'S\xc3\xa3o Paulo'), (b'TO', b'Tocantins')])),
                ('motorcycle', models.CharField(max_length=200, null=True, blank=True)),
                ('cc', models.PositiveIntegerField(null=True, blank=True)),
                ('year', models.PositiveIntegerField(null=True, blank=True)),
                ('category', models.CharField(max_length=200, null=True, choices=[(b'Street', b'street'), (b'Naked', b'naked'), (b'Custom', b'custom'), (b'Crossover', b'crossover'), (b'Sport', b'sport'), (b'Touring', b'touring'), (b'Trail', b'trail'), (b'Scooter', b'scooter')])),
                ('manufactured', models.CharField(max_length=20, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
