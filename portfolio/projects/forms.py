"""
Formularios para la aplicación de portafolio.

Define formularios Django con validación para:
- Formulario de contacto
- Gestión de perfiles
- Gestión de proyectos
"""

from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage, Profile


class ContactForm(forms.ModelForm):
    """
    Formulario para mensajes de contacto.
    
    Incluye validación personalizada para campos.
    """
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com',
                'required': True,
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto de tu consulta',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 6,
                'required': True,
            }),
        }
    
    def clean_name(self):
        """Valida que el nombre tenga al menos 3 caracteres"""
        name = self.cleaned_data.get('name')
        if name and len(name) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        return name
    
    def clean_subject(self):
        """Valida que el asunto tenga contenido"""
        subject = self.cleaned_data.get('subject')
        if subject and len(subject) < 5:
            raise ValidationError("El asunto debe tener al menos 5 caracteres.")
        return subject
    
    def clean_message(self):
        """Valida que el mensaje tenga contenido significativo"""
        message = self.cleaned_data.get('message')
        if message and len(message) < 10:
            raise ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return message


class ProfileForm(forms.ModelForm):
    """
    Formulario para editar información del perfil.
    
    Incluye validaciones de campos requeridos.
    """
    
    class Meta:
        model = Profile
        fields = [
            'name', 'title', 'bio', 'email', 'phone',
            'location', 'age', 'profile_image', 'cv_file',
            'github_url', 'linkedin_url', 'twitter_url', 'instagram_url'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'required': True,
                'min': 18,
                'max': 120,
            }),
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'cv_file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf',
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/username',
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/username',
            }),
            'twitter_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://twitter.com/username',
            }),
            'instagram_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://instagram.com/username',
            }),
        }
