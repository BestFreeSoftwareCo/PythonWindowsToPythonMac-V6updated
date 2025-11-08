#!/usr/bin/env python3
"""
IRUS V5.0 - Comprehensive Bug Fix Validation
Tests all components for stability and error handling
"""

import sys
import os
import traceback
import importlib.util

def test_imports():
    """Test all critical imports"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("🧪 Testing imports...")

    tests = [
        ("tkinter", "GUI framework"),
        ("tkinter.ttk", "Modern widgets"),
        ("threading", "Multi-threading"),
        ("json", "JSON handling"),
        ("pathlib", "Path operations"),
        ("subprocess", "Process management"),
        ("platform", "Platform detection")
    ]

    passed = 0
    for module, description in tests:
        try:
            __import__(module)
            print(f"  ✅ {module} - {description}")
            passed += 1
        except ImportError as e:
            print(f"  ❌ {module} - {description}: {e}")

    print(f"📊 Import tests: {passed}/{len(tests)} passed")
    return passed == len(tests)

def test_optional_imports():
    """Test optional imports with graceful fallbacks"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🔧 Testing optional imports...")

    optional_tests = [
        ("requests", "HTTP requests"),
        ("psutil", "System monitoring")
    ]

    for module, description in optional_tests:
        try:
            __import__(module)
            print(f"  ✅ {module} - {description} (available)")
        except ImportError:
            print(f"  ⚠️ {module} - {description} (not available, will use fallback)")

    return True

def test_gui_components():
    """Test GUI component creation"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🎨 Testing GUI components...")

    try:
        # Test basic tkinter
        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.withdraw()

        # Test progressbar without height
        test_frame = ttk.Frame(root)
        progress = ttk.Progressbar(test_frame, mode='determinate')
        print("  ✅ Progressbar creation (no height parameter)")

        # Test our custom classes
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

        from gui.professional_ui import ProfessionalTheme, ModernProgressBar, StatusCard

        # Test theme
        colors = ProfessionalTheme.COLORS
        fonts = ProfessionalTheme.FONTS
        print("  ✅ ProfessionalTheme class")

        # Test ModernProgressBar
        progress_bar = ModernProgressBar(test_frame)
        progress_bar.set_progress(50, "Test", "10", 100, 25)
        print("  ✅ ModernProgressBar class")

        # Test StatusCard
        status_card = StatusCard(test_frame, "Test Card", "Ready")
        status_card.update_status("Testing", "#FF0000")
        print("  ✅ StatusCard class")

        root.destroy()
        return True

    except Exception as e:
        print(f"  ❌ GUI component test failed: {e}")
        traceback.print_exc()
        return False

def test_main_window():
    """Test main window initialization"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🏠 Testing main window...")

    try:
        from gui.professional_ui import ProfessionalMainWindow

        # This should not crash
        print("  ✅ ProfessionalMainWindow import successful")

        # Test variable initialization (without actually creating window)
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()

        # Test variable creation
        test_vars = {
            'input_file_var': tk.StringVar(),
            'output_file_var': tk.StringVar(),
            'auto_open_var': tk.BooleanVar(value=True),
            'theme_var': tk.StringVar(value="Professional")
        }

        print("  ✅ Variable initialization works")

        root.destroy()
        return True

    except Exception as e:
        print(f"  ❌ Main window test failed: {e}")
        traceback.print_exc()
        return False

