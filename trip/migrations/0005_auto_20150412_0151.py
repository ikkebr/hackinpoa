# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_auto_20150412_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='end_point',
            field=models.CharField(max_length=255, null=True, verbose_name='Endere\xe7o final'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trip',
            name='start_point',
            field=models.CharField(max_length=255, null=True, verbose_name='Endere\xe7o de inicio'),
            preserve_default=True,
        ),
    ]
