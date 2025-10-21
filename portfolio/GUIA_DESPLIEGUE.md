# 🚀 GUÍA DE DESPLIEGUE - Portfolio Django en Internet

## OPCIÓN 1: HEROKU (Recomendado para principiantes)
Heroku es la opción más sencilla y tiene plan gratuito limitado.

### Pasos:
1. **Crea cuenta en Heroku:**
   - Ve a: https://www.heroku.com
   - Regístrate con email

2. **Instala Heroku CLI:**
   ```bash
   # En Ubuntu/Linux:
   curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
   
   # En macOS:
   brew install heroku/brew/heroku
   
   # En Windows:
   # Descarga desde: https://cli-assets.heroku.com/heroku-x64.exe
   ```

3. **Prepara el proyecto:**
   ```bash
   # Crea estos archivos en la raíz del proyecto:
   
   # Archivo: Procfile
   web: gunicorn portfolio.wsgi
   
   # Archivo: runtime.txt
   python-3.12.0
   
   # Actualiza requirements.txt
   cd /home/brian/Escritorio/Luis/portfolio/portfolio
   source ../venv/bin/activate
   pip freeze > requirements.txt
   
   # Agrega Gunicorn
   pip install gunicorn
   pip freeze > requirements.txt
   ```

4. **Modifica settings.py:**
   ```python
   # En portfolio/settings.py, actualiza:
   
   DEBUG = False
   
   ALLOWED_HOSTS = ['tudominio.herokuapp.com', 'localhost', '127.0.0.1']
   
   # Al final del archivo, agrega:
   import os
   if 'DATABASE_URL' in os.environ:
       import dj_database_url
       DATABASES = {
           'default': dj_database_url.config()
       }
   ```

5. **Inicia sesión en Heroku:**
   ```bash
   heroku login
   ```

6. **Crea la app en Heroku:**
   ```bash
   heroku create tu-portafolio-brian
   ```

7. **Sube el código:**
   ```bash
   git add .
   git commit -m "Deploy inicial"
   git push heroku main
   ```

8. **Abre tu app:**
   ```bash
   heroku open
   ```

---

## OPCIÓN 2: RAILWAY (Muy recomendado - Gratis y fácil)
Railway es gratis, rápido y muy sencillo.

### Pasos:
1. **Ve a:** https://railway.app
2. **Conecta tu GitHub** (o repositorio Git)
3. **Selecciona tu proyecto**
4. **Railway automáticamente detecta Django**
5. **Configura variables de entorno:**
   - `DEBUG = False`
   - `SECRET_KEY = tu_clave_secreta`
   - `ALLOWED_HOSTS = tu-app.railway.app`

6. **¡Listo! Tu app está en internet**

---

## OPCIÓN 3: RENDER (Muy moderno - Gratis)
Render es nuevo, gratis y muy fácil.

### Pasos:
1. **Ve a:** https://render.com
2. **Regístrate con GitHub**
3. **Create New > Web Service**
4. **Conecta tu repositorio**
5. **Configura:**
   - Build Command: `pip install -r requirements.txt && python manage.py migrate`
   - Start Command: `gunicorn portfolio.wsgi:application`

6. **Deploy automático ¡Listo!**

---

## OPCIÓN 4: AWS (Profesional pero más complejo)
Si quieres algo más robusto y profesional.

### Servicios recomendados:
- **AWS Elastic Beanstalk** (PaaS - más fácil)
- **AWS EC2** (IaaS - más control)
- **AWS RDS** (Base de datos)
- **AWS S3** (Almacenamiento de archivos)

Costo: Gratis el primer año con AWS Free Tier

---

## OPCIÓN 5: DIGITALOCEAN (Profesional - $5/mes)
Muy popular entre desarrolladores.

### Pasos:
1. **Ve a:** https://www.digitalocean.com
2. **Crea una cuenta**
3. **Crea un Droplet (servidor):**
   - Ubuntu 22.04
   - $5/mes (plan básico)

