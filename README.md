# 👨‍💻 Portafolio Personal - Brian Villanueva González

[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-0B0D0E.svg)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portafolio web profesional desarrollado con **Django 5.2** y desplegado en **Railway** con **PostgreSQL**.

🌐 **[Ver portafolio en vivo](https://portfolio-django-production-16a9.up.railway.app)**

## 📋 Características

- ✅ **Información profesional completa** - Perfil con foto, ubicación, contacto y biografía
- ✅ **7 proyectos destacados** - Cada proyecto incluye descripción, tecnologías y enlace a GitHub
- ✅ **18 habilidades organizadas** - Clasificadas por categoría (Lenguajes, Frameworks, Bases de Datos, DevOps)
- ✅ **Descarga de CV** - Botón para descargar tu CV en PDF
- ✅ **Diseño responsivo** - Optimizado para móvil, tablet y desktop
- ✅ **Formulario de contacto** - Permite que visitantes se comuniquen contigo
- ✅ **Admin panel** - Panel de administración Django para gestionar contenido

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 5.2.7** - Framework web Python
- **PostgreSQL** - Base de datos relacional en producción
- **SQLite** - Base de datos para desarrollo
- **Gunicorn** - Servidor WSGI

### Frontend
- **HTML5** - Estructura
- **CSS3** - Estilos personalizados con variables CSS
- **Bootstrap 5.3** - Framework de diseño responsivo
- **JavaScript** - Interactividad
- **Font Awesome 6.4** - Iconos

### Infraestructura & DevOps
- **Docker** - Containerización
- **Railway** - Hosting y despliegue
- **WhiteNoise** - Servicio de archivos estáticos
- **dj-database-url** - Configuración dinámica de base de datos

## 📁 Estructura del Proyecto

```
portfolio/
├── portfolio/                          # Configuración principal Django
│   ├── settings.py                    # Configuración de producción
│   ├── urls.py                        # Enrutamiento principal
│   ├── wsgi.py                        # Interfaz WSGI
│   └── views.py                       # Vistas globales
├── projects/                          # Aplicación principal
│   ├── models.py                      # Modelos (Profile, Project, Skill)
│   ├── views.py                       # Vistas (CBV)
│   ├── urls.py                        # URLs de proyectos
│   ├── admin.py                       # Panel de administración
│   └── management/commands/
│       └── load_initial_data.py       # Comando para cargar datos iniciales
├── templates/                         # Plantillas HTML
│   ├── base.html                      # Plantilla base
│   └── projects/
│       ├── index.html                 # Página principal
│       ├── about.html                 # Acerca de (perfil + CV)
│       ├── project_list.html          # Listado de proyectos
│       ├── project_detail.html        # Detalle de proyecto
│       └── skills.html                # Habilidades
├── static/                            # Archivos estáticos
│   ├── css/
│   │   └── styles.css                 # Estilos personalizados
│   ├── perfil.jpg                     # Foto de perfil
│   └── C.V-Brian _Villanueva.pdf     # CV descargable
├── Dockerfile                         # Configuración Docker
├── requirements.txt                   # Dependencias Python
└── manage.py                          # Herramienta de administración Django
```

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.12+
- pip
- virtualenv (recomendado)

### Instalación Local

1. **Clonar el repositorio**
```bash
git clone https://github.com/Br1an17V/portfolio-django.git
cd portfolio
```

2. **Crear ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno** (opcional para desarrollo)
```bash
export DEBUG=True
export DATABASE_URL=sqlite:///db.sqlite3
```

5. **Ejecutar migraciones**
```bash
cd portfolio
python manage.py migrate
```

6. **Cargar datos iniciales**
```bash
python manage.py load_initial_data --force
```

7. **Crear superusuario** (si no lo hizo el comando anterior)
```bash
python manage.py createsuperuser
```

8. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

Accede a `http://localhost:8000`

## 📦 Despliegue en Railway

El proyecto está configurado para despliegue automático en Railway:

1. **Conectar repositorio GitHub** a Railway
2. **Agregar variables de entorno** en Railway:
   - `DEBUG=False`
   - `ALLOWED_HOSTS=*.up.railway.app`
   - `SECRET_KEY=tu-clave-secreta`
3. **Railway detectará automáticamente**:
   - `Dockerfile` para construcción
   - `requirements.txt` para dependencias
   - PostgreSQL se provisionará automáticamente

El despliegue se ejecuta automáticamente con cada push a la rama `main`.

## 🔐 Panel de Administración

Accede al panel en `/admin/`:
- **Usuario**: Brian
- **Contraseña**: holamundo

Desde aquí puedes:
- Gestionar perfil
- Crear/editar proyectos
- Agregar/eliminar habilidades
- Ver mensajes de contacto

## 📊 Modelos de Base de Datos

### Profile
```python
- name (CharField)
- title (CharField)
- bio (TextField)
- email (EmailField)
- phone (CharField)
- location (CharField)
- age (IntegerField)
- profile_image (ImageField)
- github_url (URLField)
- linkedin_url (URLField)
```

### Project
```python
- title (CharField)
- description (TextField)
- short_description (CharField)
- technologies (CharField)
- category (CharField)
- status (CharField)
- github_url (URLField)
- live_url (URLField)
- start_date (DateField)
- end_date (DateField)
- featured (BooleanField)
- order (IntegerField)
```

### Skill
```python
- name (CharField)
- level (CharField: advanced/intermediate/beginner)
- category (CharField)
```

## 🎨 Personalización

### Cambiar datos personales
Edita en `/admin/` o modifica `portfolio/projects/management/commands/load_initial_data.py`

### Agregar proyectos
1. Opción 1: Via `/admin/` (más fácil)
2. Opción 2: Agregar a `load_initial_data.py` y ejecutar `python manage.py load_initial_data --force`

### Modificar estilos
Los estilos están en `static/css/styles.css` con variables CSS que facilitan la personalización:
```css
:root {
    --primary: #667eea;
    --secondary: #764ba2;
    /* ... más variables */
}
```

## 📱 Páginas Disponibles

- **Inicio** (`/`) - Página principal con proyectos destacados
- **Proyectos** (`/proyectos/`) - Listado completo de proyectos
- **Detalle de Proyecto** (`/proyectos/<slug>/`) - Información completa de cada proyecto
- **Acerca de mí** (`/acerca-de-mi/`) - Perfil, foto, CV descargable
- **Habilidades** (`/habilidades/`) - Listado de todas las habilidades
- **Contacto** (`/contacto/`) - Formulario de contacto

## �� Solución de Problemas

### La foto de perfil no aparece
- Verifica que `static/perfil.jpg` existe
- Ejecuta `python manage.py collectstatic --noinput`
- En Railway, espera a que `collectstatic` complete durante el build

### El CV no se descarga
- Verifica que `static/C.V-Brian _Villanueva.pdf` existe
- Ejecuta `python manage.py collectstatic --noinput`

### Error de CSRF en producción
- Asegúrate de que `CSRF_TRUSTED_ORIGINS` incluya tu dominio Railway
- Revisar `portfolio/settings.py`

## 🔄 Actualizar en Producción

Simplemente haz push a GitHub:
```bash
git add .
git commit -m "Tu mensaje"
git push origin main
```

Railway detectará automáticamente los cambios y redesplegará la aplicación.

## 📞 Contacto

- **Email**: brianvillanuevagonzalez@gmail.com
- **Teléfono**: 666281793
- **GitHub**: [@Br1an17V](https://github.com/Br1an17V)
- **Ubicación**: Málaga, España

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE` para más detalles.

---

**Hecho con ❤️ por Brian Villanueva González**

⭐ Si te gustó este proyecto, déjale una estrella en GitHub
