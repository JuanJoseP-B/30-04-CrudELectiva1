import os
import sys
from django.core.wsgi import get_wsgi_application

# Resolvemos las rutas de forma absoluta para Vercel
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Insertamos la ruta al PRINCIPIO para que tenga prioridad sobre /var/task
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# También añadimos la raíz del repositorio por si acaso
REPO_ROOT = os.path.dirname(BASE_DIR)
if REPO_ROOT not in sys.path:
    sys.path.append(REPO_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones_JuanJosePerez.evaluaciones_JuanJosePerez.settings')

try:
    application = get_wsgi_application()
    app = application
except Exception as e:
    print(f"Error al cargar la aplicación WSGI: {e}")
    raise e
