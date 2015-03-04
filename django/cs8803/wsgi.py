"""
WSGI config for cs8803 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# Run startup code!
import logging
logger = logging.getLogger(__name__)
logger.info('Startup code')
from django.conf import settings
from main.global_load import GlobalLoad
settings.GLOBAL_LOAD = GlobalLoad()


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cs8803.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
