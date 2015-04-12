# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_auto_20150411_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='trip',
            field=models.ForeignKey(to='trip.Trip', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='track_type',
            field=models.CharField(default=b'group', max_length=20, verbose_name='Tipo do pavimento', choices=[(b'group', b'Terra'), (b'asphalt', b'Asfalto'), (b'pave', b'Pavimento')]),
            preserve_default=True,
        ),
    ]
