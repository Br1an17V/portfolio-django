import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from projects.models import Project, Skill

# Limpiar datos previos (opcional)
# Project.objects.all().delete()
# Skill.objects.all().delete()

print("Agregando habilidades...")

# Habilidades
habilidades = [
    ('Python', 'Lenguajes', 'expert', 'fab fa-python'),
    ('JavaScript', 'Lenguajes', 'advanced', 'fab fa-js-square'),
    ('HTML5', 'Frontend', 'expert', 'fab fa-html5'),
    ('CSS3', 'Frontend', 'advanced', 'fab fa-css3-alt'),
    ('Django', 'Frameworks', 'expert', 'fas fa-cube'),
    ('React', 'Frameworks', 'intermediate', 'fab fa-react'),
    ('PostgreSQL', 'Bases de Datos', 'advanced', 'fas fa-database'),
    ('MongoDB', 'Bases de Datos', 'intermediate', 'fas fa-database'),
    ('Git', 'Herramientas', 'expert', 'fab fa-git-alt'),
    ('Docker', 'DevOps', 'intermediate', 'fab fa-docker'),
    ('REST API', 'Backend', 'advanced', 'fas fa-network-wired'),
    ('MySQL', 'Bases de Datos', 'advanced', 'fas fa-database'),
]

for name, category, level, icon in habilidades:
    if not Skill.objects.filter(name=name).exists():
        Skill.objects.create(
            name=name,
            category=category,
            level=level,
            icon=icon,
        )
        print(f"✓ {name} agregado")

print("\nAgregando proyectos de ejemplo...")

# Proyectos
proyectos = [
    {
        'title': 'E-commerce Django',
        'short_description': 'Plataforma de e-commerce completa con carrito, pagos y admin',
        'description': '''Proyecto completo de e-commerce desarrollado en Django. 
        Incluye:
        - Catálogo de productos con búsqueda y filtros
        - Carrito de compras funcional
        - Sistema de pagos integrado con Stripe
        - Panel de administración para gestionar productos
        - Sistema de pedidos y seguimiento
        - Autenticación de usuarios segura
        - Interfaz responsiva y moderna''',
        'category': 'web',
        'status': 'completed',
        'technologies': 'Python, Django, PostgreSQL, Stripe, HTML5, CSS3, JavaScript',
        'github_url': 'https://github.com/usuario/ecommerce-django',
        'live_url': 'https://ecommerce-demo.herokuapp.com',
        'start_date': datetime.now() - timedelta(days=180),
        'end_date': datetime.now() - timedelta(days=30),
        'featured': True,
        'order': 1,
    },
    {
        'title': 'App de Tareas con React',
        'short_description': 'Aplicación de gestión de tareas en tiempo real',
        'description': '''Aplicación moderna de gestión de tareas desarrollada con React.
        Características:
        - Crear, editar y eliminar tareas
        - Marcar tareas como completadas
        - Categorías y etiquetas personalizadas
        - Sincronización en tiempo real
        - Almacenamiento local con IndexedDB
        - Notificaciones push
        - Interfaz intuitiva y responsiva''',
        'category': 'web',
        'status': 'completed',
        'technologies': 'React, JavaScript, Firebase, CSS3',
        'github_url': 'https://github.com/usuario/task-app-react',
        'live_url': 'https://task-app-react.netlify.app',
        'start_date': datetime.now() - timedelta(days=120),
        'end_date': datetime.now() - timedelta(days=45),
        'featured': True,
        'order': 2,
    },
    {
        'title': 'API REST para Blog',
        'short_description': 'API RESTful completa para un sistema de blog',
        'description': '''API REST robusta y escalable para un sistema de blog.
        Incluye:
        - Autenticación JWT
        - CRUD completo de artículos
        - Sistema de comentarios
        - Paginación y búsqueda
        - Validación de datos
        - Documentación Swagger
        - Tests unitarios e integración
        - Deploy en Docker''',
        'category': 'api',
        'status': 'completed',
        'technologies': 'Django REST Framework, PostgreSQL, JWT, Docker',
        'github_url': 'https://github.com/usuario/blog-api',
        'start_date': datetime.now() - timedelta(days=90),
        'end_date': datetime.now() - timedelta(days=20),
        'featured': True,
        'order': 3,
    },
    {
        'title': 'Dashboard Analytics',
        'short_description': 'Panel de análisis de datos con gráficos interactivos',
        'description': '''Dashboard profesional para visualización de datos y analítica.
        Funcionalidades:
        - Gráficos interactivos con Chart.js
        - Estadísticas en tiempo real
        - Filtros avanzados
        - Exportación de reportes
        - Diseño responsivo
        - Múltiples tipos de gráficos
        - Integración con API externa''',
        'category': 'web',
        'status': 'in_progress',
        'technologies': 'Vue.js, Chart.js, Node.js, MongoDB',
        'github_url': 'https://github.com/usuario/dashboard-analytics',
        'start_date': datetime.now() - timedelta(days=60),
        'featured': False,
        'order': 4,
    },
]

for proyecto in proyectos:
    if not Project.objects.filter(title=proyecto['title']).exists():
        Project.objects.create(**proyecto)
        print(f"✓ {proyecto['title']} agregado")

print("\n✅ ¡Datos de ejemplo agregados correctamente!")
print("\nAccede a http://localhost:8000/admin/ para más detalles")
print("Usuario: admin")
print("Contraseña: admin123")
