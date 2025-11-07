#!/usr/bin/env python3
"""
IRUS V6.0 - Easy Launcher
Simple one-click launcher for IRUS V6.0
Handles all setup and launches the application
"""

import os
import sys
import subprocess
import platform
import tkinter as tk
from tkinter import messagebox
import webbrowser

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        return False, f"{version.major}.{version.minor}"
    return True, f"{version.major}.{version.minor}"

def check_dependencies():
    """Check if required dependencies are installed"""
    required_modules = ['tkinter', 'threading', 'json', 'os', 'sys']
    optional_modules = ['requests', 'psutil']
    
    missing_required = []
    missing_optional = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_required.append(module)
    
    for module in optional_modules:
        try:
            __import__(module)
        except ImportError:
            missing_optional.append(module)
    
    return missing_required, missing_optional

def install_dependencies():
    """Install missing dependencies"""
    try:
        # Install optional dependencies for better experience
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', 'psutil'])
        return True
    except Exception as e:
        print(f"Warning: Could not install optional dependencies: {e}")
        return False

def show_welcome_dialog():
    """Show welcome dialog for new users"""
    root = tk.Tk()
    root.withdraw()
    
    welcome_msg = """🎉 Welcome to IRUS V6.0! 🎉

IRUS (Intelligent Rewrite and Upgrade System) converts Windows Python scripts to work perfectly on macOS.

🚀 Quick Start:
1. Click 'Launch IRUS' to start the application
2. Select your Windows Python script
3. Choose 'macOS' as target system (recommended)
4. Click 'Start Conversion'
5. Your script will be converted for macOS!

💡 New Features in V6.0:
• Enhanced macOS optimization
• Improved Discord integration
• Better theme and font controls
• Advanced experimental features
• Real-time bug analysis

🌐 Need Help?
Join our Discord: https://discord.gg/j6wtpGJVng

Ready to convert your scripts?"""
    
    result = messagebox.askyesno("Welcome to IRUS V6.0", welcome_msg)
    root.destroy()
    return result

def launch_irus():
    """Launch the main IRUS application"""
    try:
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, current_dir)
        
        # Import and run IRUS
        from gui.professional_ui import ProfessionalMainWindow
        
        app = ProfessionalMainWindow()
        app.run()
        
    except ImportError as e:
        messagebox.showerror(
            "Import Error",
            f"❌ Could not import IRUS components:\n{e}\n\n"
            "Please ensure all files are in the correct location:\n"
            "• gui/professional_ui.py\n"
            "• tools/\n"
            "• All other IRUS files"
        )
    except Exception as e:
        messagebox.showerror(
            "Launch Error",
            f"❌ Error launching IRUS:\n{e}\n\n"
            "Please check the console for more details."
        )

def main():
    """Main launcher function"""
    print("🚀 IRUS V6.0 Launcher Starting...")
    print("=" * 50)
    
    # Check Python version
    compatible, version = check_python_version()
    if not compatible:
        messagebox.showerror(
            "Python Version Error",
            f"❌ Python {version} is not supported.\n\n"
            "IRUS V6.0 requires Python 3.7 or higher.\n"
            "Please upgrade your Python installation."
        )
        return
    
    print(f"✅ Python {version} - Compatible")
    
    # Check dependencies
    missing_required, missing_optional = check_dependencies()
    
    if missing_required:
        messagebox.showerror(
            "Missing Dependencies",
            f"❌ Missing required modules:\n{', '.join(missing_required)}\n\n"
            "Please install Python with tkinter support."
        )
        return
    
    print("✅ Required dependencies - OK")
    
    if missing_optional:
        print(f"⚠️ Optional dependencies missing: {', '.join(missing_optional)}")
        
        install_choice = messagebox.askyesno(
            "Optional Dependencies",
            f"Some optional features require additional modules:\n{', '.join(missing_optional)}\n\n"
            "Install them now for the best experience?\n"
            "(Discord integration, system diagnostics)"
        )
        
        if install_choice:
            print("📦 Installing optional dependencies...")
            if install_dependencies():
                print("✅ Optional dependencies installed")
            else:
                print("⚠️ Some optional dependencies could not be installed")
    else:
        print("✅ Optional dependencies - OK")
    
    # Check if this is first run
    settings_file = os.path.join(os.path.dirname(__file__), 'settings.json')
    first_run = not os.path.exists(settings_file)
    
    if first_run:
        print("🎉 First run detected - showing welcome dialog")
        if not show_welcome_dialog():
            print("👋 User cancelled - exiting")
            return
    
    # Launch IRUS
    print("🚀 Launching IRUS V6.0...")
    launch_irus()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Launcher interrupted by user")
    except Exception as e:
        print(f"\n💥 Launcher error: {e}")
        messagebox.showerror("Launcher Error", f"Unexpected error:\n{e}")
