# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from groups.views import LoginRequiredMixin

from .models import Trip, Route
from .forms import TripForm


class CreateTrip(LoginRequiredMixin, CreateView):

    model = Trip
    template_name = "trip/create.html"
    form = TripForm


class CreateRoute(LoginRequiredMixin, CreateView):

    model = Route
    template_name = "trip/route.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(CreateRoute, self).get_context_data(*args,
            **kwargs)

        context_data["trip"] = self.trip

        return context_data

    def get(self, *args, **kwargs):
        self.trip = get_object_or_404(Trip, pk=kwargs["pk"])

        return super(CreateRoute, self).get(*args, **kwargs)
