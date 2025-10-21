#!/bin/bash

# Script para ejecutar el portafolio fácilmente

echo "================================"
echo "🚀 Iniciando Portafolio Django"
echo "================================"
echo ""

# Navegar a la carpeta correcta
cd /home/brian/Escritorio/Luis/portfolio/portfolio

# Activar el entorno virtual
echo "📦 Activando entorno virtual..."
source /home/brian/Escritorio/Luis/portfolio/venv/bin/activate

# Iniciar el servidor
echo "🌐 Iniciando servidor Django..."
echo ""
echo "✅ Servidor iniciado correctamente!"
echo ""
echo "📱 Accede a tu portafolio en:"
echo "   http://localhost:8000"
echo ""
echo "🔐 Panel de administración:"
echo "   http://localhost:8000/admin"
echo "   Usuario: admin"
echo "   Contraseña: admin123"
echo ""
echo "💡 Presiona Ctrl+C para detener el servidor"
echo ""

# Ejecutar el servidor
python manage.py runserver
