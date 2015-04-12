# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from groups.views import LoginRequiredMixin

from .models import Trip, Route
from .forms import TripForm, RouteForm, WayPointForm


class CreateTrip(LoginRequiredMixin, CreateView):

    model = Trip
    template_name = "trip/create.html"
    form = TripForm

    def post(self, request):
        form = self.form(data=request.POST)
        if form.is_valid():
            trip = form.save()

            return redirect("trip:create-route", trip.id)

        return render(request, self.template_name, self.get_context_data(**{
                'form': form
            }))


class CreateRoute(LoginRequiredMixin, CreateView):

    model = Route
    template_name = "trip/route.html"
    form = RouteForm

    def get_context_data(self, *args, **kwargs):
        context_data = super(CreateRoute, self).get_context_data(*args,
            **kwargs)

        context_data["trip"] = self.trip

        return context_data

    def get(self, *args, **kwargs):
        self.trip = get_object_or_404(Trip, pk=kwargs["pk"])

        return super(CreateRoute, self).get(*args, **kwargs)

    def post(self, request, **kawrgs):
        form = self.form(data=request.POST)

        if form.is_valid():
            route = form.save()
            data = {
                'id': route.id
            }

            return HttpResponse(json.dumps(data),
                content_type="application/json")


def create_waypoint(request):
    form = WayPointForm(data=request.POST)

    if form.is_valid():
        point = form.save()

        return HttpResponse(json.dumps({'id': point.id}), content_type="application/json")

    return HttpResponse("error", content_type="application/json")


class ShowRoute(LoginRequiredMixin, DetailView):

    model = Trip

    def get_object(self, **kwargs):
        return self.model.objects.select_related("owner",
            "group").prefetch_related("route_set", "route_set__waypoint_set").get(
            pk=self.kwargs["pk"])
