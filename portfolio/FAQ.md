# ❓ Preguntas Frecuentes (FAQ)

## 🚀 Instalación y Ejecución

### ¿Cómo ejecuto el servidor?
```bash
cd /home/brian/Escritorio/Luis/portfolio/portfolio
./ejecutar.sh
```

O manualmente:
```bash
cd /home/brian/Escritorio/Luis/portfolio
source venv/bin/activate
cd portfolio
python manage.py runserver
```

### ¿Por qué me sale error al ejecutar?
Asegúrate de:
1. Estar en la carpeta correcta
2. Haber activado el entorno virtual
3. Tener Python 3.8+ instalado

### ¿En qué puerto corre?
Por defecto en el puerto 8000: `http://localhost:8000`

Para usar otro puerto:
```bash
python manage.py runserver 8080
```

---

## 🔐 Admin y Contraseñas

### Contraseña olvidada
```bash
python manage.py changepassword admin
```

### Cambiar contraseña desde el admin
1. Accede a http://localhost:8000/admin
2. Haz clic en tu usuario (esquina superior derecha)
3. Cambia tu contraseña

### Crear otro usuario admin
```bash
python manage.py createsuperuser
```

---

## 📝 Agregar Contenido

### ¿Cómo agrego un proyecto?
1. Ve a http://localhost:8000/admin
2. Haz clic en "Proyectos" → "Agregar proyecto"
3. Completa el formulario
4. Haz clic en "Guardar"

### ¿Cómo agrego una habilidad?
1. Ve a http://localhost:8000/admin
2. Haz clic en "Habilidades" → "Agregar habilidad"
3. Completa el nombre, categoría y nivel
4. Haz clic en "Guardar"

### ¿Cómo agrego imágenes?
1. En el formulario de proyecto, encuentra el campo "Imagen"
2. Haz clic en "Examinar" o arrastra la imagen
3. Sube una imagen en JPG, PNG o WebP
4. Tamaño recomendado: 1200x800px

### ¿Por qué no veo mi proyecto en la web?
Algunos motivos:
- No has marcado "Destacado" (aparecerá en la lista de proyectos)
- Necesitas recargar la página (Ctrl+F5)
- No guardaste los cambios

---

## 🎨 Personalización

### ¿Cómo cambio los colores?
Edita `templates/base.html`:
```css
:root {
    --primary: #667eea;      /* Cambiar este */
    --secondary: #764ba2;    /* O este */
    --accent: #f093fb;       /* O este */
    --dark: #1a1a2e;
    --light: #f5f5f5;
}
```

Luego recarga la página (Ctrl+F5).

### ¿Cómo cambio el nombre del sitio?
Busca "Mi Portafolio" en `templates/base.html` y cámbialo en:
- Línea ~125 (Navbar)
- Línea ~230 (Footer)

### ¿Cómo cambio la foto de fondo?
La imagen por defecto es un gradiente. Para cambiarla:

1. Ve a `templates/base.html`
2. Busca la clase `.project-card-image`
3. Cambia el background o agrega una imagen

### ¿Cómo cambio el idioma?
En `portfolio/settings.py`:
```python
LANGUAGE_CODE = 'es-es'  # Ya está en español
```

### ¿Cómo cambio la zona horaria?
En `portfolio/settings.py`:
```python
TIME_ZONE = 'America/Mexico_City'  # Cambia esto
```

---

## 🖼️ Imágenes y Archivos

### ¿Dónde van las imágenes?
- Imágenes de proyectos: carpeta `media/projects/`
- Imágenes estáticas: carpeta `static/`

### ¿Qué formatos de imagen acepta?
- JPG/JPEG
- PNG
- WebP
- GIF

### ¿Cuál es el tamaño máximo de imagen?
Por defecto 5MB. Para cambiar:

`portfolio/settings.py`:
```python
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # En bytes
```

### Mis imágenes no aparecen
1. Verifica que estén en la carpeta correcta
2. Recarga la página (Ctrl+F5)
3. Intenta con otra imagen

---

## 🔍 Búsqueda y Filtros

