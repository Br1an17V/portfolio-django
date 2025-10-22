from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from projects.models import Profile, Project, Skill
from datetime import date


class Command(BaseCommand):
    help = 'Load initial data into the database'

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', help='Force reload all data')

    def handle(self, *args, **options):
        force = options.get('force', False)
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='Brian').exists():
            User.objects.create_superuser('Brian', 'brianvillanuevagonzalez@gmail.com', 'holamundo')
            self.stdout.write(self.style.SUCCESS('✓ Superuser created: Brian'))

        # Clear existing data if force is set
        if force:
            Profile.objects.all().delete()
            Project.objects.all().delete()
            Skill.objects.all().delete()
            self.stdout.write(self.style.WARNING('⚠ Cleared existing data'))

        # Create Profile - Store image path from static folder
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                name='Brian Villanueva González',
                title='Desarrollador Full Stack',
                bio='Soy un apasionado de la ciencia y la tecnología. Actualmente acabo de terminar un Certificado de profesionalidad de Desarrollo de Aplicaciones Web y soy estudiante en la escuela disruptiva 42 Málaga. También tengo formación en Sistemas Microinformáticos y Redes, un Certificado de Profesionalidad.',
                email='brianvillanuevagonzalez@gmail.com',
                phone='666281793',
                location='Málaga, España',
                age=45
            )
            self.stdout.write(self.style.SUCCESS('✓ Profile created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Profile already exists'))

        # Create Skills
        skills_data = [
            # Lenguajes
            ('PHP', 'advanced', 'Lenguajes'),
            ('Python', 'advanced', 'Lenguajes'),
            ('JavaScript', 'intermediate', 'Lenguajes'),
            ('HTML5', 'advanced', 'Lenguajes'),
            ('CSS3', 'advanced', 'Lenguajes'),
            ('C', 'intermediate', 'Lenguajes'),
            
            # Frameworks & APIs
            ('Django', 'advanced', 'Frameworks'),
            ('FastAPI', 'intermediate', 'Frameworks'),
            ('Angular', 'intermediate', 'Frameworks'),
            
            # Bases de Datos
            ('MySQL', 'advanced', 'Bases de Datos'),
            ('MongoDB', 'intermediate', 'Bases de Datos'),
            ('MariaDB', 'intermediate', 'Bases de Datos'),
            ('SQL', 'advanced', 'Bases de Datos'),
            ('PHPMyAdmin', 'advanced', 'Bases de Datos'),
            
            # DevOps & Sistemas
            ('Docker', 'intermediate', 'DevOps'),
            ('Linux Avanzado', 'advanced', 'Sistemas'),
            ('Amazon AWS', 'intermediate', 'DevOps'),
            ('Scripts', 'intermediate', 'DevOps'),
        ]

        created_skills = 0
        for skill_name, level, category in skills_data:
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(name=skill_name, level=level, category=category)
                created_skills += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ {created_skills} new skills created (Total: {Skill.objects.count()})'))

        # Create Projects
        projects_data = [
            {
                'title': 'Juego PHP "Adivina el número"',
                'description': 'Juego realizado en PHP en el que el usuario intenta adivinar el número que ha pensado el ordenador. Tendrás 5 intentos para averiguar el número.',
                'short_description': 'Juego interactivo de adivinanza en PHP',
                'technologies': 'PHP, HTML5, CSS3',
                'github_url': 'https://github.com/Br1an17V/adivina-el-numero-php',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2024, 6, 1),
                'end_date': date(2024, 6, 15),
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Ejercicios PHP — Relación I',
                'description': 'Conjunto de 15 ejercicios resueltos en PHP siguiendo una plantilla uniforme (form.php → resultado.php) y un estilo sencillo y elegante. Incluye validación de entradas, salidas limpias y algunos extras visuales (tablas, tableros y layouts accesibles).',
                'short_description': '15 ejercicios PHP con validación y diseño elegante',
                'technologies': 'PHP, HTML5, CSS3',
                'github_url': 'https://github.com/Br1an17V/ejercicios-php_relacion-1',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2024, 7, 1),
                'end_date': date(2024, 7, 20),
                'featured': True,
                'order': 2,
            },
            {
                'title': 'Ejercicios PHP — Relación II',
                'description': 'Mini proyecto en PHP con varios ejercicios y una demo sencilla de "Apuesta y gana", diseñado con una interfaz minimalista y elegante. Práctica de formularios, envío de datos por POST, navegación entre páginas y flujos lógicos.',
                'short_description': 'Ejercicios PHP con demo "Apuesta y gana"',
                'technologies': 'PHP, HTML5, CSS3, JavaScript',
                'github_url': 'https://github.com/Br1an17V/ejercicios-php-relacion-2',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2024, 7, 21),
                'end_date': date(2024, 8, 5),
                'featured': False,
                'order': 3,
            },
            {
                'title': 'Banca Turing – CRUD PHP + MySQL',
                'description': 'Aplicación educativa de gestión de clientes para un banco ficticio. Incluye CRUD completo, validación de DNI único y listado ordenable por columnas.',
                'short_description': 'Sistema CRUD de gestión bancaria',
                'technologies': 'PHP, MySQL, HTML5, CSS3, JavaScript',
                'github_url': 'https://github.com/Br1an17V/banca-turing-crud-php-mysql',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2024, 8, 6),
                'end_date': date(2024, 8, 25),
                'featured': True,
                'order': 4,
            },
            {
                'title': 'Mi biblioteca — CRUD en PHP y MySQL',
                'description': 'Aplicación web sencilla para la gestión de una biblioteca. Permite crear, leer, actualizar y eliminar (CRUD) libros, con soporte para géneros.',
                'short_description': 'Gestor de biblioteca con CRUD',
                'technologies': 'PHP, MySQL, HTML5, CSS3',
                'github_url': 'https://github.com/Br1an17V/mi-biblioteca-php-mysql',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2024, 9, 1),
                'end_date': date(2024, 9, 15),
                'featured': False,
                'order': 5,
            },
            {
                'title': 'API con FastAPI y MongoDB con Docker',
                'description': 'API CRUD de libros construida con FastAPI, Motor (MongoDB async) y Docker Compose. Incluye endpoints para listar, crear, obtener, actualizar y borrar libros. La fecha se envía como YYYY-MM-DD y se guarda en Mongo como datetime.',
                'short_description': 'API REST con FastAPI, MongoDB y Docker',
                'technologies': 'FastAPI, Python, MongoDB, Docker, Docker Compose',
                'github_url': 'https://github.com/Br1an17V/Api-con-FastAPI-y-MongoDB-con-Docker',
                'live_url': '',
                'category': 'api',
                'status': 'completed',
                'start_date': date(2024, 9, 16),
                'end_date': date(2024, 10, 5),
                'featured': True,
                'order': 6,
            },
            {
                'title': 'Dulce Enigma — Panadería (Django)',
                'description': 'Sitio web sencillo de una panadería con páginas públicas de inicio, productos, ofertas y contacto. El proyecto está pensado para demostración/portafolio y como base para añadir catálogo, panel de administración y funcionalidades e-commerce.',
                'short_description': 'Web de panadería con Django',
                'technologies': 'Django, Python, HTML5, CSS3, JavaScript, MySQL',
                'github_url': 'https://github.com/Br1an17V/web-con-django-Dulce_Enigma',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2024, 10, 1),
                'end_date': date(2024, 10, 20),
                'featured': False,
                'order': 7,
            },
        ]

        created_projects = 0
        for project_data in projects_data:
            if not Project.objects.filter(title=project_data['title']).exists():
                Project.objects.create(**project_data)
                created_projects += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ {created_projects} new projects created (Total: {Project.objects.count()})'))
        self.stdout.write(self.style.SUCCESS('\n✅ ¡Todos tus datos están cargados correctamente!'))
