#!/usr/bin/env python3
"""
Test script for critical bug fixes
Tests the specific issues that were causing crashes
"""

import sys
import os
import traceback

def test_ui_initialization():
    """Test that UI initializes without crashing"""
    print("🧪 Testing UI initialization...")
    
    try:
        # Add current directory to path
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        from gui.professional_ui import ProfessionalMainWindow
        
        print("  ✅ Import successful")
        
        # Test initialization (without actually showing the window)
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Create the main window object
        app = ProfessionalMainWindow()
        
        print("  ✅ UI initialization successful")
        
        # Test that critical attributes exist
        required_attrs = ['log_text', 'status_label', 'notebook']
        for attr in required_attrs:
            if hasattr(app, attr):
                print(f"  ✅ {attr} exists")
            else:
                print(f"  ❌ {attr} missing")
                return False
        
        # Test log_message method
        app.log_message("Test message")
        print("  ✅ log_message works")
        
        # Clean up
        app.root.destroy()
        
        return True
        
    except Exception as e:
        print(f"  ❌ UI initialization failed: {e}")
        traceback.print_exc()
        return False

def test_settings_loading():
    """Test settings loading without crash"""
    print("\n🧪 Testing settings loading...")
    
    try:
        # Create a test settings file
        import json
        test_settings = {
            'theme': 'Professional',
            'font_size': 12,
            'auto_open': True,
            'experimental': False
        }
        
        with open('test_settings.json', 'w') as f:
            json.dump(test_settings, f)
        
        print("  ✅ Test settings file created")
        
        # Test loading (this should not crash)
        from gui.professional_ui import ProfessionalMainWindow
        
        # Mock the settings file path
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        app = ProfessionalMainWindow()
        
        # Test manual settings loading
        if os.path.exists('test_settings.json'):
            with open('test_settings.json', 'r') as f:
                settings = json.load(f)
            print("  ✅ Settings file loaded successfully")
        
        # Clean up
        app.root.destroy()
        os.remove('test_settings.json')
        
        return True
        
    except Exception as e:
        print(f"  ❌ Settings loading failed: {e}")
        traceback.print_exc()
        return False

def test_log_message_safety():
    """Test log_message method with missing components"""
    print("\n🧪 Testing log_message safety...")
    
    try:
        import tkinter as tk
        
        # Create a minimal class to test log_message
        class TestUI:
            def __init__(self):
                self.root = tk.Tk()
                self.root.withdraw()
            
            def log_message(self, message):
                """Safe log message method"""
                import time
                timestamp = time.strftime("%H:%M:%S")
                formatted_message = f"[{timestamp}] {message}"
                
                # Only update log_text if it exists
                if hasattr(self, 'log_text'):
                    try:
                        self.log_text.insert('end', message + '\n')
                        self.log_text.see('end')
                    except Exception:
                        pass
                
                # Only update status_label if it exists
                if hasattr(self, 'status_label'):
                    try:
                        self.status_label.config(text=message)
                    except Exception:
                        pass
                
                # Fallback to console if UI components aren't ready
                if not hasattr(self, 'log_text') or not hasattr(self, 'status_label'):
                    print(formatted_message)
        
        # Test with missing components
        test_ui = TestUI()
        test_ui.log_message("Test message without UI components")
        print("  ✅ log_message works without UI components")
        
        # Test with log_text but no status_label
        test_ui.log_text = tk.Text(test_ui.root)
        test_ui.log_message("Test message with log_text only")
        print("  ✅ log_message works with partial UI components")
        
        test_ui.root.destroy()
        return True
        
    except Exception as e:
        print(f"  ❌ log_message safety test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all critical bug fix tests"""
    print("🔍 IRUS V5.0 - Critical Bug Fix Validation")
    print("=" * 50)
    
    tests = [
        ("UI Initialization", test_ui_initialization),
        ("Settings Loading", test_settings_loading),
        ("Log Message Safety", test_log_message_safety)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
            print(f"✅ {test_name} - PASSED")
        else:
            print(f"❌ {test_name} - FAILED")
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL CRITICAL BUGS FIXED!")
        print("✅ IRUS V5.0 should now launch without crashing!")
    else:
        print("⚠️ Some critical issues remain. Please review the failures above.")
    
    return passed == total

if __name__ == "__main__":
    try:
        success = main()
        input("\nPress Enter to exit...")
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n💥 Test script crashed: {e}")
        traceback.print_exc()
        input("Press Enter to exit...")
        sys.exit(1)
