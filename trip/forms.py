# -*- coding: utf-8 -*-

from django import forms

from .models import Trip, Route, WayPoint

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        widgets = {
            "owner": forms.TextInput()
        }


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        exclude = ["difficult", "track_type"]


class WayPointForm(forms.ModelForm):

    class Meta:
        model = WayPoint
