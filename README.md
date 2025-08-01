# KoriRemover

Aplicación web para remover fondos de imágenes usando inteligencia artificial.

## Características

- 🖼️ **Interfaz web moderna**: Diseño responsivo con Bootstrap
- 🎯 **Drag & Drop**: Arrastra y suelta imágenes para subirlas
- 🤖 **IA Avanzada**: Utiliza rembg para remoción automática de fondos
- 📱 **Grilla de imágenes**: Visualiza todas tus imágenes procesadas
- 💾 **Descarga flexible**: Descarga tanto la imagen original como la procesada
- 🔄 **Comparación**: Compara lado a lado la imagen original vs procesada
- 🗑️ **Gestión de archivos**: Elimina imágenes que ya no necesites

## Formatos soportados

- PNG
- JPG/JPEG
- GIF
- BMP
- WEBP

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/runeimport/KoriRemover.git
cd KoriRemover
```

2. Crea un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación:
```bash
python app.py
```

2. Abre tu navegador web y ve a `http://localhost:5000`

3. Sube una imagen arrastrándola al área designada o haciendo clic en "Seleccionar Archivo"

4. Haz clic en "Procesar" para remover el fondo

5. Descarga tu imagen procesada o compárala con la original

## Estructura del proyecto

```
KoriRemover/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias de Python
├── templates/
│   └── index.html        # Interfaz web principal
├── uploads/              # Imágenes originales (se crea automáticamente)
├── processed/            # Imágenes procesadas (se crea automáticamente)
└── README.md
```

## Tecnologías utilizadas

- **Flask**: Framework web de Python
- **rembg**: Librería de IA para remoción de fondos
- **Pillow**: Procesamiento de imágenes
- **Bootstrap 5**: Framework CSS para la interfaz
- **Font Awesome**: Iconos

## Características técnicas

- Tamaño máximo de archivo: 16MB
- Procesamiento automático con IA
- Interfaz responsiva para móviles y escritorio
- Gestión automática de archivos
- Validación de tipos de archivo
- Manejo de errores robusto

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## Soporte

Si tienes algún problema o sugerencia, por favor abre un issue en GitHub.
