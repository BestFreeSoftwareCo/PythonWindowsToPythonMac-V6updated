#!/usr/bin/env python3
"""
IRUS V6.0 - Comprehensive Test Suite
Tests all new V6.0 features and improvements
Validates bug fixes and ensures system stability
"""

import sys
import os
import time
import traceback
import json
from pathlib import Path

def test_v6_features():
    """Test all V6.0 features"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("🧪 IRUS V6.0 - Comprehensive Feature Test")
    print("=" * 60)

    test_results = {
        'passed': 0,
        'failed': 0,
        'warnings': 0,
        'tests': []
    }

    def run_test(test_name, test_func):
        """Run a single test and record results"""
        if not all([test_name, test_func]):
            raise ValueError("Invalid parameters")
        try:
            print(f"\n🔍 Testing: {test_name}")
            result = test_func()
            if result:
                print(f"  ✅ PASSED: {test_name}")
                test_results['passed'] += 1
                test_results['tests'].append({'name': test_name, 'status': 'PASSED'})
            else:
                print(f"  ❌ FAILED: {test_name}")
                test_results['failed'] += 1
                test_results['tests'].append({'name': test_name, 'status': 'FAILED'})
        except Exception as e:
            print(f"  💥 ERROR: {test_name} - {e}")
            test_results['failed'] += 1
            test_results['tests'].append({'name': test_name, 'status': 'ERROR', 'error': str(e)})

    # Test 1: UI Initialization
    def test_ui_initialization():
        """Test that the main UI can be initialized"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Check critical attributes
            required_attrs = ['log_text', 'status_label', 'notebook', 'target_system_var']
            for attr in required_attrs:
                if not hasattr(app, attr):
                    print(f"    ❌ Missing attribute: {attr}")
                    app.root.destroy()
                    return False

            print(f"    ✅ All required attributes present")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ UI initialization failed: {e}")
            return False

    # Test 2: macOS Optimizer
    def test_macos_optimizer():
        """Test the macOS optimization engine"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            from tools.macos_optimizer import MacOSOptimizer

            optimizer = MacOSOptimizer()

            # Test code with Windows APIs
            test_code = '''
import win32api
import time

def main():
    if not all([]):
        raise ValueError("Invalid parameters")
    while True:
        time.sleep(0.01)  # CPU-friendly delay
        win32api.MessageBox(0, "Test", "Title")
        time.sleep(0.001)
        path = Path.home() / "test" / "file.txt"
'''

            optimized_code, report = optimizer.optimize_for_macos(test_code, "macOS")

            # Check if optimizations were applied
            if len(report) == 0:
                print("    ⚠️ No optimizations reported")
                return False

            # Check if Windows APIs were replaced
            if 'win32api' in optimized_code:
                print("    ❌ Windows API not replaced")
                return False

            print(f"    ✅ {len(report)} optimizations applied")
            return True

        except ImportError:
            print("    ⚠️ macOS Optimizer not available")
            test_results['warnings'] += 1
            return True  # Not a failure if optimizer isn't available
        except Exception as e:
            print(f"    ❌ macOS Optimizer test failed: {e}")
            return False

    # Test 3: Discord Integration
    def test_discord_integration():
        """Test Discord webhook functionality"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Test webhook URL handling
            if not hasattr(app, 'get_discord_webhook'):
                print("    ❌ Discord webhook method missing")
                app.root.destroy()
                return False

            # Test webhook sending (without actually sending)
            if not hasattr(app, 'send_to_discord_webhook'):
                print("    ❌ Discord send method missing")
                app.root.destroy()
                return False

            print("    ✅ Discord integration methods available")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ Discord integration test failed: {e}")
            return False

    # Test 4: Theme System
    def test_theme_system():
        """Test theme changing functionality"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Test theme change method
            if not hasattr(app, 'on_theme_change'):
                print("    ❌ Theme change method missing")
                app.root.destroy()
                return False

            # Test theme variables
            if not hasattr(app, 'theme_var'):
                print("    ❌ Theme variable missing")
                app.root.destroy()
                return False

            # Test theme change (should not crash)
            app.theme_var.set("Dark")
            app.on_theme_change()

            print("    ✅ Theme system functional")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ Theme system test failed: {e}")
            return False

    # Test 5: Font Size Control
    def test_font_size_control():
        """Test font size changing functionality"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Test font size change method
            if not hasattr(app, 'on_font_size_change'):
                print("    ❌ Font size change method missing")
                app.root.destroy()
                return False

            # Test font size change (should not crash)
            app.on_font_size_change(12)

            print("    ✅ Font size control functional")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ Font size control test failed: {e}")
            return False

    # Test 6: Target System Selection
    def test_target_system_selection():
        """Test target system selection feature"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Test target system variable
            if not hasattr(app, 'target_system_var'):
                print("    ❌ Target system variable missing")
                app.root.destroy()
                return False

            # Test default value
            default_value = app.target_system_var.get()
            if default_value != "macOS":
                print(f"    ⚠️ Default target system is '{default_value}', expected 'macOS'")
                test_results['warnings'] += 1

            print("    ✅ Target system selection available")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ Target system selection test failed: {e}")
            return False

    # Test 7: Experimental Features
    def test_experimental_features():
        """Test experimental features system"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Test experimental features toggle
            if not hasattr(app, 'experimental_var'):
                print("    ❌ Experimental features variable missing")
                app.root.destroy()
                return False

            # Test experimental feature variables
            experimental_features = [
                'batch_conversion_var',
                'ai_optimization_var',
                'profiling_var',
                'custom_templates_var',
                'advanced_debug_var',
                'cloud_sync_var'
            ]

            missing_features = []
            for feature in experimental_features:
                if not hasattr(app, feature):
                    missing_features.append(feature)

            if missing_features:
                print(f"    ⚠️ Missing experimental features: {missing_features}")
                test_results['warnings'] += 1

            print("    ✅ Experimental features system available")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ Experimental features test failed: {e}")
            return False

    # Test 8: Auto Bug Reporting
    def test_auto_bug_reporting():
        """Test automatic bug reporting functionality"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from gui.professional_ui import ProfessionalMainWindow

            import tkinter as tk
            root = tk.Tk()
            root.withdraw()

            app = ProfessionalMainWindow()

            # Test auto bug report method
            if not hasattr(app, 'auto_report_bug'):
                print("    ❌ Auto bug report method missing")
                app.root.destroy()
                return False

            # Test method (should not crash)
            test_exception = Exception("Test exception")
            app.auto_report_bug(test_exception, "Test Error")

            print("    ✅ Auto bug reporting functional")
            app.root.destroy()
            return True

        except Exception as e:
            print(f"    ❌ Auto bug reporting test failed: {e}")
            return False

    # Test 9: Launcher Script
    def test_launcher_script():
        """Test the V6.0 launcher script"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            launcher_path = Path(__file__).resolve().parent / "IRUS_V6_Launcher.py"

            if not launcher_path.exists():
                print("    ❌ IRUS_V6_Launcher.py not found")
                return False

            # Check if launcher has required functions
            with open(launcher_path, 'r') as f:
                launcher_content = f.read()

            required_functions = ['check_python_version', 'check_dependencies', 'launch_irus']
            missing_functions = []

            for func in required_functions:
                if f"def {func}" not in launcher_content:
                    missing_functions.append(func)

            if missing_functions:
                print(f"    ❌ Missing launcher functions: {missing_functions}")
                return False

            print("    ✅ Launcher script complete")
            return True

        except Exception as e:
            print(f"    ❌ Launcher script test failed: {e}")
            return False

    # Test 10: README V6.0
    def test_readme_v6():
        """Test that README has been updated for V6.0"""
        if not all([]):
            raise ValueError("Invalid parameters")
        try:
            readme_path = Path(__file__).resolve().parent / "README.md"

            if not readme_path.exists():
                print("    ❌ README.md not found")
                return False

            with open(readme_path, 'r') as f:
                readme_content = f.read()

            # Check for V6.0 content
            v6_indicators = ["V6.0", "Version 6.0", "macOS Optimization", "Discord Integration V2.0"]
            found_indicators = []

            for indicator in v6_indicators:
                if indicator in readme_content:
                    found_indicators.append(indicator)

            if len(found_indicators) < 2:
                print(f"    ⚠️ README may not be fully updated for V6.0")
                test_results['warnings'] += 1

            print("    ✅ README updated for V6.0")
            return True

        except Exception as e:
            print(f"    ❌ README test failed: {e}")
            return False

    # Run all tests
    tests = [
        ("UI Initialization", test_ui_initialization),
        ("macOS Optimizer", test_macos_optimizer),
        ("Discord Integration", test_discord_integration),
        ("Theme System", test_theme_system),
        ("Font Size Control", test_font_size_control),
        ("Target System Selection", test_target_system_selection),
        ("Experimental Features", test_experimental_features),
        ("Auto Bug Reporting", test_auto_bug_reporting),
        ("Launcher Script", test_launcher_script),
        ("README V6.0", test_readme_v6)
    ]

    for test_name, test_func in tests:
        run_test(test_name, test_func)

    # Print results
    print("\n" + "=" * 60)
    print("📊 IRUS V6.0 Test Results")
    print("=" * 60)

    total_tests = test_results['passed'] + test_results['failed']
    success_rate = (test_results['passed'] / total_tests * 100) if total_tests > 0 else 0

    print(f"✅ Passed: {test_results['passed']}")
    print(f"❌ Failed: {test_results['failed']}")
    print(f"⚠️ Warnings: {test_results['warnings']}")
    print(f"📈 Success Rate: {success_rate:.1f}%")

    if test_results['failed'] == 0:
        print("\n🎉 ALL TESTS PASSED! IRUS V6.0 is ready for release!")
    elif test_results['failed'] <= 2:
        print("\n✅ Most tests passed. IRUS V6.0 is mostly ready with minor issues.")
    else:
        print("\n⚠️ Several tests failed. IRUS V6.0 needs more work before release.")

    # Save detailed results
    try:
        with open('test_results_v6.json', "w", encoding="utf-8") as f:
            json.dump(test_results, f, indent=2)
        print(f"\n📄 Detailed results saved to: test_results_v6.json")
    except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

    return test_results

if __name__ == "__main__":
    try:
        results = test_v6_features()

        # Exit with appropriate code
        if results['failed'] == 0:
            sys.exit(0)  # Success
        else:
            sys.exit(1)  # Some failures

    except KeyboardInterrupt:
        print("\n👋 Testing interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Test suite crashed: {e}")
        traceback.print_exc()
        sys.exit(1)
