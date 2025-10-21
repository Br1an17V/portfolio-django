from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from projects.models import Profile, Project, Skill
from datetime import date
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
            
            # Load profile image - try multiple paths
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            photo_paths = [
                os.path.join(base_dir, 'static', 'perfil.jpg'),
                os.path.join(base_dir, '..', 'static', 'perfil.jpg'),
                '/home/brian/Escritorio/Luis/portfolio/portfolio/static/perfil.jpg',
            ]
            
            photo_loaded = False
            for photo_path in photo_paths:
                if os.path.exists(photo_path):
                    try:
                        with open(photo_path, 'rb') as f:
                            profile.profile_image.save('perfil.jpg', ContentFile(f.read()), save=True)
                        self.stdout.write(self.style.SUCCESS(f'✓ Profile image loaded from {photo_path}'))
                        photo_loaded = True
                        break
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'⚠ Error loading image from {photo_path}: {e}'))
            
            if not photo_loaded:
                self.stdout.write(self.style.WARNING('⚠ Profile image not found in any expected path'))
            
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

        # Create Projects - ACTUALIZA ESTOS CON TUS VERDADEROS PROYECTOS
        projects_data = [
            {
                'title': 'Tu Primer Proyecto',
                'description': 'Describe tu primer proyecto aquí',
                'short_description': 'Primer proyecto',
                'technologies': 'Tecnologías usadas',
                'github_url': '',
                'live_url': '',
                'category': 'web',
                'status': 'completed',
                'start_date': date(2025, 1, 1),
                'end_date': date(2025, 1, 31),
                'featured': True,
                'order': 1,
            },
        ]

        created_projects = 0
        for project_data in projects_data:
            if not Project.objects.filter(title=project_data['title']).exists():
                Project.objects.create(**project_data)
                created_projects += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ {created_projects} new projects created (Total: {Project.objects.count()})'))
        self.stdout.write(self.style.SUCCESS('\n✅ ¡Todos los datos están listos!'))
