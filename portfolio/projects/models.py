"""
Modelos para la aplicación de portafolio profesional.

Este módulo contiene los modelos de base de datos para gestionar:
- Información personal del desarrollador
- Proyectos realizados
- Habilidades técnicas
- Mensajes de contacto
"""

from django.db import models
from django.core.validators import URLValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings


def validate_age(value):
    """Valida que la edad esté en un rango razonable"""
    if value < 18 or value > 120:
        raise ValidationError("La edad debe estar entre 18 y 120 años")


class Profile(models.Model):
    """
    Modelo para la información personal del portafolio.
    
    Gestiona los datos de contacto, redes sociales y archivos personales
    del desarrollador.
    """
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre completo",
        help_text="Tu nombre y apellidos"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Título profesional",
        help_text="Ej: Desarrollador Full Stack, Ingeniero de Software"
    )
    bio = models.TextField(
        verbose_name="Biografía",
        help_text="Descripción detallada sobre ti y tu experiencia"
    )
    email = models.EmailField(
        verbose_name="Email de contacto",
        unique=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Teléfono",
        help_text="Formato: +34 666281793"
    )
    location = models.CharField(
        max_length=200,
        verbose_name="Ubicación",
        help_text="Ciudad, País"
    )
    age = models.IntegerField(
        verbose_name="Edad",
        validators=[validate_age]
    )
    profile_image = models.ImageField(
        upload_to='profile/%Y/%m/',
        verbose_name="Foto de perfil",
        null=True,
        blank=True,
        help_text="Imagen JPG o PNG, máximo 5MB"
    )
    cv_file = models.FileField(
        upload_to='cv/%Y/',
        verbose_name="Currículum (PDF)",
        null=True,
        blank=True,
        help_text="Documento PDF con tu CV"
    )
    
    # Redes sociales
    github_url = models.URLField(
        blank=True,
        verbose_name="Perfil GitHub",
        help_text="URL completa de tu perfil"
    )
    linkedin_url = models.URLField(
        blank=True,
        verbose_name="Perfil LinkedIn"
    )
    twitter_url = models.URLField(
        blank=True,
        verbose_name="Perfil Twitter"
    )
    instagram_url = models.URLField(
        blank=True,
        verbose_name="Perfil Instagram"
    )
    
    # Metadata
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )
    
    class Meta:
        verbose_name = "Perfil profesional"
        verbose_name_plural = "Perfiles"
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.name} - {self.title}"
    
    def get_social_media(self):
        """Retorna un diccionario con las redes sociales disponibles"""
        return {
            'github': self.github_url,
            'linkedin': self.linkedin_url,
            'twitter': self.twitter_url,
            'instagram': self.instagram_url,
        }


