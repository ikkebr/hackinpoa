# -*- coding: utf-8 -*-

from django.conf import settings

def get_services_tokens(request):

    tokens = {
        "google_maps_embed_token": settings.GOOGLE_MAPS_EMBED_TOKEN
    }

    return tokens
