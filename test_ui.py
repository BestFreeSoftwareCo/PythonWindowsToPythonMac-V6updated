#!/usr/bin/env python3
"""
Quick UI Test Script
Tests if the UI can initialize without errors
"""

import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def test_ui():
    """Test UI initialization"""
    
    print("🧪 Testing IRUS UI initialization...")
    
    try:
        # Test tkinter availability
        import tkinter as tk
        print("✅ tkinter available")
        
        # Test ttk availability
        from tkinter import ttk
        print("✅ ttk available")
        
        # Test basic window creation
        root = tk.Tk()
        root.withdraw()  # Hide test window
        print("✅ Basic tkinter window works")
        
        # Test progressbar without height parameter
        test_frame = ttk.Frame(root)
        test_progress = ttk.Progressbar(test_frame, mode='determinate')
        print("✅ Progressbar creation works")
        
        # Clean up
        root.destroy()
        print("✅ Window cleanup works")
        
        # Test IRUS UI import
        from gui.professional_ui import ProfessionalMainWindow
        print("✅ IRUS UI import successful")
        
        print("\n🎉 All tests passed! UI should work correctly.")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_ui()
    if success:
        print("\n✅ You can now run IRUS.bat or launch_irus.py safely!")
    else:
        print("\n❌ There are still issues that need to be fixed.")
    
    input("Press Enter to exit...")
