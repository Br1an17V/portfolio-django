# 📋 Guía de Administración del Portafolio

## Acceso al Panel de Administración

**URL:** `http://localhost:8000/admin/`

**Usuario:** `admin`
**Contraseña:** `admin123`

---

## 🎯 Gestión de Proyectos

### Agregar un Nuevo Proyecto

1. En el panel de admin, haz clic en **"Proyectos"** → **"Agregar Proyecto"**

2. Completa los campos:

   **Información Básica:**
   - **Título:** Nombre del proyecto (ej: "Sistema de Gestión de Tareas")
   - **Descripción Corta:** Una línea (ej: "Aplicación web para organizar tareas")
   - **Descripción:** Detalle completo con características y logros

   **Detalles del Proyecto:**
   - **Categoría:** Selecciona una:
     - Web: Aplicación web
     - Móvil: App móvil
     - Desktop: Aplicación de escritorio
     - API: API REST/GraphQL
     - Bot: Bots automáticos
     - Script: Herramientas/scripts
     - Otro: Otros tipos

   - **Estado:** 
     - Completado: Proyecto terminado
     - En Progreso: Actualmente trabajando
     - Pausado: Temporalmente pausado
     - Archivado: Proyectos antiguos

   - **Tecnologías:** Separa con comas
     ```
     Python, Django, PostgreSQL, React, JavaScript
     ```

   - **Destacado:** Marca si quieres que aparezca en la página de inicio
   - **Orden:** Número para ordenar (1 primero, 2 segundo, etc.)

   **Multimedia:**
   - **Imagen:** Sube una portada del proyecto (recomendado: 800x600px)

   **Enlaces:**
   - **GitHub:** URL del repositorio (ej: https://github.com/usuario/proyecto)
   - **URL en Vivo:** Enlace al sitio en producción (opcional)

   **Fechas:**
   - **Fecha de Inicio:** Cuándo comenzó
   - **Fecha de Finalización:** Cuándo terminó (dejar en blanco si está en progreso)

3. Haz clic en **"Guardar"**

### Ejemplo Completo

```
Título: E-commerce Platform
Descripción Corta: Tienda en línea completa con carrito y pagos
Descripción: Plataforma de e-commerce desarrollada en Django que incluye:
- Catálogo de productos con búsqueda
- Carrito de compras funcional
- Integración con Stripe para pagos
- Panel de administración para productos
- Seguimiento de pedidos
Categoría: Web
Estado: Completado
Tecnologías: Django, React, PostgreSQL, Stripe, HTML5, CSS3
Destacado: Sí (marca la opción)
Orden: 1
Imagen: [Sube una imagen]
GitHub: https://github.com/usuario/ecommerce
URL en Vivo: https://mitienda.com
Fecha de Inicio: 01/06/2024
Fecha de Finalización: 31/08/2024
```

### Editar un Proyecto Existente

1. Ve a **"Proyectos"**
2. Haz clic en el proyecto que quieras editar
3. Modifica los campos necesarios
4. Haz clic en **"Guardar"**

### Eliminar un Proyecto

1. Ve a **"Proyectos"**
2. Marca el checkbox del proyecto
3. En "Acción", selecciona "Eliminar objetos seleccionados"
4. Haz clic en **"Ir"**
5. Confirma la eliminación

---

## 🛠️ Gestión de Habilidades

### Agregar una Habilidad

1. En el panel de admin, haz clic en **"Habilidades"** → **"Agregar Habilidad"**

2. Completa:
   - **Nombre:** Ej: "Python", "Django", "React"
   - **Categoría:** Ej: "Lenguajes", "Frameworks", "Bases de Datos"
   - **Nivel:** Selecciona tu dominio:
     - Principiante (1 estrella)
     - Intermedio (2 estrellas)
     - Avanzado (3 estrellas)
     - Experto (5 estrellas)
   - **Ícono:** Código de Font Awesome (ej: `fab fa-python`, `fab fa-js`)
   - **Orden:** Número para ordenar (1, 2, 3...)

3. Haz clic en **"Guardar"**

### Iconos Font Awesome Recomendados

```
Lenguajes:
- Python: fab fa-python
- JavaScript: fab fa-js-square
- Java: fab fa-java
- C#: fas fa-code
- PHP: fab fa-php
- Go: fas fa-code

Frameworks:
- Django: fas fa-cube
- React: fab fa-react
- Vue: fab fa-vuejs
- Angular: fab fa-angular
- FastAPI: fas fa-bolt

Bases de Datos:
- PostgreSQL: fas fa-database
- MongoDB: fas fa-leaf
- MySQL: fas fa-database
- Redis: fas fa-fire

Herramientas:
- Git: fab fa-git-alt
- Docker: fab fa-docker
- Linux: fab fa-linux
- GitHub: fab fa-github
```

---

## 📊 Filtros y Búsqueda

### Filtrar Proyectos

En la página `/proyectos/`:
- **Por Categoría:** Dropdown "Categoría"
- **Por Estado:** Dropdown "Estado"
- Combina ambos para resultados específicos

### Buscar en el Admin

1. En el admin, ve a cualquier modelo
2. Usa el campo de búsqueda en la esquina superior derecha
3. Busca por título, descripción o tecnologías

---

## 🔍 Visualizar Cambios

Una vez que guardes un proyecto, verás:

**En la página de inicio `/`:**
- Los proyectos marcados como "Destacado" con imagen

**En `/proyectos/`:**
- Tu proyecto en la lista
- Disponible para filtrar

**En `/proyectos/<id>/`:**
- Página completa del proyecto
- Todos los detalles
- Botones para GitHub y URL en vivo

**En `/habilidades/`:**
- Tu habilidad agrupada por categoría
- Mostrada con estrellas según el nivel

---

## 📝 Consejos Importantes

### ✅ DO's (Haz)

✅ Usa descripciones claras y detalladas
✅ Agrega imágenes atractivas para cada proyecto
✅ Mantén las tecnologías actualizadas
✅ Destaca tus mejores proyectos
✅ Ordena por relevancia o cronología
✅ Incluye links a GitHub y demos en vivo
✅ Revisa regularmente la página para verificar cambios

### ❌ DON'Ts (No Hagas)

❌ No dejes campos vacíos importantes
❌ No uses descripciones muy cortas
❌ No olvides agregar imágenes
❌ No enlaces rotos a GitHub
❌ No desordenes la presentación
❌ No mezcles información irrelevante
❌ No actualices categorías equivocadas

---

## 🔐 Cambiar Contraseña del Admin

1. Ve a `/admin/` con tu usuario
2. Haz clic en tu nombre en la esquina superior derecha
3. Haz clic en "Cambiar contraseña"
4. Ingresa la contraseña actual
5. Ingresa la nueva contraseña dos veces
6. Haz clic en "Cambiar contraseña"

---

## 👥 Crear Otros Usuarios Admin

Si necesitas que otra persona acceda:

1. En el admin, ve a **"Usuarios"** (en el menú principal)
2. Haz clic en **"Agregar Usuario"**
3. Ingresa usuario y contraseña
4. Marca las permisos que necesita
5. Haz clic en **"Guardar"**

---

## 📱 Respuestas de Admin por Dispositivo

El panel de admin también es responsivo:
- ✅ Funciona en móviles
- ✅ Funciona en tablets
- ✅ Funciona en desktops

---

## 🆘 Problemas Comunes

### El admin no carga
- Verifica que Django esté corriendo: `python manage.py runserver`
- Asegúrate de tener la URL correcta: `http://localhost:8000/admin/`

### No veo mis cambios
- Recarga la página (Ctrl+Shift+R para limpiar caché)
- Asegúrate de haber hecho clic en "Guardar"

### La imagen no se sube
- Verifica que Pillow esté instalado: `pip install Pillow`
- Comprueba que el tamaño sea menor a 5MB
- Usa formatos: JPG, PNG

### ¿Olvidé la contraseña?
```bash
python manage.py changepassword admin
```

---

## 📞 Siguiente Paso

**¿Listo para personalizar?**

1. Cambiar la información general del sitio
2. Agregar tus proyectos reales
3. Mostrar tus verdaderas habilidades
4. ¡Compartir con el mundo! 🌍

---

**¡Tu portafolio está completamente funcional! 🎉**
