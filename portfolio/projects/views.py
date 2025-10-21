"""
Vistas para la aplicación de portafolio profesional.

Define las vistas principales para:
- Página de inicio
- Listado y detalle de proyectos
- Listado de habilidades
- Página de acerca de mí
- Formulario de contacto
"""

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Project, Skill, Profile, ContactMessage
from .forms import ContactForm


class IndexView(ListView):
    """
    Vista de inicio - Página principal del portafolio.
    
    Muestra proyectos destacados y un resumen de habilidades.
    """
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 6
    
    def get_queryset(self):
        """Obtiene proyectos destacados ordenados por fecha"""
        return Project.objects.filter(featured=True).order_by('-start_date')
    
    def get_context_data(self, **kwargs):
        """Agrega contexto adicional a la plantilla"""
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['skills'] = Skill.objects.all()[:6]  # Top 6 habilidades
        context['all_projects_count'] = Project.objects.count()
        context['total_skills'] = Skill.objects.count()
        return context


class AboutView(TemplateView):
    """
    Vista de 'Acerca de mí' - Información profesional detallada.
    
    Muestra la biografía, habilidades y enlaces a redes sociales.
    """
    template_name = 'projects/about.html'
    
    def get_context_data(self, **kwargs):
        """Proporciona contexto con información del perfil"""
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        context['profile'] = profile
        
        # Agrupar habilidades por categoría
        skills_by_category = {}
        for skill in Skill.objects.all():
            category = skill.get_category_display()
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append(skill)
        
        context['skills_by_category'] = skills_by_category
        context['total_projects'] = Project.objects.count()
        context['total_skills'] = Skill.objects.count()
        return context


class ProjectListView(ListView):
    """
    Vista de lista de proyectos con filtros.
    
    Permite filtrar por categoría y estado, con paginación.
    """
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        """Obtiene proyectos con filtros aplicados"""
        queryset = Project.objects.all().order_by('-start_date')
        
        # Filtro por categoría
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Filtro por estado
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Búsqueda por palabra clave
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(technologies__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Agrega opciones de filtro al contexto"""
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.CATEGORY_CHOICES
        context['statuses'] = Project.STATUS_CHOICES
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_status'] = self.request.GET.get('status', '')
        context['search_query'] = self.request.GET.get('search', '')
        return context


class ProjectDetailView(DetailView):
    """
    Vista detallada de un proyecto individual.
    
    Muestra información completa con proyectos relacionados.
    """
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        """Agrega proyectos relacionados al contexto"""
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        
        # Proyectos relacionados de la misma categoría
        context['related_projects'] = Project.objects.filter(
            category=project.category
        ).exclude(id=project.id)[:3]
        
        return context


class SkillListView(ListView):
    """
    Vista de habilidades técnicas.
    
    Agrupa habilidades por categoría para visualización organizada.
    """
    model = Skill
    template_name = 'projects/skills.html'
    context_object_name = 'skills'
    
    def get_queryset(self):
        """Obtiene todas las habilidades ordenadas"""
        return Skill.objects.all().order_by('category', 'order')
    
    def get_context_data(self, **kwargs):
        """Organiza habilidades por categoría"""
        context = super().get_context_data(**kwargs)
        
        # Agrupar habilidades por categoría
        skills_by_category = {}
        for skill in self.get_queryset():
            category = skill.get_category_display()
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append(skill)
        
        context['skills_by_category'] = skills_by_category
        context['total_skills'] = Skill.objects.count()
        return context


class ContactView(View):
    """
    Vista para formulario de contacto.
    
    Gestiona tanto GET (mostrar formulario) como POST (procesar mensaje).
    """
    
    def get(self, request, *args, **kwargs):
        """Muestra el formulario de contacto vacío"""
        form = ContactForm()
        profile = Profile.objects.first()
        return render(request, 'projects/contact.html', {
            'form': form,
            'profile': profile,
        })
    
    def post(self, request, *args, **kwargs):
        """Procesa el formulario de contacto"""
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Guardar el mensaje
            message = form.save()
            
            # Enviar email de confirmación
            try:
                message.send_confirmation_email()
            except Exception as e:
                print(f"Error al enviar email: {e}")
            
            # Mensaje de éxito al usuario
            messages.success(
                request,
                '¡Mensaje enviado correctamente! Nos pondremos en contacto pronto.'
            )
            
            # Redirigir a la misma página limpia
            return redirect('projects:contact')
        else:
            # Si hay errores, mostrar formulario con errores
            profile = Profile.objects.first()
            return render(request, 'projects/contact.html', {
                'form': form,
                'profile': profile,
            })


class DownloadCVView(View):
    """
    Vista para descargar el currículum en PDF.
    """
    
    def get(self, request, *args, **kwargs):
        """Descarga el archivo CV del perfil"""
        profile = Profile.objects.first()
        
        if profile and profile.cv_file:
            return redirect(profile.cv_file.url)
        else:
            messages.error(request, 'El currículum no está disponible.')
            return redirect('projects:index')
