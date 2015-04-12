# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_auto_20150412_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='route',
            field=models.ForeignKey(to='trip.Route', null=True),
            preserve_default=True,
        ),
    ]
