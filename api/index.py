import os
import sys

# Punto de entrada para Vercel - resuelve el conflicto de nombres
# Añadimos la carpeta del proyecto Django (donde está manage.py) al inicio del path
DJANGO_PROJECT_DIR = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'evaluaciones_JuanJosePerez')
)

if DJANGO_PROJECT_DIR not in sys.path:
    sys.path.insert(0, DJANGO_PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones_JuanJosePerez.settings')

from django.core.wsgi import get_wsgi_application
app = application = get_wsgi_application()