4. **Conecta por SSH e instala:**
   ```bash
   # Actualiza sistema
   sudo apt update && sudo apt upgrade -y
   
   # Instala Python, Nginx, PostgreSQL
   sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y
   
   # Clona tu repositorio
   git clone tu-repositorio
   cd tu-proyecto
   
   # Crea entorno virtual
   python3 -m venv venv
   source venv/bin/activate
   
   # Instala dependencias
   pip install -r requirements.txt
   pip install gunicorn
   
   # Configura Nginx (proxy inverso)
   # Configura Systemd (para ejecutar siempre)
   ```

---

## OPCIÓN 6: VPS O SERVIDOR PROPIO
Si tienes un servidor propio (GoDaddy, Namecheap, etc.).

### Instalación básica:
```bash
# Conectate por SSH
ssh usuario@tu-servidor.com

# Instala dependencias
sudo apt update
sudo apt install python3 python3-pip nginx supervisor postgresql -y

# Clona proyecto
git clone tu-repositorio
cd tu-proyecto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configura Gunicorn con Supervisor
# Configura Nginx como proxy

# Reinicia servicios
sudo systemctl restart nginx
```

---

## COMPARATIVA RÁPIDA:

| Opción | Precio | Facilidad | Recomendación |
|--------|--------|-----------|---------------|
| **Heroku** | Gratis/Pago | ⭐⭐⭐⭐⭐ | Para probar |
| **Railway** | Gratis | ⭐⭐⭐⭐⭐ | **MEJOR** |
| **Render** | Gratis | ⭐⭐⭐⭐⭐ | **MEJOR** |
| **AWS** | Gratis 1 año | ⭐⭐⭐ | Profesional |
| **DigitalOcean** | $5/mes | ⭐⭐⭐⭐ | Muy bueno |
| **VPS Propio** | Variable | ⭐⭐ | Máximo control |

---

## 🎯 MI RECOMENDACIÓN PARA TI:

**Para empezar: USA RAILWAY**
- ✓ Es gratis
- ✓ Super rápido de desplegar
- ✓ Perfecto para portafolios
- ✓ No necesita configuración compleja
- ✓ Soporta Django perfectamente

---

## PASOS RÁPIDOS PARA RAILWAY:

1. **Ve a:** https://railway.app
2. **Click en "Start a new project"**
3. **Conecta tu GitHub**
4. **Selecciona tu repositorio**
5. **Railway configura TODO automáticamente**
6. **¡Listo! Tu portafolio está en internet**

Tu URL será algo como: `tu-portafolio.up.railway.app`

---

## ANTES DE DESPLEGAR - CHECKLIST:

- [ ] ¿Tienes `requirements.txt` actualizado?
- [ ] ¿Configuraste `DEBUG = False` en settings?
- [ ] ¿Agregaste tu dominio a `ALLOWED_HOSTS`?
- [ ] ¿Tu base de datos está respaldada?
- [ ] ¿Tienes `Procfile` o configuración de inicio?
- [ ] ¿Los archivos estáticos están configurados?
- [ ] ¿El CV y foto están en `static/`?

---

## DESPUÉS DE DESPLEGAR:

- Prueba todas las URLs
- Verifica que la foto de perfil se vea bien
- Prueba descargar el CV
- Prueba el formulario de contacto
- Monitorea los logs

---

## ¿PREGUNTAS FRECUENTES?

**P: ¿Puedo usar mi propio dominio?**
R: Sí, en Railway, Render, Heroku - puedes conectar un dominio custom.

**P: ¿Qué pasa con la base de datos?**
R: Railway y Render ofrecen PostgreSQL gratis. Heroku ya no.

**P: ¿Cómo subo cambios después?**
R: Solo haz `git push` y se redeploya automáticamente.

**P: ¿Necesito certificado SSL?**
R: Todos incluyen HTTPS gratis (Let's Encrypt).

**P: ¿Los archivos static se ven?**
R: Sí, debes hacer `python manage.py collectstatic` antes de desplegar.

---

## PRÓXIMOS PASOS:

1. Elige una opción (recomiendo Railway)
2. Avísame y te ayudo con el despliegue específico
3. Configuramos tu dominio custom (opcional)
4. ¡Tu portafolio estará en internet! 🎉

