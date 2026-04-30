# Guía Técnica de Implementación Backend V3 - Sistema de Calificaciones

## Arquitectura y Estructura Modular
El proyecto sigue un enfoque modular profesional, separando lógica de modelos, formularios y vistas.

## Fases de Implementación

### Fase 1: Entorno y Arquitectura Base
* Configuración de Django 6.0 y entorno virtual.
* Registro de la aplicación `calificaciones_JuanJosePerez`.

### Fase 2: Modelado de Datos y Lógica Interna
* Entidad `Calificacion` con validadores de rango (0.0 - 5.0).
* Intercepción del guardado para cálculo automático de promedio.

### Fase 3: Lógica de Negocio y Operaciones CRUD
* Implementación de CRUD protegido por autenticación.
* Formularios con validación en el cliente y servidor.

### Fase 4: Agregación de Datos Institucionales
* Uso de `Avg` para estadísticas globales dinámicas.

### Fase 5: Autenticación y Recuperación
* **Rama**: `feature/backend-auth-recovery`
* **Password Reset**: Implementación de `PasswordResetView` con tokens seguros.
* **Username Recovery**: Vista personalizada `recover_username` que valida identidad vía email.
* **Modularidad**: Lógica desacoplada en `forms.py` y `views.py`.

## Configuración de Rutas (URLs)
* `accounts/password-reset/`: Formulario inicial.
* `accounts/recover-username/`: Recuperación de usuario.
