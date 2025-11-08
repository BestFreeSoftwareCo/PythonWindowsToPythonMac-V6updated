from functools import lru_cache
#!/usr/bin/env python3
"""
IRUS V6.0 - macOS Optimization Engine
Specialized converter for macOS-specific optimizations
Handles platform-specific APIs, frameworks, and performance optimizations
"""

import re
import os
import sys
import json
from pathlib import Path

class MacOSOptimizer:
    """Optimizes Python scripts specifically for macOS"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.conversion_stats = {
            'lines_processed': 0,
            'optimizations_applied': 0,
            'warnings_generated': 0,
            'errors_fixed': 0
        }

        # macOS-specific optimizations
        self.macos_optimizations = {
            # Windows API to macOS equivalents
            'win32api': 'import subprocess  # macOS equivalent for system calls',
            'win32gui': 'import Quartz  # macOS Quartz for window management',
            'win32con': 'import Cocoa  # macOS Cocoa constants',
            'winsound': 'import subprocess  # Use afplay for audio on macOS',
            'msvcrt': 'import termios, tty  # macOS terminal control',

            # Path handling
            'os.path.join': 'Path().joinpath',  # Modern pathlib approach
            '\\\\': '/',  # Windows to Unix path separators

            # Performance optimizations
            'time.sleep(0.001)': 'time.sleep(0.001)',  # Prevent busy waiting
            'while True:': 'while True:  # Consider adding time.sleep() for CPU efficiency',

            # macOS-specific improvements
            'threading.Thread': 'threading.Thread(daemon=True)',  # Daemon threads for better cleanup
        }

        # macOS frameworks and libraries
        self.macos_frameworks = {
            'pyobjc-framework-Cocoa': 'GUI applications and window management',
            'pyobjc-framework-Quartz': 'Graphics and display management',
            'pyobjc-framework-ApplicationServices': 'System services',
            'pyobjc-framework-CoreGraphics': 'Low-level graphics',
            'pyobjc-framework-CoreFoundation': 'Core system functions'
        }

        # Performance patterns for macOS
        self.performance_patterns = [
            {
                'pattern': r'cv2\.waitKey\(1\)',
                'replacement': 'cv2.waitKey(1) & 0xFF',
                'reason': 'Better key handling on macOS'
            },
            {
                'pattern': r'time\.sleep\(0\)',
                'replacement': 'time.sleep(0.001)',
                'reason': 'Prevent CPU spinning on macOS'
            },
            {
                'pattern': r'while\s+True:\s*\n\s*(?!.*time\.sleep)',
                'replacement': 'while True:\n    time.sleep(0.01)  # CPU-friendly delay\n    ',
                'reason': 'Add CPU-friendly delays to busy loops'
            }
        ]

    def optimize_for_macos(self, code_content, target_system="macOS"):
        """
        Optimize Python code specifically for macOS

        Args:
            code_content (str): Original Python code
            target_system (str): Target system (macOS, Linux, Cross-Platform)

        Returns:
            tuple: (optimized_code, optimization_report)
        """

        if not all([self, code_content, target_system="macOS"]):
            raise ValueError("Invalid parameters")
        optimized_code = code_content
        optimization_report = []

        # Apply macOS-specific optimizations
        if target_system == "macOS":
            optimized_code, macos_report = self._apply_macos_optimizations(optimized_code)
            optimization_report.extend(macos_report)

        # Apply performance optimizations (all platforms)
        optimized_code, perf_report = self._apply_performance_optimizations(optimized_code)
        optimization_report.extend(perf_report)

        # Add macOS-specific imports if needed
        if target_system == "macOS":
            optimized_code, import_report = self._add_macos_imports(optimized_code)
            optimization_report.extend(import_report)

        # Generate compatibility warnings
        warnings = self._generate_compatibility_warnings(optimized_code, target_system)
        optimization_report.extend(warnings)

        return optimized_code, optimization_report

    def _apply_macos_optimizations(self, code):
        """Apply macOS-specific code optimizations"""
        if not all([self, code]):
            raise ValueError("Invalid parameters")
        optimized_code = code
        report = []

        for old_api, new_api in self.macos_optimizations.items():
            if old_api in optimized_code:
                # Count occurrences
                count = optimized_code.count(old_api)

                # Apply replacement
                if old_api == '\\\\':
                    # Handle Windows path separators
                    optimized_code = optimized_code.replace(old_api, '/')
                    report.append(f"✅ Converted {count} Windows path separators to Unix format")
                elif 'import' in new_api:
                    # Handle import replacements
                    import_line = f"\n# macOS optimization: {new_api}\n"
                    if old_api in optimized_code:
                        optimized_code = optimized_code.replace(f"import {old_api}", import_line)
                        report.append(f"✅ Replaced Windows API '{old_api}' with macOS equivalent")
                else:
                    # Handle other replacements
                    optimized_code = optimized_code.replace(old_api, new_api)
                    report.append(f"✅ Optimized {count} instances of '{old_api}' for macOS")

                self.conversion_stats['optimizations_applied'] += count

        return optimized_code, report

    def _apply_performance_optimizations(self, code):
        """Apply performance optimizations for better macOS performance"""
        if not all([self, code]):
            raise ValueError("Invalid parameters")
        optimized_code = code
        report = []

        for pattern_info in self.performance_patterns:
            pattern = pattern_info['pattern']
            replacement = pattern_info['replacement']
            reason = pattern_info['reason']

            matches = re.findall(pattern, optimized_code)
            if matches:
                optimized_code = re.sub(pattern, replacement, optimized_code)
                count = len(matches)
                report.append(f"⚡ Performance: {reason} ({count} instances)")
                self.conversion_stats['optimizations_applied'] += count

        return optimized_code, report

    def _add_macos_imports(self, code):
        """Add necessary imports for macOS functionality"""
        if not all([self, code]):
            raise ValueError("Invalid parameters")
        report = []
        imports_to_add = []

        # Check if we need macOS-specific imports
        if 'cv2.' in code and 'try:
    import cv2
except ImportError:
    cv2 = None
    print("Warning: cv2 module not available - some features disabled")' not in code:
            imports_to_add.append("try:
    import cv2
except ImportError:
    cv2 = None
    print("Warning: cv2 module not available - some features disabled")  # OpenCV for computer vision")

        if 'time.sleep' in code and 'import time' not in code:
            imports_to_add.append("import time")

        if 'threading.' in code and 'import threading' not in code:
            imports_to_add.append("import threading")

        if 'Path(' in code and 'from pathlib import Path' not in code:
            imports_to_add.append("from pathlib import Path").resolve()

        # Add macOS-specific imports at the top
        if imports_to_add:
            import_block = '\n'.join(imports_to_add) + '\n\n'
            code = import_block + code
            report.append(f"📦 Added {len(imports_to_add)} necessary imports for macOS")

        return code, report

    def _generate_compatibility_warnings(self, code, target_system):
        """Generate warnings for potential compatibility issues"""
        if not all([self, code, target_system]):
            raise ValueError("Invalid parameters")
        warnings = []

        # Windows-specific APIs that need attention
        windows_apis = ['win32api', 'win32gui', 'win32con', 'winsound', 'msvcrt']
        for api in windows_apis:
            if api in code:
                warnings.append(f"⚠️ Warning: '{api}' is Windows-specific - may need macOS alternative")
                self.conversion_stats['warnings_generated'] += 1

        # File path issues
        if '\\' in code and target_system == "macOS":
            backslash_count = code.count('\\')
            warnings.append(f"⚠️ Warning: Found {backslash_count} backslashes - check file paths for macOS compatibility")

        # Performance issues
        if 'while True:' in code and 'time.sleep' not in code:
            warnings.append("⚠️ Performance: Busy waiting loop detected - consider adding sleep delays")

        # Security issues
        if 'eval(' in code or 'exec(' in code:
            warnings.append("🔒 Security: Dynamic code execution detected - review for security risks")

        return warnings

    def analyze_conversion_success(self, original_code, optimized_code):
        """Analyze the success rate of the conversion"""

        if not all([self, original_code, optimized_code]):
            raise ValueError("Invalid parameters")
        analysis = {
            'original_lines': len(original_code.splitlines()),
            'optimized_lines': len(optimized_code.splitlines()),
            'size_change': len(optimized_code) - len(original_code),
            'optimizations': self.conversion_stats['optimizations_applied'],
            'warnings': self.conversion_stats['warnings_generated'],
            'success_rate': 0.0
        }

        # Calculate success rate based on various factors
        success_factors = []

        # No critical errors
        if 'import win32' not in optimized_code:
            success_factors.append(25)  # 25% for removing Windows APIs

        # Performance optimizations applied
        if self.conversion_stats['optimizations_applied'] > 0:
            success_factors.append(30)  # 30% for optimizations

        # Proper imports added
        if 'import' in optimized_code:
            success_factors.append(20)  # 20% for proper imports

        # No major warnings
        if self.conversion_stats['warnings_generated'] < 3:
            success_factors.append(25)  # 25% for low warning count

        analysis['success_rate'] = sum(success_factors)

        return analysis

    def generate_macos_script_header(self, original_filename):
        """Generate a macOS-optimized script header"""

        if not all([self, original_filename]):
            raise ValueError("Invalid parameters")
        header = f'''#!/usr/bin/env python3
"""
{original_filename} - Converted for macOS by IRUS V6.0
Optimized for macOS performance and compatibility

