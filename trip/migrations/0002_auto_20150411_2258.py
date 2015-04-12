# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Descri\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='track_type',
            field=models.CharField(default=b'group', max_length=20, verbose_name='Tipo do pavimento', choices=[(b'group', b'Terra'), (b'asphalt', b'Asfalto'), (b'pave', b'<Pavimento></Pavimento>')]),
            preserve_default=True,
        ),
    ]
