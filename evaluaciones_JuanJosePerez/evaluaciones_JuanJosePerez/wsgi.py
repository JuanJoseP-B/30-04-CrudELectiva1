"""
WSGI config for evaluaciones_JuanJosePerez project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

# Fix para Vercel: el resolver de Vercel cachea 'evaluaciones_JuanJosePerez' como
# la carpeta EXTERIOR (sin settings.py). Necesitamos:
# 1. Agregar la carpeta del proyecto Django (donde esta manage.py) al inicio del path
# 2. Limpiar el modulo cacheado para que Python lo re-resuelva correctamente

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# CRITICO: Eliminar el modulo cacheado por el resolver de Vercel
if 'evaluaciones_JuanJosePerez' in sys.modules:
    del sys.modules['evaluaciones_JuanJosePerez']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones_JuanJosePerez.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application
