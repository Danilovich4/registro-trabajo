@echo off
setlocal

REM Ruta base del proyecto
set "BASE=C:\Users\Dani\OneDrive\Escritorio\02_Proyectos_Personales\02_Programacion\04_Registro_trabajo"

REM Crear estructura de carpetas
mkdir "%BASE%\src\core"
mkdir "%BASE%\src\infrastructure"
mkdir "%BASE%\src\presentation"
mkdir "%BASE%\src\config"
mkdir "%BASE%\src\tests"
mkdir "%BASE%\docs"

REM Crear archivos base
type nul > "%BASE%\README.md"
type nul > "%BASE%\.gitignore"
type nul > "%BASE%\requirements.txt"

echo.
echo ✅ Estructura de proyecto creada con éxito en:
echo %BASE%

pause
