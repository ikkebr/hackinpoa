# -*- coding: utf-8 -*-

from django.db import models


class WayPoint(models.Model):
    pass


class Route(models.Model):
    pass


class Trip(models.Model):

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"descrição")
    start_at = models.DateField(u"Data de inicio")
    end_at = models.DateField(u"Date Final")
    created_at = models.DateTimeField("Data de criação", auto_now=True)
    start_point = models.CharField(u"Endereço de inicio", max_length==255)
    end_point = models.CharField(u"Endereço final", max_length=255)
    distance = models.FloatField(u"Distância")
    duration = models.TimeField(u"Duração")
