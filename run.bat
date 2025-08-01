@echo off
echo ========================================
echo         🚀 KoriRemover
echo     Removedor de Fondos con IA
echo ========================================
echo.

REM Verificar si el entorno virtual existe
if not exist "venv" (
    echo ❌ ERROR: Entorno virtual no encontrado.
    echo.
    echo Por favor ejecuta primero: install.bat
    echo.
    pause
    exit /b 1
)

REM Activar entorno virtual
echo 🔄 Activando entorno virtual...
call venv\Scripts\activate
if errorlevel 1 (
    echo ❌ Error al activar el entorno virtual.
    echo.
    echo Intenta ejecutar install.bat nuevamente.
    pause
    exit /b 1
)

REM Verificar si las dependencias están instaladas
echo 🔍 Verificando dependencias...
python -c "import flask, rembg, PIL" >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Las dependencias no están instaladas.
    echo.
    echo Ejecuta install.bat para instalar las dependencias.
    pause
    exit /b 1
)

echo ✅ Dependencias verificadas!
echo.
echo 🌐 Iniciando servidor web...
echo.
echo 📍 La aplicacion estara disponible en:
echo    http://localhost:5000
echo    http://127.0.0.1:5000
echo.
echo 💡 Consejos:
echo    - Arrastra imagenes directamente al navegador
echo    - Formatos soportados: PNG, JPG, GIF, BMP, WEBP
echo    - Tamaño maximo: 16MB
echo.
echo ⏹️  Presiona Ctrl+C para detener el servidor
echo.

REM Ejecutar la aplicación
python app.py
