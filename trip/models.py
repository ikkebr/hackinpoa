# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from groups.models import Group
from trip.utils import get_trip_image_path


DIFFICULT = (
    ("easy", u"Fácil"),
    ("medium", u"Médio"),
    ("hard", u"Difícil")
)


class Trip(models.Model):
    owner = models.ForeignKey(User, verbose_name=u"Dono")
    group = models.ForeignKey(Group, verbose_name=U"Grupo")

    name = models.CharField(u"name", max_length=255)
    description = models.TextField(u"descrição")
    start_at = models.DateField(u"Data de inicio")
    end_at = models.DateField(u"Date Final")
    created_at = models.DateTimeField("Data de criação", auto_now=True)
    is_public = models.BooleanField(u"É público", default=True)



class Route(models.Model):
    start_point = models.CharField(u"Endereço de inicio", max_length==255)
    end_point = models.CharField(u"Endereço final", max_length=255)
    distance = models.FloatField(u"Distância")
    duration = models.TimeField(u"Duração")
    difficult = models.CharField(u"Dificuldade", choices=DIFFICULT,
        default=DIFFICULT[0][0])
    track_type = models.CharField(u"Tipo do pavimento", choices=TRACK_TYPE,
        default=TRACK_TYPE[0][0])


class WayPoint(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(u"Endereço", null=True, blank=True)


class Image(models.Model):
    trip = models.ForeignKey(Trip, verbose_name=u"Viagem")
    image = models.ImageField(upload_to=get_trip_image_path)
