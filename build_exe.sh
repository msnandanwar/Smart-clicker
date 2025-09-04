#!/bin/bash

echo "Building Smart Screen Region Clicker executable..."
echo

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Method 1: Check if we're in a virtual environment already
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Using active virtual environment: $VIRTUAL_ENV"
    PYTHON_CMD="python"
    PIP_CMD="pip"
    PYINSTALLER_CMD="pyinstaller"
elif [[ -f ".venv/bin/python" ]]; then
    echo "Found local virtual environment: .venv"
    PYTHON_CMD=".venv/bin/python"
    PIP_CMD=".venv/bin/pip"
    PYINSTALLER_CMD=".venv/bin/pyinstaller"
elif [[ -f "../.venv/bin/python" ]]; then
    echo "Found virtual environment one level up: ../.venv"
    PYTHON_CMD="../.venv/bin/python"
    PIP_CMD="../.venv/bin/pip"
    PYINSTALLER_CMD="../.venv/bin/pyinstaller"
elif command_exists python3; then
    echo "No virtual environment found, using system Python3"
    echo "Warning: This will install PyInstaller globally if not present"
    PYTHON_CMD="python3"
    PIP_CMD="pip3"
    PYINSTALLER_CMD="pyinstaller"
elif command_exists python; then
    echo "No virtual environment found, using system Python"
    echo "Warning: This will install PyInstaller globally if not present"
    PYTHON_CMD="python"
    PIP_CMD="pip"
    PYINSTALLER_CMD="pyinstaller"
else
    echo "Error: No Python installation found!"
    echo
    echo "Please either:"
    echo "1. Create a virtual environment: python3 -m venv .venv"
    echo "2. Activate an existing virtual environment: source .venv/bin/activate"
    echo "3. Install Python and ensure it's in your PATH"
    exit 1
fi

# Check if PyInstaller is installed
if ! $PYTHON_CMD -c "import PyInstaller" 2>/dev/null; then
    echo "Installing PyInstaller..."
    if ! $PIP_CMD install pyinstaller; then
        echo "Error: Failed to install PyInstaller"
        exit 1
    fi
fi

# Build the executable
echo "Building executable..."
if ! $PYINSTALLER_CMD --onefile --windowed --name "SmartClicker" main.py; then
    echo "Error: Build failed"
    exit 1
fi

echo
echo "Build completed successfully!"
echo "Executable created at: dist/SmartClicker"
echo
