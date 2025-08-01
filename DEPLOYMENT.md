# 🌐 KoriRemover - Guía de Despliegue

## � GitHub Pages (Demo Estático)

**URL del Demo**: https://runeimport.github.io/KoriRemover

### ✅ Ya configurado automáticamente:
- GitHub Actions configurado (`.github/workflows/deploy-pages.yml`)
- Demo estático en `/docs/index.html`
- Se despliega automáticamente en cada push a `main`

### 📋 Lo que incluye el demo:
- ✅ Interfaz completa de usuario
- ✅ Drag & drop de archivos
- ✅ Vista previa de imágenes
- ✅ Simulación de procesamiento
- ✅ Enlaces a instalación completa

## 🚀 Aplicación Completa (Con IA)

### 1. Render (Recomendado - Gratis)

**Pasos para desplegar:**

1. Ve a [render.com](https://render.com) y crea una cuenta
2. Conecta tu repositorio de GitHub (runeimport/KoriRemover)
3. Crea un nuevo "Web Service"
4. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app_basic.py`
   - **Environment**: Python 3

**Archivos incluidos para Render:**
- ✅ `Procfile` - Comando de inicio
- ✅ `runtime.txt` - Versión de Python
- ✅ `requirements.txt` - Dependencias

### 2. Railway

1. Ve a [railway.app](https://railway.app)
2. Conecta GitHub y selecciona el repositorio
3. Railway detectará automáticamente que es una app Python

### 3. Vercel

1. Ve a [vercel.com](https://vercel.com)
2. Importa desde GitHub
3. Configura como aplicación Python

### 4. PythonAnywhere (Gratis limitado)

1. Ve a [pythonanywhere.com](https://pythonanywhere.com)
2. Sube los archivos
3. Configura como aplicación Flask

## 🔧 Variables de Entorno

Para producción, configura:
- `PORT` - Puerto del servidor (automático en la mayoría de servicios)
- `DEBUG` - `false` para producción

## 📝 Notas Importantes

- La aplicación usa almacenamiento local para imágenes
- En servicios como Render, las imágenes subidas son temporales
- Para persistencia, considera usar AWS S3 o similar

## 🌟 URLs del Proyecto

- **Repositorio**: https://github.com/runeimport/KoriRemover
- **Demo Local**: http://localhost:5000

Una vez desplegado, tu aplicación estará disponible 24/7 en internet!