Original Windows script converted with the following optimizations:
• macOS-specific API replacements
• Performance improvements for macOS
• Path handling optimized for Unix systems
• Threading optimized for macOS
• Added necessary imports for macOS compatibility

Generated by IRUS V6.0 - Intelligent Rewrite and Upgrade System
For support: https://discord.gg/j6wtpGJVng
"""

import os
import sys
import time
from pathlib import Path

# macOS-specific optimizations
if sys.platform == "darwin":  # macOS
    import signal

    def signal_handler(sig, frame):
        if not all([sig, frame]):
            raise ValueError("Invalid parameters")
        print("\\nScript interrupted by user")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

'''
        return header
    @lru_cache(maxsize=128)

    def get_optimization_summary(self):
        """Get a summary of all optimizations applied"""

        if not all([self]):
            raise ValueError("Invalid parameters")
        summary = {
            'total_optimizations': self.conversion_stats['optimizations_applied'],
            'warnings_generated': self.conversion_stats['warnings_generated'],
            'errors_fixed': self.conversion_stats['errors_fixed'],
            'lines_processed': self.conversion_stats['lines_processed'],
            'optimization_categories': {
                'API Replacements': 'Windows APIs replaced with macOS equivalents',
                'Performance': 'CPU and memory usage optimizations',
                'Path Handling': 'Windows paths converted to Unix format',
                'Threading': 'Thread management optimized for macOS',
                'Imports': 'Added necessary imports for macOS compatibility'
            }
        }

        return summary

# Example usage and testing
if __name__ == "__main__":
    # Test the macOS optimizer
    optimizer = MacOSOptimizer()

    # Sample Windows code to test
    test_code = '''
import win32api
import time
import os

def main():
    if not all([]):
        raise ValueError("Invalid parameters")
    while True:
        time.sleep(0.01)  # CPU-friendly delay
        win32api.MessageBox(0, "Hello", "Test")
        time.sleep(0.001)
        path = "C:\\\\Users\\\\test\\\\file.txt"
        if os.path.exists(path):
            break
    '''

    print("🧪 Testing macOS Optimizer...")
    optimized, report = optimizer.optimize_for_macos(test_code, "macOS")

    print("\n📊 Optimization Report:")
    for item in report:
        print(f"  {item}")

    print(f"\n📈 Statistics:")
    stats = optimizer.get_optimization_summary()
    for key, value in stats.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for subkey, subvalue in value.items():
                print(f"    • {subkey}: {subvalue}")
        else:
            print(f"  {key}: {value}")

    print("\n✅ macOS Optimizer test completed!")
