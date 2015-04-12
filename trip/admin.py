from django.contrib import admin

from .models import Trip, Route, WayPoint

class TripAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip, TripAdmin)

class RouteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Route, RouteAdmin)


class WaypointAdmin(admin.ModelAdmin):
    pass

admin.site.register(WayPoint, WaypointAdmin)