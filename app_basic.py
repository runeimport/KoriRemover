import os
import uuid
import logging
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw, ImageFilter
import io
import base64
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Crear directorios si no existen
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def simple_background_removal(image_path):
    """
    Implementación básica de remoción de fondo usando PIL
    Esta es una versión simplificada mientras solucionamos los problemas con rembg
    """
    try:
        # Abrir la imagen
        img = Image.open(image_path)
        
        # Convertir a RGBA si no lo está
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Crear una nueva imagen con fondo transparente
        # Esta es una implementación muy básica - idealmente usaríamos rembg
        # Por ahora, simplemente convertimos píxeles blancos a transparentes
        data = img.getdata()
        newData = []
        
        for item in data:
            # Si el píxel es blanco (o casi blanco), hacerlo transparente
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))  # Transparente
            else:
                newData.append(item)
        
        img.putdata(newData)
        return img
        
    except Exception as e:
        logger.error(f"Error en remoción básica de fondo: {e}")
        # Si falla, devolver imagen original convertida a RGBA
        img = Image.open(image_path)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        return img

def get_image_data():
    """Obtener datos de todas las imágenes procesadas"""
    try:
        images = []
        upload_files = os.listdir(app.config['UPLOAD_FOLDER']) if os.path.exists(app.config['UPLOAD_FOLDER']) else []
        processed_files = os.listdir(app.config['PROCESSED_FOLDER']) if os.path.exists(app.config['PROCESSED_FOLDER']) else []
        
        # Crear un diccionario de archivos procesados
        processed_dict = {}
        for file in processed_files:
            if file.startswith('processed_'):
                original_name = file.replace('processed_', '')
                processed_dict[original_name] = file
        
        for original_file in upload_files:
            if allowed_file(original_file):
                try:
                    image_data = {
                        'id': original_file.rsplit('.', 1)[0],
                        'original_name': original_file,
                        'original_path': os.path.join(app.config['UPLOAD_FOLDER'], original_file),
                        'processed_name': processed_dict.get(original_file, None),
                        'processed_path': os.path.join(app.config['PROCESSED_FOLDER'], processed_dict.get(original_file, '')) if processed_dict.get(original_file) else None,
                        'upload_time': datetime.fromtimestamp(os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], original_file))).strftime('%Y-%m-%d %H:%M:%S')
                    }
                    images.append(image_data)
                except Exception as e:
                    logger.warning(f"Error procesando archivo {original_file}: {e}")
                    continue
        
        return sorted(images, key=lambda x: x['upload_time'], reverse=True)
    except Exception as e:
        logger.error(f"Error obteniendo datos de imágenes: {e}")
        return []

@app.route('/')
def index():
    images = get_image_data()
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
        
        if file and allowed_file(file.filename):
            # Generar nombre único
            unique_id = str(uuid.uuid4())[:8]
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{unique_id}{ext}"
            
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            logger.info(f"Archivo subido exitosamente: {filename}")
            return jsonify({
                'success': True,
                'filename': filename,
                'message': 'Archivo subido exitosamente'
            })
        
        return jsonify({'error': 'Tipo de archivo no permitido'}), 400
        
    except Exception as e:
        logger.error(f"Error subiendo archivo: {e}")
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500

@app.route('/process/<filename>')
def process_image(filename):
    try:
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        if not os.path.exists(input_path):
            return jsonify({'error': 'Archivo no encontrado'}), 404
        
        logger.info(f"Iniciando procesamiento de: {filename}")
        
        # Usar remoción básica de fondo por ahora
        processed_img = simple_background_removal(input_path)
        
        # Guardar la imagen procesada
        processed_filename = f"processed_{filename}"
        # Cambiar extensión a PNG para soportar transparencia
        processed_filename = processed_filename.rsplit('.', 1)[0] + '.png'
        processed_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
        
        processed_img.save(processed_path, 'PNG')
        
        logger.info(f"Procesamiento completado: {processed_filename}")
        return jsonify({
            'success': True,
            'processed_filename': processed_filename,
            'message': 'Imagen procesada exitosamente (versión básica - pronto tendremos IA avanzada)'
        })
        
    except Exception as e:
        logger.error(f"Error procesando imagen {filename}: {e}")
        return jsonify({'error': f'Error al procesar la imagen: {str(e)}'}), 500

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        # Determinar si es original o procesado
        if filename.startswith('processed_'):
            folder = app.config['PROCESSED_FOLDER']
        else:
            folder = app.config['UPLOAD_FOLDER']
        
        file_path = os.path.join(folder, filename)
        
        if os.path.exists(file_path):
            logger.info(f"Descargando archivo: {filename}")
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'error': 'Archivo no encontrado'}), 404
            
    except Exception as e:
        logger.error(f"Error descargando archivo {filename}: {e}")
        return jsonify({'error': f'Error al descargar el archivo: {str(e)}'}), 500

@app.route('/delete/<filename>')
def delete_image(filename):
    try:
        # Eliminar archivo original
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(original_path):
            os.remove(original_path)
            logger.info(f"Archivo original eliminado: {filename}")
        
        # Eliminar archivo procesado si existe
        processed_filename = f"processed_{filename}"
        # También buscar versión PNG
        processed_filename_png = processed_filename.rsplit('.', 1)[0] + '.png'
        
        for pf in [processed_filename, processed_filename_png]:
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], pf)
            if os.path.exists(processed_path):
                os.remove(processed_path)
                logger.info(f"Archivo procesado eliminado: {pf}")
        
        return jsonify({'success': True, 'message': 'Imagen eliminada exitosamente'})
        
    except Exception as e:
        logger.error(f"Error eliminando imagen {filename}: {e}")
        return jsonify({'error': f'Error al eliminar la imagen: {str(e)}'}), 500

@app.route('/get_images')
def get_images():
    images = get_image_data()
    return jsonify(images)

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'El archivo es demasiado grande. Máximo 16MB.'}), 413

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def server_error(e):
    logger.error(f"Error interno del servidor: {e}")
    return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    print("🚀 Iniciando KoriRemover...")
    print("📍 Aplicación disponible en: http://localhost:5000")
    print("💡 Versión básica - pronto tendremos IA avanzada para remoción de fondos")
    print("⏹️  Presiona Ctrl+C para detener el servidor")
    print()
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido por el usuario")
    except Exception as e:
        logger.error(f"Error iniciando el servidor: {e}")
        print(f"❌ Error: {e}")
        input("Presiona Enter para continuar...")
