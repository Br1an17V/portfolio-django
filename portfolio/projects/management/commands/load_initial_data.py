from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from projects.models import Profile, Project, Skill
import os


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

        # Create Profile with photo
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                name='Brian Villanueva González',
                title='Desarrollador Full Stack',
                bio='Apasionado por la programación y el desarrollo web. Especializado en Django, Python y tecnologías modernas.',
                email='brianvillanuevagonzalez@gmail.com',
                phone='+34 123 456 789',
                location='España',
                age=25
            )
            
            # Load profile photo
            photo_path = os.path.join(os.path.dirname(__file__), '../../../../../static/perfil.jpg')
            if os.path.exists(photo_path):
                with open(photo_path, 'rb') as f:
                    profile.photo.save('perfil.jpg', ContentFile(f.read()), save=True)
                self.stdout.write(self.style.SUCCESS('✓ Profile photo loaded'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠ Photo not found at {photo_path}'))
            
            self.stdout.write(self.style.SUCCESS('✓ Profile created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Profile already exists'))

        # Create Skills
        skills_data = [
            ('Python', 'advanced', 'Lenguajes'),
            ('Django', 'advanced', 'Frameworks'),
            ('JavaScript', 'intermediate', 'Lenguajes'),
            ('React', 'intermediate', 'Frontend'),
            ('HTML/CSS', 'advanced', 'Frontend'),
            ('PostgreSQL', 'intermediate', 'Bases de Datos'),
            ('Git', 'advanced', 'Herramientas'),
            ('Docker', 'beginner', 'DevOps'),
            ('REST APIs', 'advanced', 'Backend'),
            ('Bootstrap', 'advanced', 'Frontend'),
            ('Gunicorn', 'intermediate', 'DevOps'),
            ('Nginx', 'beginner', 'DevOps'),
            ('Linux', 'intermediate', 'Sistemas'),
            ('SQL', 'advanced', 'Bases de Datos'),
            ('JSON', 'advanced', 'Lenguajes'),
            ('AJAX', 'intermediate', 'Frontend'),
            ('Celery', 'beginner', 'Backend'),
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
                'title': 'Portfolio Django',
                'description': 'Portafolio personal desarrollado con Django 5.2. Incluye sección de proyectos, habilidades y formulario de contacto. Desplegado en Railway con PostgreSQL.',
                'technologies': 'Django, Python, PostgreSQL, Bootstrap, CSS',
                'link': 'https://github.com/Br1an17V/portfolio-django',
                'category': 'Web',
                'featured': True,
            },
            {
                'title': 'Sistema de Gestión de Inventario',
                'description': 'Aplicación web para gestión de inventario en tiempo real. Incluye módulos de entrada/salida de productos, reportes y control de usuarios.',
                'technologies': 'Django, Python, MySQL, JavaScript, jQuery',
                'link': '#',
                'category': 'Web',
                'featured': True,
            },
            {
                'title': 'API REST de Películas',
                'description': 'API REST desarrollada con Django REST Framework. Permite consultar, crear y actualizar información de películas. Incluye autenticación por token.',
                'technologies': 'Django REST Framework, Python, SQLite, Postman',
                'link': '#',
                'category': 'Backend',
                'featured': False,
            },
            {
                'title': 'Blog Personal',
                'description': 'Blog personal con sistema de comentarios, categorías y búsqueda. Incluye panel de administración personalizado.',
                'technologies': 'Django, Python, PostgreSQL, HTML, CSS',
                'link': '#',
                'category': 'Web',
                'featured': False,
            },
            {
                'title': 'Chatbot con IA',
                'description': 'Chatbot inteligente integrado con procesamiento de lenguaje natural. Responde preguntas frecuentes automáticamente.',
                'technologies': 'Python, NLP, Django, JavaScript',
                'link': '#',
                'category': 'Backend',
                'featured': True,
            },
            {
                'title': 'Aplicación de Tareas',
                'description': 'Aplicación de tareas con autenticación de usuarios, categorías y recordatorios. Diseño responsive e intuitivo.',
                'technologies': 'Django, React, Bootstrap, CSS, JavaScript',
                'link': '#',
                'category': 'Web',
                'featured': False,
            },
            {
                'title': 'Sistema de Facturación',
                'description': 'Sistema completo de facturación para pequeños negocios. Incluye reportes PDF, historial de facturas y gestión de clientes.',
                'technologies': 'Django, Python, ReportLab, PostgreSQL',
                'link': '#',
                'category': 'Web',
                'featured': False,
            },
        ]

        created_projects = 0
        for project_data in projects_data:
            if not Project.objects.filter(title=project_data['title']).exists():
                Project.objects.create(**project_data)
                created_projects += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ {created_projects} new projects created (Total: {Project.objects.count()})'))
        self.stdout.write(self.style.SUCCESS('\n✅ ¡Todos los datos están listos!'))
