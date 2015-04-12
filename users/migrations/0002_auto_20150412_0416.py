# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(max_length=200, null=True, choices=[(b'crossover', b'Crossover'), (b'custom', b'Custom'), (b'naked', b'Naked'), (b'scooter', b'Scooter'), (b'sport', b'Sport'), (b'street', b'Street'), (b'touring', b'Touring'), (b'trail', b'Trail')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, max_length=10, choices=[(b'M', b'Masculino'), (b'F', b'Feminino'), (b'O', b'Outro')]),
            preserve_default=True,
        ),
    ]
