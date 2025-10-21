# 📱 GUÍA COMPLETA: SUBIR A GITHUB Y DESPLEGAR EN RAILWAY

## PASO 1: PREPARAR GIT EN TU PROYECTO

### 1.1 Abre la terminal en tu proyecto:

```bash
cd /home/brian/Escritorio/Luis/portfolio
```

### 1.2 Inicializa Git (si no está inicializado):

```bash
git init
```

### 1.3 Agrega todos los archivos:

```bash
git add .
```

### 1.4 Realiza el primer commit:

```bash
git commit -m "Proyecto portfolio Django - Versión inicial"
```

---

## PASO 2: CREAR CUENTA EN GITHUB

### 2.1 Ve a GitHub:
- URL: https://github.com
- Click en "Sign up" (Registrarse)

### 2.2 Datos para registrarse:
- Email: Usa tu email (brianvillanuevagonzalez@gmail.com)
- Username: Algo como `Br1an17V` o `brian-portfolio`
- Password: Una contraseña segura

### 2.3 Verifica tu email:
- GitHub te enviará un email
- Click en el link para confirmar

### 2.4 ¡Ya tienes cuenta GitHub! ✓

---

## PASO 3: CREAR REPOSITORIO EN GITHUB

### 3.1 Una vez logueado en GitHub:

1. Click en el **+** arriba a la derecha
2. Selecciona **"New repository"**

### 3.2 Configuración del repositorio:

**Repository name:** `portfolio` (o `portfolio-django`)

**Description:** `Portfolio profesional de Brian Villanueva - Desarrollador Full Stack`

**Public o Private:** Selecciona **PUBLIC** (para que se vea el portafolio)

**Initialize repository:** 
- [ ] NO marques "Add README"
- [ ] NO marques ".gitignore"
- [ ] NO marques "License"

### 3.3 Click en **"Create repository"**

---

## PASO 4: CONECTAR TU PROYECTO LOCAL CON GITHUB

### 4.1 GitHub te mostrará comandos. Ejecuta en tu terminal:

```bash
cd /home/brian/Escritorio/Luis/portfolio

# Agrega el repositorio remoto
git remote add origin https://github.com/tu-usuario/portfolio.git

# Renombra la rama a 'main' (si es necesario)
git branch -M main

# Sube el código
git push -u origin main
```

**REEMPLAZA `tu-usuario` con tu nombre de usuario de GitHub**

Ejemplo si tu usuario es `Br1an17V`:
```bash
git remote add origin https://github.com/Br1an17V/portfolio.git
```

### 4.2 Te pedirá autenticación:

Opción A: **Token (Recomendado)**
- Ve a: https://github.com/settings/tokens
- Click en "Generate new token (classic)"
- Name: `portfolio-push`
- Select scopes: Marca `repo` (acceso completo a repos)
- Click "Generate token"
- Copia el token (aparece solo una vez)
- Pega el token cuando Git lo pida

Opción B: **Contraseña de GitHub** (si usas HTTPS)
- Usa tu contraseña de GitHub

### 4.3 ¡Listo! Tu código está en GitHub 🎉

---

## PASO 5: VERIFICAR QUE ESTÁ EN GITHUB

### 5.1 Ve a tu repositorio:
```
https://github.com/tu-usuario/portfolio
```

Ejemplo:
```
https://github.com/Br1an17V/portfolio
```

### 5.2 Deberías ver:
- ✓ Tu código (manage.py, settings.py, etc.)
- ✓ Tus templates
- ✓ Tu archivo CSS en `static/css/`
- ✓ README.md y GUIA_DESPLIEGUE.md

---

## PASO 6: DESPLEGAR EN RAILWAY

### 6.1 Ve a Railway:
```
https://railway.app
```

### 6.2 Click en "Start a new project"

### 6.3 Conecta con GitHub:
- Click en "Deploy from GitHub repo"
- Autoriza Railway a acceder a tu GitHub
- Selecciona tu repositorio `portfolio`
- Click en "Deploy"

### 6.4 Railway hace TODO automáticamente:
- Detecta que es Django
- Instala dependencias
- Crea la base de datos
- Configura el servidor
- ¡Tu portafolio está en internet! 🚀

### 6.5 Tu URL será:
```
https://portfolio-xxx.up.railway.app
```

(Donde `xxx` es un código único de Railway)

---

## COMANDOS ÚTILES PARA DESPUÉS

### Actualizar código en GitHub:

```bash
# Haz cambios en tu código

# Agrega cambios
git add .

# Crea un commit
git commit -m "Descripción de los cambios"

# Sube a GitHub
git push
```

### Railway se redeploya automáticamente cuando haces push a GitHub

---

## SOLUCIÓN DE PROBLEMAS

### Error: "Permission denied (publickey)"

**Solución:**
```bash
# Usa HTTPS en lugar de SSH
git remote set-url origin https://github.com/tu-usuario/portfolio.git
git push
```

### Error: "fatal: refusing to merge unrelated histories"

**Solución:**
```bash
git push --force-with-lease origin main
```

### Railway no redeploya después de push

**Solución:**
1. Ve a Railway Dashboard
2. Settings > Redeploy
3. Haz clic en "Manual Deploy"

---

## DOMINIO PERSONALIZADO (Opcional)

Si quieres usar tu propio dominio (`tudominio.com`):

1. Compra dominio en: Namecheap, GoDaddy, etc ($10-12/año)
2. En Railway > Settings > Domains
3. Agrega tu dominio
4. Apunta los DNS a Railway (instrucciones en la plataforma)
5. ¡Listo en ~1 hora!

---

## CHECKLIST FINAL

- [ ] Git inicializado en tu proyecto
- [ ] Repositorio creado en GitHub
- [ ] Código subido a GitHub
- [ ] Puedes ver tu código en GitHub
- [ ] Cuenta Railroad creada
- [ ] Proyecto desplegado en Railway
- [ ] Puedes acceder a tu portafolio en internet
- [ ] La foto se ve bien ovalada
- [ ] El CV se descarga correctamente
- [ ] Formulario de contacto funciona

---

## ¡FELICIDADES! 🎉

Tu portafolio está:
- ✓ En GitHub (versionado y seguro)
- ✓ En internet (accesible 24/7)
- ✓ Funcionando perfectamente
- ✓ Con dominio automático

¡Ahora puedes compartir tu portafolio con el mundo! 🌍

---

## PRÓXIMOS PASOS

1. **Agrega más proyectos** en el admin (http://tuurl.railway.app/admin/)
2. **Personaliza colores** editando `static/css/styles.css`
3. **Actualiza tu bio** en el admin
4. **Prueba el formulario de contacto** desde la página pública
5. **Comparte tu URL** con empleadores, clientes, etc.

---

## SOPORTE

Si tienes dudas:
- GitHub Docs: https://docs.github.com
- Railway Docs: https://docs.railway.app
- Django Docs: https://docs.djangoproject.com

¡Mucho éxito! 🚀

