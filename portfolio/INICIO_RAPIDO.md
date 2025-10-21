# 🚀 Guía de Inicio Rápido - Portafolio Django

¡Bienvenido a tu nuevo portafolio! Aquí te mostramos cómo empezar en 5 minutos.

## ⚡ Inicio Rápido

### 1. Activar el Entorno Virtual
```bash
cd /home/brian/Escritorio/Luis/portfolio
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Ejecutar el Servidor
```bash
cd portfolio
python manage.py runserver
```

### 3. Acceder a tu Portafolio
- **Sitio**: http://localhost:8000
- **Admin**: http://localhost:8000/admin

## 🔑 Credenciales

| Campo | Valor |
|-------|-------|
| Usuario | admin |
| Contraseña | admin123 |

## 📋 Primeros Pasos

### 1. Ver tu Portafolio en Vivo
1. Abre http://localhost:8000 en tu navegador
2. Verás la página de inicio con proyectos destacados
3. Navega por las diferentes secciones

### 2. Acceder al Panel de Admin
1. Ve a http://localhost:8000/admin
2. Ingresa con usuario: `admin` y contraseña: `admin123`
3. Verás el panel de control

### 3. Agregar tus Proyectos

#### Opción A: Usando el Admin (Interfaz Gráfica)
1. En el admin, haz clic en "Proyectos" → "Agregar proyecto"
2. Completa el formulario:
   - **Título**: Nombre de tu proyecto
   - **Descripción Corta**: Resumen (max 500 caracteres)
   - **Descripción**: Descripción detallada
   - **Categoría**: Tipo de proyecto
   - **Estado**: Completado, En Progreso, etc.
   - **Tecnologías**: Python, Django, React (separadas por comas)
   - **Imagen**: Foto del proyecto (opcional)
   - **URLs**: Enlaces a GitHub o sitio en vivo
   - **Fechas**: Cuándo iniciaste y finalizaste
   - **Destacado**: Marca si quieres que aparezca en la portada

#### Opción B: Automatizado (Datos de Ejemplo)
Si ya agregaste datos de ejemplo con el script, ya tienes 4 proyectos listos.

### 4. Agregar tus Habilidades

1. En el admin, haz clic en "Habilidades" → "Agregar habilidad"
2. Completa:
   - **Habilidad**: Nombre (Python, React, etc.)
   - **Categoría**: Lenguajes, Frameworks, DevOps, etc.
   - **Nivel**: Principiante, Intermedio, Avanzado, Experto
   - **Ícono**: (Opcional) Ícono de Font Awesome

## 🎨 Personalizar tu Portafolio

### Cambiar la Información del Sitio
Edita `portfolio/settings.py`:
```python
# Cambiar zona horaria
TIME_ZONE = 'America/Mexico_City'

# Cambiar idioma
LANGUAGE_CODE = 'es-es'
```

### Cambiar Colores
Edita `templates/base.html` y busca `:root { ... }`:
```css
:root {
    --primary: #667eea;      /* Azul principal */
    --secondary: #764ba2;    /* Púrpura */
    --accent: #f093fb;       /* Rosa */
    --dark: #1a1a2e;        /* Gris oscuro */
    --light: #f5f5f5;       /* Gris claro */
}
```

### Agregar tu Información en el Footer
Edita `templates/base.html`, busca `<footer>` y personaliza el contenido.

## 🌐 URLs de tu Portafolio

| URL | Descripción |
|-----|-------------|
| `/` | Inicio |
| `/proyectos/` | Lista de proyectos |
| `/proyectos/<id>/` | Detalle de proyecto |
| `/habilidades/` | Tus habilidades |
| `/admin/` | Panel de administración |

## 💾 Hacer Cambios

Después de hacer cambios en:
- **Modelos** (models.py): Ejecuta migraciones
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Templates o Static Files**: Recarga el navegador (Ctrl+F5)
- **Views**: Reinicia el servidor

## 🔍 Carpetas Importantes

```
portfolio/
├── templates/         ← Templates HTML
│   └── projects/
│       ├── index.html ← Página de inicio
│       ├── project_list.html
│       ├── project_detail.html
│       └── skills.html
├── projects/
│   ├── models.py      ← Modelos de BD
│   ├── views.py       ← Vistas
│   ├── admin.py       ← Admin customizado
│   └── urls.py        ← Rutas
└── portfolio/
    ├── settings.py    ← Configuración
    └── urls.py        ← URLs principales
```

## 📝 Editar Archivos

### Para Cambiar el Nombre del Sitio
Busca "Mi Portafolio" en:
- `templates/base.html` (línea ~50 - Navbar)
- `templates/base.html` (línea ~210 - Footer)

### Para Agregar Redes Sociales
Edita el footer en `templates/base.html` (línea ~220)

## 🚨 Solución de Problemas

### "Error al cargar imágenes"
```bash
python manage.py collectstatic --noinput
```

### "Página en blanco después de cambios"
```bash
# Reinicia el servidor
Ctrl+C  # Detener
python manage.py runserver  # Iniciar nuevamente
```

### "No veo mis cambios"
Presiona `Ctrl+F5` en el navegador para hacer una recarga completa.

## 📱 Ver en Móvil

Desde otra computadora en la misma red:
```bash
# Obtener tu IP local
ifconfig | grep inet

# Luego accede desde el móvil a:
http://TU_IP_LOCAL:8000
```

## 🎯 Próximos Pasos

1. ✅ Personaliza los colores y el nombre
2. ✅ Agrega tus proyectos reales
3. ✅ Agrega tus habilidades
4. ✅ Completa el footer con tus redes
5. ✅ Sube a producción (Heroku, AWS, etc.)

## 📚 Documentación Completa

Para más detalles, lee `README.md`

## 💬 Necesitas Ayuda?

- Revisa la documentación oficial de Django: https://docs.djangoproject.com
- Documentación de Bootstrap: https://getbootstrap.com/docs
- Pregunta sobre Django: https://stackoverflow.com

---

**¡Tu portafolio está listo! 🎉**

Ahora solo necesitas personalizarlo con tus datos y ¡estará lista para mostrar a potenciales empleadores!
