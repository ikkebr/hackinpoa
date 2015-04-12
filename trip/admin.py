from django.contrib import admin

from .models import Trip, Route

class TripAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip, TripAdmin)

class RouteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Route, RouteAdmin)
