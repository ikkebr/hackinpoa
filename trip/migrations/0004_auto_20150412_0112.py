# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_auto_20150412_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_at',
            field=models.DateField(null=True, verbose_name='Date Final', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_at',
            field=models.DateField(null=True, verbose_name='Data de inicio', blank=True),
            preserve_default=True,
        ),
    ]
