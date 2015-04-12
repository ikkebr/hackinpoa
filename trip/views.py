# -*- coding: utf-8 -*-

from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from groups.views import LoginRequiredMixin

from .models import Trip


class CreateTrip(LoginRequiredMixin, CreateView):

    model = Trip
    template_name = "trip/create.html"

class CreateTrip_(LoginRequiredMixin, CreateView):

    model = Trip
    template_name = "trip/_create.html"
