"""
Configuración del panel de administración Django.

Define la interfaz de administración para gestionar:
- Perfil profesional
- Proyectos
- Habilidades
- Mensajes de contacto
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Project, Skill, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Administración del perfil profesional"""
    
    list_display = ('name', 'title', 'email', 'location', 'age', 'updated_at')
    list_filter = ('location', 'age', 'created_at')
    search_fields = ('name', 'title', 'email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('name', 'title', 'bio', 'age', 'location')
        }),
        ('Contacto', {
            'fields': ('email', 'phone')
        }),
        ('Multimedia', {
            'fields': ('profile_image', 'cv_file')
        }),
        ('Redes Sociales', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'instagram_url'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Administración de proyectos"""
    
    list_display = (
        'title', 'category_badge', 'status_badge', 
        'featured', 'start_date', 'order', 'updated_at'
    )
    list_filter = ('category', 'status', 'featured', 'start_date')
    search_fields = ('title', 'description', 'technologies')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'short_description', 'description')
        }),
        ('Clasificación', {
            'fields': ('category', 'status', 'featured')
        }),
        ('Detalles Técnicos', {
            'fields': ('technologies', 'image')
        }),
        ('Enlaces', {
            'fields': ('github_url', 'live_url')
        }),
        ('Fechas', {
            'fields': ('start_date', 'end_date')
        }),
        ('Visualización', {
            'fields': ('order',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    list_editable = ('featured', 'order')
    ordering = ['-featured', '-start_date']
    
    def category_badge(self, obj):
        """Muestra la categoría con color"""
        colors = {
            'web': '#667eea',
            'api': '#764ba2',
            'mobile': '#f093fb',
            'bot': '#4facfe',
            'script': '#00f2fe',
            'desktop': '#43e97b',
            'otro': '#999999',
        }
        color = colors.get(obj.category, '#999999')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px; font-size: 11px;">{}</span>',
            color,
            obj.get_category_display()
        )
    category_badge.short_description = 'Categoría'
    
    def status_badge(self, obj):
        """Muestra el estado con color"""
        colors = {
            'completed': 'green',
            'in_progress': 'orange',
            'paused': 'gray',
            'archived': 'red',
        }
        color = colors.get(obj.status, 'gray')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px; font-size: 11px;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'Estado'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Administración de habilidades"""
    
    list_display = ('name', 'category', 'level_display', 'order')
    list_filter = ('category', 'level')
    search_fields = ('name', 'description')
    list_editable = ('order',)
    ordering = ['category', 'order']
    
    fieldsets = (
        ('Información', {
            'fields': ('name', 'category', 'level')
        }),
        ('Visualización', {
            'fields': ('icon', 'order', 'description')
        })
    )
    
    def level_display(self, obj):
        """Muestra el nivel con estrellas"""
        stars = '⭐' * obj.get_level_stars()
        return f"{obj.get_level_display()} {stars}"
    level_display.short_description = 'Nivel'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Administración de mensajes de contacto"""
    
    list_display = ('name', 'email', 'subject', 'read_icon', 'responded_icon', 'created_at')
    list_filter = ('read', 'responded', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'message_preview')
    
    fieldsets = (
        ('Información del Remitente', {
            'fields': ('name', 'email')
        }),
        ('Mensaje', {
            'fields': ('subject', 'message_preview')
        }),
        ('Estado', {
            'fields': ('read', 'responded')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    list_editable = ()
    actions = ['mark_as_read', 'mark_as_responded']
    
    def read_icon(self, obj):
        """Muestra icono de lectura"""
        if obj.read:
            return format_html('✅ Leído')
        else:
            return format_html('📧 No leído')
    read_icon.short_description = 'Estado Lectura'
    
    def responded_icon(self, obj):
        """Muestra icono de respuesta"""
        if obj.responded:
            return format_html('✅ Respondido')
        else:
            return format_html('⏳ Pendiente')
    responded_icon.short_description = 'Estado Respuesta'
    
    def message_preview(self, obj):
        """Muestra vista previa del mensaje"""
        return obj.message
    message_preview.short_description = 'Mensaje'
    
    def mark_as_read(self, request, queryset):
        """Acción para marcar como leído"""
        updated = queryset.update(read=True)
        self.message_user(request, f'{updated} mensaje(s) marcado(s) como leído.')
    mark_as_read.short_description = "Marcar como leído"
    
    def mark_as_responded(self, request, queryset):
        """Acción para marcar como respondido"""
        updated = queryset.update(responded=True)
        self.message_user(request, f'{updated} mensaje(s) marcado(s) como respondido.')
    mark_as_responded.short_description = "Marcar como respondido"
