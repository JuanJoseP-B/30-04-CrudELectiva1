# Guía de Diseño y UI Frontend V3 - Sistema de Calificaciones

## Concepto Estético
**Premium Minimalista**: Blanco puro (#FFFFFF) y Rojo Institucional (#D32F2F).

## Fases de Implementación

### Fase 1: Identidad Visual y Branding
* Tipografía: **Anthropic Serif** (Headers) e Inter (Body).
* Paleta de colores global en variables CSS.

### Fase 2: Estructura y Navegación
* Navbar dinámica que resalta la sección activa en rojo.
* Contenedores con espaciado balanceado.

### Fase 3: Componentes Interactivos y Formularios
* Bordes finos que cambian a rojo en `:focus`.
* Tablas con hover effect y promedios destacados.

### Fase 4: UX de Datos y Pulido Final
* Tarjetas de estadísticas con sombras suaves.
* Animaciones de transición sutiles.

### Fase 5: Interfaces de Seguridad
* **Rama**: `feature/ui-security-recovery`
* Plantillas de recuperación: `recover_username.html` y `password_reset_form.html`.
* Mensajes de alerta (Success/Error) con diseño limpio.
* Botones con bordes sutilmente redondeados y hover states refinados.
