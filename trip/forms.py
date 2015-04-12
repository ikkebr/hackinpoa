# -*- coding: utf-8 -*-

from django import forms

from .models import Trip

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        widgets = {
            "owner": forms.TextInput()
        }
