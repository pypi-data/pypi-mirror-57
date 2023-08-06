# -*- coding: utf-8 -*-
from django.conf import settings

DEFAULT_SETTINGS = {
    'API_KEY': None,
    'SECRET': None,
    'BWIDTH': '',
    'BHEIGHT': '',
    'SIZE': '',
    'WIDTH': '',
    'HEIGHT': '',
    'DELAY': '',
    'COUNTRY': '',
    'TIMESTAMP': '',
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'THUMBALIZR_SETTINGS'))

globals().update(USER_SETTINGS)