@echo off
echo Building Smart Screen Region Clicker executable...
echo.

:: Method 1: Check if we're in a virtual environment already
if defined VIRTUAL_ENV (
    echo Using active virtual environment: %VIRTUAL_ENV%
    goto :build
)

:: Method 2: Look for local virtual environment
if exist ".venv\Scripts\python.exe" (
    echo Found local virtual environment: .venv
    set "PYTHON_PATH=.venv\Scripts\python.exe"
    set "PIP_PATH=.venv\Scripts\pip.exe"
    set "PYINSTALLER_PATH=.venv\Scripts\pyinstaller.exe"
    goto :check_pyinstaller
)

:: Method 3: Look for virtual environment one level up (current setup)
if exist "..\\.venv\\Scripts\\python.exe" (
    echo Found virtual environment one level up: ..\\.venv
    set "PYTHON_PATH=..\\.venv\\Scripts\\python.exe"
    set "PIP_PATH=..\\.venv\\Scripts\\pip.exe"
    set "PYINSTALLER_PATH=..\\.venv\\Scripts\\pyinstaller.exe"
    goto :check_pyinstaller
)

:: Method 4: Try system Python
python --version >nul 2>&1
if not errorlevel 1 (
    echo No virtual environment found, using system Python
    echo Warning: This will install PyInstaller globally if not present
    set "PYTHON_PATH=python"
    set "PIP_PATH=pip"
    set "PYINSTALLER_PATH=pyinstaller"
    goto :check_pyinstaller
)

:: No Python found
echo Error: No Python installation found!
echo.
echo Please either:
echo 1. Create a virtual environment: python -m venv .venv
echo 2. Activate an existing virtual environment
echo 3. Install Python and ensure it's in your PATH
pause
exit /b 1

:check_pyinstaller
:: Check if PyInstaller is installed
"%PYTHON_PATH%" -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo Installing PyInstaller...
    "%PIP_PATH%" install pyinstaller
    if errorlevel 1 (
        echo Error: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

:build
:: Build the executable
echo Building executable...
if defined VIRTUAL_ENV (
    pyinstaller --onefile --windowed --name "SmartClicker" main.py
) else (
    "%PYINSTALLER_PATH%" --onefile --windowed --name "SmartClicker" main.py
)

if errorlevel 1 (
    echo Error: Build failed
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo Executable created at: dist\SmartClicker.exe
echo.
pause
pause
