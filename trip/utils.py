# -*- coding: utf-8 -*-

def get_trip_image_path(instance, filename):
    return "%s/%s" % (instance.id, filename)
