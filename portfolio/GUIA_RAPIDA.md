# 🚀 Guía Rápida - Portfolio Django

## ⚡ Inicio rápido

```bash
# 1. Activar entorno virtual
source ../venv/bin/activate

# 2. Aplicar migraciones (si no lo hizo aún)
python manage.py migrate

# 3. Crear usuario administrador
python manage.py createsuperuser

# 4. Ejecutar servidor
python manage.py runserver

# 5. Acceder
# Sitio: http://localhost:8000
# Admin: http://localhost:8000/admin
```

---

## 📝 Próximos pasos para completar el portfolio

### 1. Añadir tu perfil en el admin
```
1. Ve a http://localhost:8000/admin
2. Inicia sesión con tu usuario
3. Haz clic en "Perfiles"
4. Haz clic en "Añadir perfil"
5. Completa todos los campos con tu información
6. Carga tu foto de perfil y CV
7. Guarda
```

### 2. Agregar tus proyectos
```
1. En el admin, haz clic en "Proyectos"
2. Haz clic en "Añadir proyecto"
3. Completa:
   - Título
   - Descripción detallada
   - Descripción corta
   - Categoría
   - Estado
   - Tecnologías (separadas por coma)
   - URLs de GitHub y demo
   - Fechas
   - ¡Marca "Destacado" para mostrar en inicio!
4. Guarda
```

### 3. Agregar tus habilidades
```
1. En el admin, haz clic en "Habilidades"
2. Haz clic en "Añadir habilidad"
3. Completa:
   - Nombre (ej: Python, Django)
   - Categoría
   - Nivel (Principiante, Intermedio, Avanzado, Experto)
   - Icono Font Awesome (opcional)
   - Descripción (opcional)
4. Guarda
```

---

## 🎨 Personalización del diseño

El archivo `base.html` contiene toda la estilos. Puedes cambiar:

```css
/* Colores principales en base.html - línea ~13 */
:root {
    --primary: #667eea;       /* Cambiar color principal */
    --secondary: #764ba2;     /* Cambiar color secundario */
    --accent: #f093fb;        /* Cambiar color acento */
    --dark: #1a1a2e;          /* Cambiar color oscuro */
    --light: #f5f5f5;         /* Cambiar color claro */
}
```

---

## 📂 Archivos importantes

| Archivo | Descripción |
|---------|-------------|
| `models.py` | Define la estructura de datos |
| `views.py` | Contiene la lógica de las páginas |
| `forms.py` | Formularios con validación |
| `urls.py` | Rutas de navegación |
| `admin.py` | Configuración del panel admin |
| `templates/base.html` | Plantilla base (estilos globales) |
| `templates/projects/*.html` | Plantillas de cada página |

---

## 🛠️ Comandos útiles Django

```bash
# Crear migraciones si modificas modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Hacer backup de la BD
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json

# Acceder a la consola interactiva
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic

# Ejecutar tests
python manage.py test
```

---

## 🔧 Modificaciones frecuentes

### Cambiar nombre del sitio
En `templates/base.html`, línea ~180:
```html
<a class="navbar-brand" href="{% url 'projects:index' %}">
    <i class="fas fa-code"></i> TU_NOMBRE_AQUI  <!-- Cambiar aquí -->
</a>
```

### Cambiar información del footer
En `templates/base.html`, línea ~220:
```html
<h5>TU_NOMBRE</h5>
<p>Tu descripción breve aquí</p>
```

### Agregar nuevas rutas
En `projects/urls.py`:
```python
urlpatterns = [
    # Rutas existentes...
    path('nueva-seccion/', views.NuevaVista.as_view(), name='nueva_seccion'),
]
```

---

## 🐛 Solucionar problemas comunes

### Error: "Módulo no encontrado"
```bash
# Reinstala las dependencias
pip install -r ../requirements.txt
```

### Error: "Tabla no existe"
```bash
# Aplica las migraciones
python manage.py migrate
```

### Error: "Permiso denegado en archivos"
```bash
# Recarga archivos estáticos
python manage.py collectstatic --noinput
```

### Formulario de contacto no envía emails
```
# Configura en settings.py:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Así los emails aparecen en la consola en desarrollo
```

---

## 📊 Estadísticas del proyecto

- **Modelos**: 4 (Profile, Project, Skill, ContactMessage)
- **Vistas**: 8 (Index, About, Projects, Details, Skills, Contact, Download CV)
- **Plantillas**: 8 (base + 7 específicas)
- **URLs**: 7 rutas principales
- **Formularios**: 2 (Contacto, Perfil)
- **Líneas de código Python**: ~800
- **Líneas de HTML/CSS**: ~1200

---

## 💡 Tips y trucos

1. **Usa el Admin para agregar contenido** - Es más rápido que editar directamente en BD
2. **Revisa los logs** - Cuando algo falla, mira los mensajes en la terminal
3. **Usa Firefox DevTools** - Para debuggear CSS y JavaScript
4. **Haz backup regular** - Especialmente antes de cambios importantes
5. **Comenta tu código** - Facilita mantenerlo en el futuro

---

## 🚀 Próximos pasos (mejoras futuras)

- [ ] Agregar sistema de comentarios en proyectos
- [ ] Sistema de galería de imágenes por proyecto
- [ ] Blog con artículos técnicos
- [ ] Suscripción a newsletter
- [ ] Sistema de descargas de recursos
- [ ] Integración con redes sociales
- [ ] Análiticas del sitio
- [ ] Optimización SEO

---

**¡Ya estás listo! 🎉 Ahora a completar tu portfolio.**