class Project(models.Model):
    """
    Modelo para proyectos profesionales y personales.
    
    Permite almacenar y gestionar información detallada de cada proyecto,
    incluyendo tecnologías, estado, enlaces externos y multimedia.
    """
    
    CATEGORY_CHOICES = [
        ('web', 'Aplicación Web'),
        ('mobile', 'Aplicación Móvil'),
        ('desktop', 'Aplicación de Escritorio'),
        ('api', 'API REST'),
        ('bot', 'Bot'),
        ('script', 'Script/Herramienta'),
        ('otro', 'Otro'),
    ]
    
    STATUS_CHOICES = [
        ('completed', 'Completado'),
        ('in_progress', 'En Progreso'),
        ('paused', 'Pausado'),
        ('archived', 'Archivado'),
    ]
    
    title = models.CharField(
        max_length=200,
        verbose_name="Título del proyecto",
        db_index=True
    )
    description = models.TextField(
        verbose_name="Descripción detallada",
        help_text="Explicación completa del proyecto, objetivos y resultados"
    )
    short_description = models.CharField(
        max_length=500,
        verbose_name="Descripción corta",
        help_text="Resumen en una línea para listados"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='web',
        verbose_name="Categoría",
        db_index=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='completed',
        verbose_name="Estado",
        db_index=True
    )
    technologies = models.CharField(
        max_length=500,
        verbose_name="Tecnologías utilizadas",
        help_text="Separa con comas: Python, Django, PostgreSQL"
    )
    image = models.ImageField(
        upload_to='projects/%Y/%m/',
        verbose_name="Imagen del proyecto",
        null=True,
        blank=True,
        help_text="Captura de pantalla o thumbnail"
    )
    github_url = models.URLField(
        verbose_name="URL de GitHub",
        blank=True,
        null=True,
        help_text="Repositorio del proyecto"
    )
    live_url = models.URLField(
        verbose_name="URL en vivo",
        blank=True,
        null=True,
        help_text="Demo o sitio desplegado"
    )
    start_date = models.DateField(
        verbose_name="Fecha de inicio",
        db_index=True
    )
    end_date = models.DateField(
        verbose_name="Fecha de finalización",
        null=True,
        blank=True
    )
    featured = models.BooleanField(
        default=False,
        verbose_name="Destacado en inicio",
        db_index=True,
        help_text="Aparecerá en la página de inicio"
    )
    order = models.IntegerField(
        default=0,
        verbose_name="Orden de visualización"
    )
    
    # Metadata
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creado en"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Actualizado en"
    )
    
    class Meta:
        ordering = ['-featured', '-start_date', 'order']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        indexes = [
            models.Index(fields=['-featured', '-start_date']),
            models.Index(fields=['category', '-start_date']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """
        Retorna una lista de tecnologías individuales.
        
        Returns:
            list: Lista de nombres de tecnologías limpiados
        """
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    def is_active(self):
        """Verifica si el proyecto está activo"""
        return self.status == 'completed'


class Skill(models.Model):
    """
    Modelo para habilidades técnicas.
    
    Almacena información sobre lenguajes, frameworks y herramientas
    que domina el desarrollador, con nivel de experiencia.
    """
    
    LEVEL_CHOICES = [
        ('beginner', 'Principiante'),
        ('intermediate', 'Intermedio'),
        ('advanced', 'Avanzado'),
        ('expert', 'Experto'),
    ]
    
    CATEGORY_CHOICES = [
        ('language', 'Lenguaje de Programación'),
        ('framework', 'Framework'),
        ('database', 'Base de Datos'),
        ('tool', 'Herramienta'),
        ('platform', 'Plataforma'),
        ('other', 'Otro'),
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name="Habilidad",
        db_index=True
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoría",
        db_index=True,
        help_text="Tipo de habilidad"
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='intermediate',
        verbose_name="Nivel de experiencia"
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Clase Font Awesome",
        help_text="Ej: fab fa-python, fas fa-database"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Descripción",
        help_text="Detalles sobre tu experiencia con esta habilidad"
    )
    order = models.IntegerField(
        default=0,
        verbose_name="Orden de visualización"
    )
    
    class Meta:
        ordering = ['category', 'order']
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        unique_together = ['name', 'category']
        indexes = [
            models.Index(fields=['category', 'order']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"
    
    def get_level_stars(self):
        """Retorna número de estrellas según el nivel"""
        stars_map = {
            'beginner': 1,
            'intermediate': 2,
            'advanced': 3,
            'expert': 4,
        }
        return stars_map.get(self.level, 0)


class ContactMessage(models.Model):
    """
    Modelo para guardar mensajes de contacto del formulario.
    
    Permite almacenar y gestionar inquietudes de visitantes
    con seguimiento de lectura y respuesta.
    """
    
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre",
        db_index=True
    )
    email = models.EmailField(
        verbose_name="Email de contacto"
    )
    subject = models.CharField(
        max_length=200,
        verbose_name="Asunto"
    )
    message = models.TextField(
        verbose_name="Mensaje"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Recibido en",
        db_index=True
    )
    read = models.BooleanField(
        default=False,
        verbose_name="Leído",
        db_index=True
    )
    responded = models.BooleanField(
        default=False,
        verbose_name="Respondido"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        indexes = [
            models.Index(fields=['-created_at', 'read']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.subject[:50]}"
    
    def mark_as_read(self):
        """Marca el mensaje como leído"""
        self.read = True
        self.save(update_fields=['read'])
    
    def send_confirmation_email(self):
        """Envía email de confirmación al usuario"""
        try:
            send_mail(
                subject='Confirmación de tu mensaje - Portfolio',
                message=f'''Hola {self.name},

Hemos recibido tu mensaje y nos pondremos en contacto pronto.

Asunto: {self.subject}

Gracias por tu interés.

Saludos,
Brian Villanueva González''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error enviando email: {e}")
