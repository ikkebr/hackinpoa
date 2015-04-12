# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20150411_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name=b'Grupo P\xc3\xbablico?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Nome'),
            preserve_default=True,
        ),
    ]
