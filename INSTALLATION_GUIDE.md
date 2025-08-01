# 🚀 GUÍA DE INSTALACIÓN Y CONFIGURACIÓN - KoriRemover

## ⚠️ Requisitos Previos

### 1. Instalar Python
Antes de ejecutar la aplicación, necesitas instalar Python 3.7 o superior.

**Opción A: Microsoft Store (Recomendado para Windows 10/11)**
1. Abre Microsoft Store
2. Busca "Python 3.11" o "Python 3.12"
3. Haz clic en "Obtener" para instalar

**Opción B: Sitio web oficial**
1. Ve a https://www.python.org/downloads/
2. Descarga Python 3.11 o 3.12 para Windows
3. **IMPORTANTE**: Durante la instalación, marca la casilla "Add Python to PATH"
4. Selecciona "Install Now"

### 2. Verificar la instalación
Abre una nueva ventana de PowerShell o CMD y ejecuta:
```
python --version
```
Si ves un error, prueba también:
```
py --version
```
Deberías ver algo como "Python 3.11.x" o "Python 3.12.x". Si ninguno de los dos comandos funciona, revisa la instalación y asegúrate de marcar "Add Python to PATH".

## 🔧 Instalación de KoriRemover

### Método 1: Instalación automática (Recomendado)
1. Abre PowerShell como administrador
2. Navega al directorio del proyecto:
   ```
   cd "c:\Users\pc\Desktop\KoriRmover\KoriRemover"
   ```
3. Ejecuta el instalador automático:
   ```
   .\install.bat
   ```

### Método 2: Instalación manual
1. Abre PowerShell en el directorio del proyecto
2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   ```
   venv\Scripts\Activate.ps1
   ```
   
   Si tienes problemas con la política de ejecución, ejecuta primero:
   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. Actualiza pip:
   ```
   python -m pip install --upgrade pip
   ```

5. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Ejecutar la Aplicación

### Método 1: Script automático
```
.\run.bat
```

### Método 2: Manual
1. Activa el entorno virtual (si no está activado):
   ```
   venv\Scripts\Activate.ps1
   ```

2. Ejecuta la aplicación:
   ```
   python app.py
   ```

3. Abre tu navegador web y ve a: http://localhost:5000

## 📱 Cómo usar KoriRemover

1. **Subir imagen**: Arrastra y suelta una imagen en el área designada o haz clic en "Seleccionar Archivo"
2. **Procesar**: Haz clic en el botón "Procesar" para remover el fondo automáticamente
3. **Descargar**: Descarga tanto la imagen original como la procesada
4. **Comparar**: Usa el botón "Comparar" para ver las imágenes lado a lado
5. **Gestionar**: Elimina imágenes que ya no necesites

## 🎯 Características

- ✅ **Formatos soportados**: PNG, JPG, JPEG, GIF, BMP, WEBP
- ✅ **Tamaño máximo**: 16MB por archivo
- ✅ **Interfaz moderna**: Diseño responsivo con Bootstrap 5
- ✅ **Drag & Drop**: Arrastra archivos directamente
- ✅ **IA avanzada**: Usa rembg para remoción precisa de fondos
- ✅ **Comparación visual**: Ve el antes y después
- ✅ **Gestión de archivos**: Organiza tus imágenes fácilmente

## 🔧 Solución de Problemas

### Error: "Python no encontrado"
- Reinstala Python marcando "Add to PATH" durante la instalación
- Reinicia PowerShell después de instalar Python

### Error: "No se puede ejecutar scripts"
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: "pip no encontrado"
```
python -m ensurepip --upgrade
```

### Error de memoria durante el procesamiento
- Asegúrate de que la imagen sea menor a 16MB
- Cierra otras aplicaciones para liberar memoria

### La aplicación no carga en el navegador
- Verifica que no haya errores en la consola
- Asegúrate de que el puerto 5000 no esté siendo usado por otra aplicación
- Intenta con http://127.0.0.1:5000

## 📂 Estructura de Archivos

```
KoriRemover/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias de Python
├── install.bat        # Script de instalación automática
├── run.bat            # Script de ejecución
├── templates/
│   └── index.html     # Interfaz web
├── uploads/           # Imágenes originales (se crea automáticamente)
├── processed/         # Imágenes procesadas (se crea automáticamente)
└── README.md
```

## 🆘 Soporte

Si tienes problemas:
1. Verifica que Python esté correctamente instalado
2. Asegúrate de que el entorno virtual esté activado
3. Revisa que todas las dependencias estén instaladas
4. Comprueba los logs en la consola para errores específicos

¡Disfruta usando KoriRemover! 🎉
