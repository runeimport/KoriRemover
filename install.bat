@echo off
echo ========================================
echo      KoriRemover - Instalacion
echo ========================================
echo.

REM Verificar si Python está instalado
echo Verificando instalacion de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Python no esta instalado.
    echo.
    echo Por favor instala Python 3.7 o superior desde:
    echo 1. Microsoft Store ^(busca "Python 3.11"^)
    echo 2. https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Durante la instalacion, marca "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado!
python --version

REM Verificar si el entorno virtual ya existe
if exist "venv" (
    echo.
    echo ⚠️  El entorno virtual ya existe. ¿Quieres recrearlo? ^(y/n^)
    set /p recreate=
    if /i "%recreate%"=="y" (
        echo Eliminando entorno virtual existente...
        rmdir /s /q venv
    ) else (
        echo Usando entorno virtual existente...
        goto activate_venv
    )
)

REM Crear entorno virtual
echo.
echo 📦 Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo ❌ Error al crear el entorno virtual.
    pause
    exit /b 1
)

:activate_venv
REM Activar entorno virtual
echo.
echo 🔄 Activando entorno virtual...
call venv\Scripts\activate
if errorlevel 1 (
    echo ❌ Error al activar el entorno virtual.
    pause
    exit /b 1
)

REM Actualizar pip
echo.
echo 📈 Actualizando pip...
python -m pip install --upgrade pip

REM Instalar dependencias
echo.
echo 📥 Instalando dependencias...
echo    - Flask (framework web)
echo    - rembg (IA para remover fondos)
echo    - Pillow (procesamiento de imagenes)
echo    - Werkzeug (utilidades web)
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Error al instalar dependencias.
    echo.
    echo Intentando instalar dependencias una por una...
    pip install flask
    pip install rembg
    pip install Pillow
    pip install werkzeug
)

echo.
echo ========================================
echo        ✅ INSTALACION COMPLETADA!
echo ========================================
echo.
echo Para ejecutar KoriRemover:
echo   1. Ejecuta: run.bat
echo   2. O manualmente:
echo      - venv\Scripts\activate
echo      - python app.py
echo   3. Abre tu navegador en: http://localhost:5000
echo.
echo ¡Disfruta removiendo fondos con IA! 🎉
echo.
pause