### ¿Por qué no me funciona la búsqueda?
Los filtros en la lista de proyectos buscan por:
- Categoría exacta
- Estado exacto

No hacen búsqueda de texto. Si necesitas eso, díselo a tu desarrollador.

### ¿Cómo cambio el orden de los proyectos?
En el admin, cada proyecto tiene un campo "Orden". Los proyectos se muestran por:
1. Destacados primero
2. Fecha de inicio (más recientes primero)
3. Número de orden

---

## 🚀 Despliegue

### ¿Cómo despliego a producción?
Opciones recomendadas:
- **Heroku** (fácil)
- **PythonAnywhere** (mejor para Django)
- **AWS** (escalable)
- **DigitalOcean** (VPS)

Lee el archivo `MEJORAS.md` para instrucciones.

### ¿Qué cambios hago antes de desplegar?
1. Cambiar `DEBUG = False` en settings
2. Cambiar `SECRET_KEY`
3. Configurar `ALLOWED_HOSTS`
4. Usar una base de datos de producción (PostgreSQL)
5. Configurar variables de entorno

---

## 🐛 Errores Comunes

### "No module named django"
Instala Django:
```bash
source venv/bin/activate
pip install django
```

### "Cannot use ImageField because Pillow is not installed"
Instala Pillow:
```bash
source venv/bin/activate
pip install Pillow
```

### "No tables in database"
Ejecuta las migraciones:
```bash
python manage.py migrate
```

### "Static files not found"
Colecta los archivos estáticos:
```bash
python manage.py collectstatic --noinput
```

### "Page not found (404)"
Verifica que la URL sea correcta:
- `/` ← Inicio
- `/proyectos/` ← Proyectos
- `/proyectos/1/` ← Detalle de proyecto 1
- `/habilidades/` ← Habilidades
- `/admin/` ← Admin

### "Permission denied" al ejecutar script
Dale permisos:
```bash
chmod +x ejecutar.sh
```

---

## 💾 Base de Datos

### ¿Cómo hago backup de los datos?
```bash
python manage.py dumpdata > backup.json
```

### ¿Cómo restauro los datos?
```bash
python manage.py loaddata backup.json
```

### ¿Cómo cambio a PostgreSQL?
1. Instala PostgreSQL
2. En `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. Instala el adaptador:
```bash
pip install psycopg2
```

4. Ejecuta migraciones:
```bash
python manage.py migrate
```

---

## ⚡ Rendimiento

### ¿El sitio es lento?
Comprueba:
1. ¿Estás en desarrollo? Es normal que sea un poco lento
2. ¿Tienes muchas imágenes grandes? Comprime las imágenes
3. ¿La base de datos es muy grande? Optimiza las queries

### ¿Cómo optimizo el sitio?
Lee el archivo `MEJORAS.md` para tips de rendimiento.

---

## 📱 Responsive

### ¿Por qué se ve mal en móvil?
1. Recarga la página (Ctrl+F5)
2. Verifica que Bootstrap está cargando
3. Abre la consola (F12) para ver errores

### ¿Cómo pruebo en móvil?
Desde otra computadora en la misma red:
```bash
# Obtén tu IP local
ipconfig  # Windows
ifconfig  # Mac/Linux

# Accede desde el móvil a:
http://TU_IP_LOCAL:8000
```

---

## 🆘 Más Ayuda

Si no encuentras la solución:
1. Revisa `README.md` para documentación completa
2. Revisa `INICIO_RAPIDO.md` para pasos básicos
3. Revisa `MEJORAS.md` para optimizaciones
4. Consulta Stack Overflow
5. Lee la documentación oficial de Django

---

## 💡 Tips Finales

- **Guarda siempre antes de salir** del admin
- **Recarga (Ctrl+F5)** después de cambios CSS
- **Usa datos de ejemplo** para aprender
- **Lee la documentación** de Bootstrap y Django
- **Haz backup** de tu base de datos regularmente
- **Prueba cambios** primero en desarrollo

---

¿No encontraste tu respuesta? Escríbeme en los comentarios. 📧