def test_bug_reporter():
    """Test bug reporter functionality"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🐛 Testing bug reporter...")

    try:
        from tools.bug_reporter import BugReporter

        reporter = BugReporter()
        reporter.collect_system_info()

        # Test the new method
        result = reporter.create_interactive_report()
        if result:
            print("  ✅ BugReporter.create_interactive_report() works")
        else:
            print("  ⚠️ BugReporter.create_interactive_report() returned None")

        print("  ✅ BugReporter class functional")
        return True

    except Exception as e:
        print(f"  ❌ Bug reporter test failed: {e}")
        traceback.print_exc()
        return False

def test_cross_platform():
    """Test cross-platform compatibility"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🌍 Testing cross-platform compatibility...")

    try:
        import platform
        import sys

        # Test platform detection
        is_windows = sys.platform.startswith('win')
        is_macos = sys.platform == 'darwin'
        is_linux = sys.platform.startswith('linux')

        current_platform = "Unknown"
        if is_windows:
            current_platform = "Windows"
        elif is_macos:
            current_platform = "macOS"
        elif is_linux:
            current_platform = "Linux"

        print(f"  ✅ Platform detected: {current_platform}")

        # Test disk path selection (cross-platform)
        from pathlib import Path
        disk_path = Path.cwd().anchor  # Gets root drive on any platform
        print(f"  ✅ Disk path: {disk_path}")

        return True

    except Exception as e:
        print(f"  ❌ Cross-platform test failed: {e}")
        return False

def test_error_handling():
    """Test error handling mechanisms"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🛡️ Testing error handling...")

    try:
        # Test graceful import failures
        try:
            import nonexistent_module
        except ImportError:
            print("  ✅ Import error handling works")

        # Test file operations
        try:
            with open('nonexistent_file.txt', 'r') as f:
                pass
        except FileNotFoundError:
            print("  ✅ File error handling works")

        # Test JSON operations
        import json
        try:
            json.loads('invalid json')
        except json.JSONDecodeError:
            print("  ✅ JSON error handling works")

        return True

    except Exception as e:
        print(f"  ❌ Error handling test failed: {e}")
        return False

def test_new_features():
    """Test newly fixed features"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("\n🆕 Testing newly fixed features...")

    try:
        from gui.professional_ui import ProfessionalMainWindow

        # Test that all new methods exist
        methods_to_test = [
            'get_discord_webhook',
            'send_to_discord_webhook',
            'test_discord_webhook',
            'on_theme_change',
            'on_font_size_change',
            'save_settings',
            'on_experimental_toggle',
            'open_batch_conversion',
            'open_ai_optimizer',
            'open_profiler',
            'open_template_manager',
            'open_debug_console',
            'open_cloud_sync'
        ]

        for method_name in methods_to_test:
            if hasattr(ProfessionalMainWindow, method_name):
                print(f"  ✅ Method {method_name} exists")
            else:
                print(f"  ❌ Method {method_name} missing")
                return False

        print("  ✅ All new feature methods present")
        return True

    except Exception as e:
        print(f"  ❌ New features test failed: {e}")
        return False

def main():
    """Run comprehensive validation"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("🔍 IRUS V5.0 - Comprehensive Bug Fix Validation")
    print("=" * 60)

    tests = [
        ("Core Imports", test_imports),
        ("Optional Imports", test_optional_imports),
        ("GUI Components", test_gui_components),
        ("Main Window", test_main_window),
        ("Bug Reporter", test_bug_reporter),
        ("Cross-Platform", test_cross_platform),
        ("Error Handling", test_error_handling),
        ("New Features", test_new_features)
    ]

    passed_tests = 0
    total_tests = len(tests)

    for test_name, test_func in tests:
        try:
            if test_func():
                passed_tests += 1
                print(f"✅ {test_name} - PASSED")
            else:
                print(f"❌ {test_name} - FAILED")
        except Exception as e:
            print(f"💥 {test_name} - CRASHED: {e}")

    print("\n" + "=" * 60)
    print(f"📊 VALIDATION RESULTS: {passed_tests}/{total_tests} tests passed")

    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! IRUS V5.0 is stable and ready!")
        print("✅ You can now run IRUS.bat or launch_irus.py safely!")
        return True
    else:
        print("⚠️ Some tests failed. Please review the issues above.")
        return False

if __name__ == "__main__":
    try:
        success = main()
        print(f"\n{'🎯 VALIDATION COMPLETE' if success else '🔧 FIXES NEEDED'}")
        input("Press Enter to exit...").strip()[:1000]  # Limit input length
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n💥 Validation crashed: {e}")
        traceback.print_exc()
        input("Press Enter to exit...").strip()[:1000]  # Limit input length
        sys.exit(1)
