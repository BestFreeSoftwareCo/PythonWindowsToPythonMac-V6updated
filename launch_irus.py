#!/usr/bin/env python3
"""
IRUS V5.0 - Main Launcher
Cross-platform launcher with comprehensive error handling
"""

import sys
import os
import traceback
import tkinter as tk
from tkinter import messagebox

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True

def check_tkinter():
    """Check if tkinter is available"""
    try:
        import tkinter
        # Test basic tkinter functionality
        root = tkinter.Tk()
        root.withdraw()  # Hide the test window
        root.destroy()
        return True
    except ImportError:
        print("❌ tkinter is not available")
        print("Please install tkinter:")
        if sys.platform.startswith('win'):
            print("  - Reinstall Python with tkinter support")
        elif sys.platform == 'darwin':
            print("  - brew install python-tk")
        else:
            print("  - sudo apt-get install python3-tk")
        return False
    except Exception as e:
        print(f"❌ tkinter test failed: {e}")
        return False

def setup_environment():
    """Setup the environment for IRUS"""
    
    # Add current directory to Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    # Create necessary directories
    directories = ['output', 'config', 'logs', 'feedback', 'bug_reports']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Set up logging
    log_file = os.path.join('logs', 'irus.log')
    
    return True

def show_error_dialog(title, message, details=None):
    """Show error dialog with optional details"""
    try:
        root = tk.Tk()
        root.withdraw()
        
        if details:
            full_message = f"{message}\n\nDetails:\n{details}"
        else:
            full_message = message
        
        messagebox.showerror(title, full_message)
        root.destroy()
    except Exception as e:
        # Fallback to console output
        print(f"❌ {title}: {message}")
        if details:
            print(f"Details: {details}")
        print(f"GUI Error: {e}")

def launch_irus():
    """Launch the IRUS application"""
    
    print("🚀 Starting IRUS V5.0...")
    print("=" * 50)
    
    # Check system requirements
    print("🔍 Checking system requirements...")
    
    if not check_python_version():
        show_error_dialog(
            "Python Version Error",
            "IRUS requires Python 3.7 or higher.\n\nPlease update your Python installation."
        )
        return False
    
    if not check_tkinter():
        show_error_dialog(
            "tkinter Not Available",
            "IRUS requires tkinter for the graphical interface.\n\nPlease install tkinter support."
        )
        return False
    
    print("✅ System requirements met")
    
    # Setup environment
    print("🔧 Setting up environment...")
    if not setup_environment():
        show_error_dialog(
            "Environment Setup Error",
            "Failed to setup IRUS environment.\n\nCheck file permissions and try again."
        )
        return False
    
    print("✅ Environment ready")
    
    # Import and launch the main application
    try:
        print("📱 Loading IRUS interface...")
        
        # Import the main UI
        from gui.professional_ui import ProfessionalMainWindow
        
        print("✅ IRUS loaded successfully")
        print("🎯 Launching interface...")
        
        # Create and run the application
        app = ProfessionalMainWindow()
        
        print("🎉 IRUS V5.0 is now running!")
        print("💡 Close this console window to exit IRUS")
        
        # Start the main loop
        app.run()
        
        print("👋 IRUS closed successfully")
        return True
        
    except ImportError as e:
        error_msg = f"Failed to import IRUS components: {str(e)}"
        details = traceback.format_exc()
        
        print(f"❌ {error_msg}")
        print("🔧 Traceback:")
        print(details)
        
        show_error_dialog(
            "Import Error",
            f"{error_msg}\n\nThis usually means some files are missing or corrupted.",
            details
        )
        return False
        
    except Exception as e:
        error_msg = f"Unexpected error launching IRUS: {str(e)}"
        details = traceback.format_exc()
        
        print(f"❌ {error_msg}")
        print("🔧 Traceback:")
        print(details)
        
        show_error_dialog(
            "IRUS Launch Error",
            f"{error_msg}\n\nPlease report this bug to the developer.",
            details
        )
        return False

def main():
    """Main entry point"""
    
    try:
        # Change to script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        # Launch IRUS
        success = launch_irus()
        
        if not success:
            print("\n❌ IRUS failed to start")
            print("💡 Please check the error messages above")
            input("Press Enter to exit...")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n👋 IRUS startup cancelled by user")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n💥 Critical error: {e}")
        print("🔧 Traceback:")
        traceback.print_exc()
        
        show_error_dialog(
            "Critical Error",
            f"A critical error occurred:\n\n{str(e)}\n\nIRUS cannot start.",
            traceback.format_exc()
        )
        
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
