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

### Option 1: Download Executable (Recommended - NO Python Required!) 🎯
**Perfect for regular users who just want to use the tool:**

1. Download `SmartClicker.exe` from the [Releases](https://github.com/msnandanwar/Smart-clicker/releases) page
2. Double-click and run - **no installation or setup needed!**
3. **Requirements**: Only Windows 10/11 - Python is NOT required!

> ✅ **The executable is completely self-contained** - it includes Python and all dependencies bundled inside.

### Option 2: Run from Source (For Developers) 🛠️
**For users who want to modify the code or contribute:**

**Requirements**: Python 3.7+ must be installed on your system

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

### For Executable Users (Most Users) ✅
- **Windows 10/11** - That's it! No Python or additional software needed.
- The executable includes everything required to run.

### For Source Code Users (Developers) 🛠️
- **Python 3.7+** 
- **pip** (Python package manager)
- All dependencies listed in `requirements.txt` (installed automatically)

> 💡 **Tip**: If you just want to use the tool, download the executable. If you want to modify the code or contribute, use the source code option.

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

## ❓ Frequently Asked Questions

### Do I need Python installed to use this tool?
**No!** If you download the executable (`SmartClicker.exe`), you don't need Python or any other software. The executable is completely self-contained and includes everything needed to run.

### What's the difference between the executable and source code?
- **Executable**: Ready-to-use, no setup required, just download and run
- **Source Code**: For developers who want to modify the code or contribute to the project

### Why might my antivirus flag the executable?
Some antivirus software flag automation tools as potentially suspicious. This is normal for legitimate automation software. The executable is safe - it only contains your Python application and required libraries.

## 🐛 Troubleshooting

- **Application won't start (source code)**: Ensure you have Python 3.7+ installed and all dependencies
- **Application won't start (executable)**: Try running as administrator or check antivirus settings
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
