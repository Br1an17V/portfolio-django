# 🎨 Portfolio Profesional - Brian Villanueva González

> Sitio web escaparate profesional con Django - Un portafolio digital moderno y funcional

![Django](https://img.shields.io/badge/Django-5.0+-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat-square)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)

## 📋 Descripción

Portfolio profesional desarrollado con **Django** que funciona como escaparate digital completo. Permite mostrar tu trayectoria profesional, proyectos realizados, habilidades técnicas y ofrecer un canal de contacto directo.

### ✨ Características principales

- ✅ **Página de inicio**: Resumen profesional con proyectos destacados
- ✅ **Proyectos**: Listado filtrable de trabajos realizados con detalles técnicos
- ✅ **Acerca de mí**: Biografía profesional completa con foto y CV descargable
- ✅ **Habilidades**: Catálogo de competencias técnicas organizadas por categoría
- ✅ **Contacto**: Formulario funcional con validación y confirmación por email
- ✅ **Panel Admin**: Interfaz profesional para gestionar contenido
- ✅ **Diseño Responsivo**: Funciona perfectamente en móvil, tablet y desktop
- ✅ **Optimizado**: Índices de base de datos, paginación y búsqueda

---

## 🚀 Secciones del sitio

### 1. **Inicio** (`/`)
Página principal que muestra:
- Presentación profesional
- Proyectos destacados (máximo 6 por página)
- Resumen de habilidades principales
- Acceso rápido a otras secciones

### 2. **Proyectos** (`/proyectos/`)
Galería completa de trabajos con:
- Filtrado por categoría y estado
- Búsqueda por palabra clave
- Información técnica de cada proyecto
- Enlaces a GitHub y demo en vivo

### 3. **Detalle de Proyecto** (`/proyectos/<id>/`)
Página individual que incluye:
- Descripción completa del proyecto
- Stack tecnológico utilizado
- Proyectos relacionados
- Enlaces y recursos

### 4. **Acerca de mí** (`/acerca-de-mi/`)
Sección de perfil profesional con:
- Foto de perfil
- Biografía completa
- Información de contacto
- Redes sociales
- Habilidades técnicas detalladas con nivel
- Descarga de CV en PDF

### 5. **Habilidades** (`/habilidades/`)
Catalogo estructurado de competencias:
- Lenguajes de Programación
- Frameworks y Librerías
- Bases de Datos
- Herramientas
- Plataformas
- Nivel de experiencia con visualización de estrellas

### 6. **Contacto** (`/contacto/`)
Formulario de comunicación con:
- Validación de campos
- Envío de confirmación por email
- Información de contacto visible
- Enlaces a redes sociales

---

## 🛠️ Tecnologías utilizadas

### Backend
- **Django 5.0**: Framework web
- **Python 3.12**: Lenguaje de programación
- **SQLite/MariaDB**: Base de datos

### Frontend
- **Bootstrap 5.3**: Framework CSS
- **Font Awesome 6.4**: Iconografía
- **Poppins Google Fonts**: Tipografía

### Herramientas
- **Git**: Control de versiones
- **VS Code**: Editor de código
- **Pillow**: Procesamiento de imágenes

---

## 📦 Instalación y configuración

### Requisitos previos
```bash
- Python 3.12+
- pip (gestor de paquetes)
- Virtual Environment (venv)
```

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Br1an17V/portfolio.git
cd portfolio/portfolio
```

2. **Crear entorno virtual**
```bash
python -m venv ../venv
source ../venv/bin/activate  # En Linux/Mac
# o
..\venv\Scripts\activate  # En Windows
```

3. **Instalar dependencias**
```bash
pip install -r ../requirements.txt
```

4. **Aplicar migraciones**
```bash
python manage.py migrate
```

5. **Crear usuario administrador**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Sitio: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## 📚 Estructura del proyecto

```
portfolio/
├── portfolio/               # Configuración principal
│   ├── settings.py         # Configuración Django
│   ├── urls.py             # URLs principales
│   ├── wsgi.py            # Configuración producción
│   └── asgi.py            # Configuración async
│
├── projects/              # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas (lógica)
│   ├── forms.py           # Formularios
│   ├── urls.py            # URLs de la app
│   ├── admin.py           # Configuración admin
│   ├── migrations/        # Migraciones BD
│   └── tests.py          # Tests unitarios
│
├── templates/            # Plantillas HTML
│   ├── base.html        # Plantilla base
│   └── projects/        # Plantillas por sección
│       ├── index.html
│       ├── about.html
│       ├── contact.html
│       ├── project_list.html
│       ├── project_detail.html
│       └── skills.html
│
├── static/              # Archivos estáticos
│   ├── css/            # Estilos personalizados
│   ├── js/             # Scripts personalizados
│   ├── perfil.jpg      # Foto de perfil
│   └── C.V-Brian.pdf   # Currículum

├── db.sqlite3           # Base de datos
├── manage.py            # Gestor Django
└── requirements.txt     # Dependencias Python
```

---

## 💾 Modelos de datos

### Profile
Información personal del desarrollador:
```python
- name: Nombre completo
- title: Título profesional
- bio: Biografía
- email: Email de contacto
- phone: Teléfono
- location: Ubicación
- age: Edad
- profile_image: Foto de perfil
- cv_file: Archivo PDF CV
- github_url, linkedin_url, twitter_url, instagram_url: Redes sociales
```

### Project
Proyectos realizados:
```python
- title: Título del proyecto
- description: Descripción completa
- short_description: Resumen corto
- category: Categoría (web, api, mobile, etc.)
- status: Estado (completado, en progreso, pausado)
- technologies: Tecnologías utilizadas
- image: Imagen del proyecto
- github_url, live_url: Enlaces
- start_date, end_date: Fechas
- featured: Destacado en inicio
- order: Orden de visualización
```

### Skill
Habilidades técnicas:
```python
- name: Nombre de la habilidad
- category: Categoría (lenguaje, framework, BD, etc.)
- level: Nivel (principiante, intermedio, avanzado, experto)
- icon: Icono Font Awesome
- description: Descripción de experiencia
- order: Orden de visualización
```

### ContactMessage
Mensajes de contacto:
```python
- name: Nombre del remitente
- email: Email del remitente
- subject: Asunto
- message: Contenido del mensaje
- created_at: Fecha de recepción
- read: Indicador de lectura
- responded: Indicador de respuesta
```

---

## 🔧 Ejemplos de código

### Herencia de plantillas

**base.html** - Plantilla base común:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mi Portfolio{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navbar, Footer, etc. -->
    {% block content %}{% endblock %}
    {% block extra_js %}{% endblock %}
</body>
</html>
```

**about.html** - Extiende base.html:
```html
{% extends "base.html" %}

{% block title %}Acerca de mí - Brian Villanueva{% endblock %}

{% block content %}
<!-- Contenido específico de la sección -->
<section class="hero">
    <h1>Acerca de mí</h1>
</section>
{% endblock %}
```

### Rutas URL

```python
# urls.py de projects
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('proyectos/', views.ProjectListView.as_view(), name='project_list'),
    path('proyectos/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('acerca-de-mi/', views.AboutView.as_view(), name='about'),
    path('habilidades/', views.SkillListView.as_view(), name='skills'),
    path('contacto/', views.ContactView.as_view(), name='contact'),
    path('descargar-cv/', views.DownloadCVView.as_view(), name='download_cv'),
]
```

### Vistas con lógica personalizada

```python
class ProjectListView(ListView):
    """Vista con filtrados y búsqueda"""
    model = Project
    template_name = 'projects/project_list.html'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Project.objects.all().order_by('-start_date')
        
        # Filtro por categoría
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Búsqueda por palabra clave
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
        
        return queryset
```

### Archivos estáticos

Uso de archivos estáticos en plantillas:
```html
<!-- Imagen de perfil desde carpeta static -->
<img src="{{ profile.profile_image.url }}" alt="Foto de perfil">

<!-- Descarga de CV -->
<a href="{% url 'projects:download_cv' %}" class="btn btn-primary">
    <i class="fas fa-download"></i> Descargar CV
</a>
```

---

## 👤 Información personal

**Nombre**: Brian Villanueva González  
**Profesión**: Desarrollador Full Stack  
**Ubicación**: Málaga, España  
**Email**: brianvillanuevagonzalez@gmail.com  
**Teléfono**: +34 666 281 793  

### Formación
- 📜 Certificado de Profesionalidad en Desarrollo de Aplicaciones Web
- 🎓 Estudiante en 42 Málaga (Escuela Disruptiva)
- 📚 Certificado de Profesionalidad en Sistemas Microinformáticos y Redes

### Redes Sociales
- 🐙 GitHub: [github.com/Br1an17V](https://github.com/Br1an17V)
- 💼 LinkedIn: [En desarrollo]
- �� Twitter: [En desarrollo]

---

## 📋 Requisitos del ejercicio

✅ **Secciones mínimas implementadas:**
- ✓ Página de inicio (landing)
- ✓ Trabajos realizados (proyectos)
- ✓ Acerca de mí (biografía, historia profesional, habilidades)
- ✓ Contacto (formulario y datos de contacto)

✅ **Secciones opcionales implementadas:**
- ✓ Tecnologías (lenguajes, frameworks, herramientas)
- ✓ Currículum descargable en PDF
- ✓ Redes sociales integradas

✅ **Repositorio GitHub:**
- ✓ Código fuente completo
- ✓ README con descripción
- ✓ Estructura bien documentada
- ✓ Extractos de código relevantes

---

## �� Paleta de colores

```css
--primary: #667eea     /* Azul principal */
--secondary: #764ba2   /* Púrpura */
--accent: #f093fb      /* Magenta */
--dark: #1a1a2e        /* Gris oscuro */
--light: #f5f5f5       /* Gris claro */
```

---

## 📝 Buenas prácticas implementadas

✅ **Django Best Practices**:
- Uso de class-based views
- Modelos bien estructurados con docstrings
- Validación de datos en formularios
- Separación de responsabilidades
- Uso de signals y managers customizados

✅ **Código Limpio**:
- Comentarios claros y descriptivos
- Nombres de variables significativos
- Funciones pequeñas y reutilizables
- DRY (Don't Repeat Yourself)

✅ **Seguridad**:
- CSRF protection en formularios
- Validación de entrada de datos
- Protección contra SQL injection (ORM)
- Email validation

✅ **Performance**:
- Índices en campos frecuentemente consultados
- Paginación de resultados
- Select_related y prefetch_related (cuando sea necesario)
- Compresión de imágenes

---

## 🚀 Despliegue

### Usando Gunicorn + Nginx

```bash
# Instalar gunicorn
pip install gunicorn

# Ejecutar aplicación
gunicorn portfolio.wsgi

# Configurar con Nginx (proxy inverso)
```

### Variables de entorno (.env)
```
DEBUG=False
SECRET_KEY=tu-clave-secreta
ALLOWED_HOSTS=dominio.com,www.dominio.com
DB_NAME=portafolio_db
DB_USER=usuario_db
DB_PASSWORD=contraseña_segura
DB_HOST=localhost
```

---

## 📧 Contacto

¿Tienes preguntas o sugerencias? ¡Contáctame!

- 📨 Email: brianvillanuevagonzalez@gmail.com
- 🔗 GitHub: [github.com/Br1an17V](https://github.com/Br1an17V)
- 💬 Visitando mi portfolio: [tu-dominio.com](https://tu-dominio.com)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- Django Community
- Bootstrap
- Font Awesome
- A todos los que visiten mi portfolio

---

**Hecho con ❤️ por Brian Villanueva González**

*Última actualización: 21 de octubre de 2025*
