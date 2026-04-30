"""
WSGI config for evaluaciones_JuanJosePerez project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones_JuanJosePerez.settings')

application = get_wsgi_application()
