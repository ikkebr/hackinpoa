# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150412_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Categoria', choices=[(b'crossover', b'Crossover'), (b'custom', b'Custom'), (b'naked', b'Naked'), (b'scooter', b'Scooter'), (b'sport', b'Sport'), (b'street', b'Street'), (b'touring', b'Touring'), (b'trail', b'Trail')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cc',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Cilindrada', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=100, verbose_name=b'Cidade'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='manufactured',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Fabricante', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='motorcycle',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Modelo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, max_length=10, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino'), (b'O', b'Outro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(max_length=2, verbose_name=b'Estado', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maran\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernanbuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SE', b'Sergipe'), (b'SP', b'S\xc3\xa3o Paulo'), (b'TO', b'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Ano', blank=True),
            preserve_default=True,
        ),
    ]
