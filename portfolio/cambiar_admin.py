import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth.models import User

# Eliminar usuario 'luis' si existe
try:
    user_luis = User.objects.get(username='luis')
    user_luis.delete()
    print("✓ Usuario 'luis' eliminado")
except User.DoesNotExist:
    print("ℹ Usuario 'luis' no encontrado")

# Actualizar contraseña si el usuario Brian ya existe
try:
    user_brian = User.objects.get(username='Brian')
    user_brian.set_password('holamundo')
    user_brian.save()
    print("✓ Contraseña de usuario 'Brian' actualizada")
except User.DoesNotExist:
    # Crear nuevo usuario si no existe
    user = User.objects.create_superuser('Brian', 'brian@portfolio.local', 'holamundo')
    print("✓ Usuario 'Brian' creado")

print("\n✅ Credenciales actualizadas:")
print("   Usuario: Brian")
print("   Contraseña: holamundo")
