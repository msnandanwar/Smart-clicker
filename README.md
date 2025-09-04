# Smart Screen Region Clicker

A modern, user-friendly desktop automation tool that performs automated mouse clicking within a defined rectangular region.

## 🎯 Features

- **Random Region Clicking**: Click at random points within a user-defined rectangular area
- **Modern Dark UI**: Beautiful, professional interface with real-time feedback
- **Keyboard Controls**: ESC key for instant stopping
- **Live Statistics**: Real-time click count, runtime, and click rate monitoring
- **Visual Feedback**: Color-coded status indicators and position tracking
- **Safety Features**: Input validation and error handling
- **Configurable Delays**: Set custom delays between clicks

## 🚀 Quick Start

### Option 1: Download Executable (Windows)
1. Download `SmartClicker.exe` from the [Releases](https://github.com/msnandanwar/Smart-clicker/releases) page
2. Run the executable - no installation needed!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/msnandanwar/Smart-clicker.git
cd Smart-clicker

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## 🎮 How to Use

1. **Set Coordinates**: Define your click region by entering:
   - Top Left X, Y coordinates
   - Bottom Right X, Y coordinates
   - Use "Get Current Mouse Position" to help find coordinates

2. **Configure Delay**: Set the delay between clicks (in seconds)

3. **Start Clicking**: Click the "▶ START CLICKING" button

4. **Stop Clicking**: Press the **ESC key** at any time to stop

## 📋 Requirements

- Python 3.7+ (for source installation)
- Windows 10/11 (for executable)
- Dependencies listed in `requirements.txt`

## 🛠️ Building Executable

### Easy Method (Recommended)

**Windows:**
```bash
# Double-click the build script or run:
.\build_exe.bat
```

**Linux/Mac:**
```bash
# Make script executable first (one time only):
chmod +x build_exe.sh

# Then run:
./build_exe.sh
```

The build scripts will automatically:
- Detect your Python environment (virtual env or system)
- Install PyInstaller if needed
- Build the executable

### Manual Method

If you prefer to build manually:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name "SmartClicker" main.py
```

The executable will be created in the `dist/` folder.

## ⚠️ Important Notes

- **Use Responsibly**: Only use this tool on applications and websites you own or have permission to automate
- **Screen Coordinates**: Make sure your coordinates are within screen bounds
- **Antivirus**: Some antivirus software may flag automation tools - this is normal for legitimate automation software

## 🐛 Troubleshooting

- **Application won't start**: Ensure you have Python 3.7+ installed and all dependencies
- **Clicking not working**: Verify coordinates are correct and within screen bounds
- **Can't stop clicking**: Press ESC key (works globally)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

See [DEVELOPMENT.md](DEVELOPMENT.md) for development setup instructions.

## 📄 License

This project is licensed under a Custom License - see the [LICENSE](LICENSE) file for details.

**Summary**: You can use and distribute this software freely, but modifications require author permission.

## 🙏 Acknowledgments

- Built with Python, tkinter, pyautogui, and pynput
- Modern UI inspired by contemporary desktop applications
