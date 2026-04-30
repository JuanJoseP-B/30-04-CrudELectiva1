# Guía de Despliegue: Render + Supabase

Para desplegar tu proyecto en Render y conectarlo a una base de datos PostgreSQL en Supabase, hemos preparado tu código con las dependencias necesarias (`psycopg2-binary`, `dj-database-url`, `gunicorn`, `whitenoise`) y hemos ajustado `settings.py`.

Sigue estos pasos para finalizar el proceso:

## 1. Preparar Supabase (Base de Datos)
1. Ve a [Supabase](https://supabase.com/) y crea un nuevo proyecto.
2. Una vez creado el proyecto, ve a **Project Settings** > **Database**.
3. Busca la sección **Connection string** y selecciona la pestaña **URI**.
4. Copia la cadena de conexión. Debería verse similar a esto: 
   `postgresql://postgres.[tu-id]:[tu-password]@aws-0-region.pooler.supabase.com:6543/postgres`
   *(Recuerda reemplazar `[tu-password]` con la contraseña real que le asignaste a tu base de datos).*

## 2. Preparar el Repositorio
Como hemos añadido nuevos archivos (`build.sh`, modificado `requirements.txt` y `settings.py`), primero debes subir estos cambios a GitHub:
```powershell
git add .
git commit -m "Configuración para despliegue en Render y Supabase"
git push origin main
```

## 3. Desplegar en Render
1. Ve a [Render](https://render.com/) y crea un nuevo **Web Service**.
2. Conecta tu cuenta de GitHub y selecciona el repositorio `30-04-CrudELectiva1`.
3. Completa la configuración del Web Service:
   * **Name**: `evaluaciones-juan-jose` (o el que prefieras).
   * **Environment**: `Python 3`.
   * **Build Command**: `./build.sh`
   * **Start Command**: `cd evaluaciones_JuanJosePerez && gunicorn evaluaciones_JuanJosePerez.wsgi:application`

4. Desplázate hacia abajo hasta la sección **Environment Variables** y añade las siguientes:
   * `PYTHON_VERSION`: `3.10.0` (o tu versión actual de Python).
   * `SECRET_KEY`: `escribe_aqui_una_cadena_larga_y_aleatoria`
   * `DATABASE_URL`: *(pega aquí la Connection string URI que copiaste de Supabase)*.

5. Haz clic en **Create Web Service**.

## ¿Qué pasará ahora?
Render detectará el push de GitHub, ejecutará el script `./build.sh` (que instala las dependencias, aplica las migraciones a Supabase y recolecta los archivos estáticos) y luego iniciará la aplicación con Gunicorn. 

Gracias a `dj-database-url` en tu `settings.py`, Django usará automáticamente la URL de Supabase en lugar de la base de datos local SQLite cuando detecte la variable `DATABASE_URL`.
