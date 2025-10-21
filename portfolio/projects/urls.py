"""
Configuración de URLs para la aplicación projects.

Define las rutas para:
- Página de inicio
- Proyectos (listado y detalle)
- Acerca de mí
- Habilidades
- Contacto
- Descarga de CV
"""

from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Página de inicio
    path('', views.IndexView.as_view(), name='index'),
    
    # Proyectos
    path('proyectos/', views.ProjectListView.as_view(), name='project_list'),
    path('proyectos/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    
    # Habilidades
    path('habilidades/', views.SkillListView.as_view(), name='skills'),
    
    # Acerca de mí
    path('acerca-de-mi/', views.AboutView.as_view(), name='about'),
    
    # Contacto
    path('contacto/', views.ContactView.as_view(), name='contact'),
    
    # Descarga de CV
    path('descargar-cv/', views.DownloadCVView.as_view(), name='download_cv'),
]
