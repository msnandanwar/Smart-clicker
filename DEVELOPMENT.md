# Development Setup

This document provides instructions for developers who want to contribute to or modify the Smart Screen Region Clicker.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for version control)

## Setting Up Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/smart-clicker.git
   cd smart-clicker
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**:
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

## Building Executable

### Windows
Run the provided batch script:
```bash
build_exe.bat
```

Or manually:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "SmartClicker" main.py
```

### Linux/Mac
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "SmartClicker" main.py
```

## Project Structure

```
smart-clicker/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # User documentation
├── LICENSE             # MIT License
├── CHANGELOG.md        # Version history
├── .gitignore          # Git ignore rules
├── build_exe.bat       # Windows build script
└── dist/               # Built executables (gitignored)
```

## Code Structure

- **GUI Components**: Modern dark theme interface using tkinter
- **Click Logic**: Random coordinate generation within defined regions
- **Hotkey Handling**: Global ESC key listener using pynput
- **Threading**: Separate thread for clicking to keep GUI responsive
- **Error Handling**: Comprehensive input validation and error dialogs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Testing

Manual testing checklist:
- [ ] GUI opens and displays correctly
- [ ] All input fields accept valid values
- [ ] Invalid inputs show appropriate error messages
- [ ] Clicking works within specified region
- [ ] ESC key stops clicking reliably
- [ ] Statistics update correctly
- [ ] Application closes properly
