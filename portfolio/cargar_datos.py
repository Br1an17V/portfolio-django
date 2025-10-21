import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from projects.models import Profile, Project, Skill

# Eliminar datos previos (opcional, comentar si quieres mantener)
Profile.objects.all().delete()
Project.objects.all().delete()
Skill.objects.all().delete()

# 1. CREAR PERFIL
profile = Profile.objects.create(
    name="Brian Villanueva González",
    title="Desarrollador Full Stack",
    bio="""Soy un apasionado de la ciencia y la tecnología. Actualmente acabo de terminar un Certificado de profesionalidad de Desarrollo de Aplicaciones Web y soy estudiante en la escuela disruptiva 42 Málaga. También tengo formación en Sistemas Microinformáticos y Redes, un Certificado de Profesionalidad.""",
    email="brianvillanuevagonzalez@gmail.com",
    phone="666281793",
    location="Málaga, España",
    age=45,
    profile_image="perfil.jpg",
    cv_file="C.V-Brian_Villanueva.pdf",
    github_url="https://github.com/Br1an17V",
    linkedin_url="",
    twitter_url="",
    instagram_url=""
)
print("✓ Perfil creado")

# 2. CREAR PROYECTOS
projects_data = [
    {
        "title": "Juego PHP - Adivina el número",
        "description": "Juego realizado en PHP en el que el usuario intenta adivinar el número que ha pensado el ordenador. Tendrás 5 intentos para averiguar el número.",
        "category": "php",
        "github_url": "https://github.com/Br1an17V/adivina-el-numero-php",
        "featured": True,
        "order": 1,
        "technologies": "PHP, HTML5, CSS3",
        "start_date": datetime(2024, 1, 15).date()
    },
    {
        "title": "Ejercicios PHP — Relación I",
        "description": "Conjunto de 15 ejercicios resueltos en PHP siguiendo una plantilla uniforme (form.php → resultado.php) y un estilo sencillo y elegante. Incluye validación de entradas, salidas limpias y algunos extras visuales (tablas, tableros y layouts accesibles).",
        "category": "php",
        "github_url": "https://github.com/Br1an17V/ejercicios-php_relacion-1",
        "featured": True,
        "order": 2,
        "technologies": "PHP, HTML5, CSS3",
        "start_date": datetime(2024, 2, 10).date()
    },
    {
        "title": "Ejercicios PHP — Relación II",
        "description": "Mini proyecto en PHP con varios ejercicios y una demo sencilla de 'Apuesta y gana', diseñado con una interfaz minimalista y elegante. Practica formularios, envío de datos por POST, navegación entre páginas y pequeños flujos lógicos.",
        "category": "php",
        "github_url": "https://github.com/Br1an17V/ejercicios-php-relacion-2",
        "featured": True,
        "order": 3,
        "technologies": "PHP, HTML5, CSS3",
        "start_date": datetime(2024, 2, 20).date()
    },
    {
        "title": "Banca Turing – CRUD PHP + MySQL",
        "description": "Aplicación educativa de gestión de clientes para un banco ficticio. Incluye CRUD completo, validación de DNI único y listado ordenable por columnas.",
        "category": "php",
        "github_url": "https://github.com/Br1an17V/banca-turing-crud-php-mysql",
        "featured": True,
        "order": 4,
        "technologies": "PHP, MySQL, HTML5, CSS3",
        "start_date": datetime(2024, 3, 5).date()
    },
    {
        "title": "Mi biblioteca — CRUD en PHP y MySQL",
        "description": "Aplicación web sencilla para la gestión de una biblioteca. Permite crear, leer, actualizar y eliminar (CRUD) libros, con soporte para géneros.",
        "category": "php",
        "github_url": "https://github.com/Br1an17V/mi-biblioteca-php-mysql",
        "featured": True,
        "order": 5,
        "technologies": "PHP, MySQL, HTML5, CSS3",
        "start_date": datetime(2024, 3, 15).date()
    },
    {
        "title": "API con FastAPI y MongoDB con Docker",
        "description": "API CRUD de libros construida con FastAPI, Motor (MongoDB async) y Docker Compose. Incluye endpoints para listar, crear, obtener, actualizar y borrar libros. La fecha se envía como YYYY-MM-DD y se guarda en Mongo como datetime.",
        "category": "python",
        "github_url": "https://github.com/Br1an17V/Api-con-FastAPI-y-MongoDB-con-Docker",
        "featured": True,
        "order": 6,
        "technologies": "Python, FastAPI, MongoDB, Docker",
        "start_date": datetime(2024, 5, 10).date()
    },
    {
        "title": "Dulce Enigma — Panadería (Django)",
        "description": "Sitio web sencillo de una panadería con páginas públicas de inicio, productos, ofertas y contacto. El proyecto está pensado para demostración/portafolio y como base para añadir catálogo, panel de administración y funcionalidades e-commerce.",
        "category": "django",
        "github_url": "https://github.com/Br1an17V/web-con-django-Dulce_Enigma",
        "featured": True,
        "order": 7,
        "technologies": "Django, Python, HTML5, CSS3, Bootstrap",
        "start_date": datetime(2024, 6, 1).date()
    }
]

for proj in projects_data:
    project = Project.objects.create(
        title=proj["title"],
        description=proj["description"],
        category=proj["category"],
        github_url=proj["github_url"],
        featured=proj["featured"],
        order=proj["order"],
        technologies=proj["technologies"],
        start_date=proj["start_date"]
    )
print(f"✓ {len(projects_data)} proyectos creados")

# 3. CREAR HABILIDADES
skills_data = [
    # Bases de datos
    {"name": "MySQL", "category": "database", "level": "expert", "order": 1},
    {"name": "MongoDB", "category": "database", "level": "expert", "order": 2},
    {"name": "SQL", "category": "database", "level": "expert", "order": 3},
    {"name": "MariaDB", "category": "database", "level": "advanced", "order": 4},
    
    # Lenguajes
    {"name": "HTML5", "category": "language", "level": "expert", "order": 1},
    {"name": "CSS3", "category": "language", "level": "expert", "order": 2},
    {"name": "JavaScript", "category": "language", "level": "advanced", "order": 3},
    {"name": "PHP", "category": "language", "level": "expert", "order": 4},
    {"name": "Python", "category": "language", "level": "advanced", "order": 5},
    {"name": "C", "category": "language", "level": "intermediate", "order": 6},
    
    # Frameworks
    {"name": "Angular", "category": "framework", "level": "advanced", "order": 1},
    {"name": "Django", "category": "framework", "level": "advanced", "order": 2},
    {"name": "FastAPI", "category": "framework", "level": "advanced", "order": 3},
    
    # Otros
    {"name": "Docker", "category": "tools", "level": "advanced", "order": 1},
    {"name": "AWS", "category": "tools", "level": "intermediate", "order": 2},
    {"name": "Linux", "category": "tools", "level": "advanced", "order": 3},
    {"name": "Git", "category": "tools", "level": "advanced", "order": 4},
]

for skill in skills_data:
    Skill.objects.create(
        name=skill["name"],
        category=skill["category"],
        level=skill["level"],
        order=skill["order"]
    )

print(f"✓ {len(skills_data)} habilidades creadas")

print("\n" + "="*60)
print("✅ DATOS CARGADOS EXITOSAMENTE")
print("="*60)
print("\nResumen:")
print(f"  • Perfil: {profile.name}")
print(f"  • Proyectos: {Project.objects.count()}")
print(f"  • Habilidades: {Skill.objects.count()}")
print("\nPuedes ver los cambios en: http://127.0.0.1:8000/admin/")
