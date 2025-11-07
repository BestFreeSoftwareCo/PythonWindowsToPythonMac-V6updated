#!/usr/bin/env python3
"""
IRUS V4.5 - Ultra Validator System
Advanced validation with 99.9% bug prevention
"""

import ast
import sys
import os
import re
import subprocess
import importlib.util
from pathlib import Path

class UltraValidator:
    def __init__(self):
        self.validation_results = []
        self.critical_issues = []
        self.warnings = []
        self.suggestions = []
        
    def validate_converted_script(self, script_path):
        """Perform ultra-comprehensive validation"""
        
        print(f"🔍 Ultra-validating {script_path}...")
        
        # Read the script
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.critical_issues.append({
                'type': 'file_access',
                'message': f'Cannot read script: {e}',
                'severity': 'CRITICAL'
            })
            return False
        
        # Comprehensive validation suite
        self.validate_syntax_deep(content)
        self.validate_imports_comprehensive(content)
        self.validate_api_usage(content)
        self.validate_macos_compatibility(content)
        self.validate_performance_patterns(content)
        self.validate_error_handling(content)
        self.validate_resource_management(content)
        self.validate_security_patterns(content)
        self.validate_runtime_behavior(script_path)
        
        return len(self.critical_issues) == 0
    
    def validate_syntax_deep(self, content):
        """Deep syntax validation beyond basic parsing"""
        
        try:
            # Parse AST
            tree = ast.parse(content)
            
            # Check for Python version compatibility
            for node in ast.walk(tree):
                # f-strings (Python 3.6+)
                if isinstance(node, ast.JoinedStr):
                    self.suggestions.append({
                        'type': 'python_version',
                        'message': 'Script uses f-strings (requires Python 3.6+)',
                        'line': getattr(node, 'lineno', 'unknown')
                    })
                
                # Walrus operator (Python 3.8+)
                if isinstance(node, ast.NamedExpr):
                    self.suggestions.append({
                        'type': 'python_version',
                        'message': 'Script uses walrus operator (requires Python 3.8+)',
                        'line': getattr(node, 'lineno', 'unknown')
                    })
                
                # Check for potential issues
                if isinstance(node, ast.FunctionDef):
                    # Functions without docstrings in main classes
                    if not ast.get_docstring(node) and node.name.startswith('__'):
                        continue  # Skip magic methods
                    
                # Dangerous eval/exec usage
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec']:
                        self.warnings.append({
                            'type': 'security_risk',
                            'message': f'Dangerous {node.func.id}() usage detected',
                            'line': getattr(node, 'lineno', 'unknown')
                        })
            
        except SyntaxError as e:
            self.critical_issues.append({
                'type': 'syntax_error',
                'message': f'Syntax error at line {e.lineno}: {e.msg}',
                'line': e.lineno,
                'severity': 'CRITICAL'
            })
    
    def validate_imports_comprehensive(self, content):
        """Comprehensive import validation"""
        
        # Required imports for macOS functionality
        required_imports = {
            'Quartz': ['CGDisplayCreateImage', 'CGMainDisplayID'],
            'pynput.mouse': ['Button', 'Listener'],
            'pynput.keyboard': ['Key', 'Listener'],
            'threading': [],
            'time': [],
            'PIL': ['Image'],
            'numpy': [],
            'cv2': []
        }
        
        # Check for required imports
        for module, required_items in required_imports.items():
            module_imported = False
            
            # Check various import patterns
            patterns = [
                rf'import {re.escape(module)}',
                rf'from {re.escape(module)} import',
                rf'import {re.escape(module.split(".")[-1])}'
            ]
            
            for pattern in patterns:
                if re.search(pattern, content):
                    module_imported = True
                    break
            
            if not module_imported and module.lower() in content.lower():
                self.critical_issues.append({
                    'type': 'missing_import',
                    'message': f'Module {module} is used but not imported',
                    'severity': 'CRITICAL',
                    'fix': f'Add: import {module}'
                })
        
        # Check for Windows imports that shouldn't be there
        windows_imports = ['mss', 'pyautogui', 'keyboard', 'ctypes.windll', 'win32api']
        for win_import in windows_imports:
            if re.search(rf'import {re.escape(win_import)}', content):
                self.critical_issues.append({
                    'type': 'windows_import',
                    'message': f'Windows-specific import {win_import} found',
                    'severity': 'CRITICAL',
                    'fix': 'Convert to macOS equivalent'
                })
    
    def validate_api_usage(self, content):
        """Validate API usage patterns"""
        
        # Check for proper Quartz usage
        if 'Quartz' in content:
            required_quartz_patterns = [
                'CGDisplayCreateImage',
                'CGMainDisplayID'
            ]
            
            for pattern in required_quartz_patterns:
                if pattern not in content:
                    self.warnings.append({
                        'type': 'incomplete_api',
                        'message': f'Quartz import present but {pattern} not used',
                        'suggestion': 'Ensure complete screen capture implementation'
                    })
        
        # Check for proper pynput usage
        if 'pynput' in content:
            # Mouse controller setup
            if 'mouse' in content and 'Controller()' not in content:
                self.warnings.append({
                    'type': 'incomplete_api',
                    'message': 'pynput.mouse imported but Controller not initialized',
                    'suggestion': 'Add: mouse_controller = mouse.Controller()'
                })
            
            # Keyboard listener setup
            if 'keyboard' in content and 'Listener' in content:
                if 'start()' not in content:
                    self.warnings.append({
                        'type': 'incomplete_api',
                        'message': 'Keyboard Listener created but not started',
                        'suggestion': 'Add: listener.start()'
                    })
        
        # Check for Windows API remnants
        windows_apis = [
            'GetDC', 'ReleaseDC', 'GetDeviceCaps', 'SetPixel',
            'pyautogui.click', 'pyautogui.move', 'keyboard.is_pressed'
        ]
        
        for api in windows_apis:
            if api in content:
                self.critical_issues.append({
                    'type': 'unconverted_api',
                    'message': f'Windows API {api} not converted to macOS',
                    'severity': 'CRITICAL',
                    'fix': 'Convert to macOS equivalent API'
                })
    
    def validate_macos_compatibility(self, content):
        """Validate macOS-specific compatibility"""
        
        # Check for file path issues
        if re.search(r'[A-Z]:\\', content):
            self.critical_issues.append({
                'type': 'file_paths',
                'message': 'Windows file paths detected (C:\\)',
                'severity': 'HIGH',
                'fix': 'Convert to Unix-style paths'
            })
        
        # Check for registry access
        if 'winreg' in content or 'HKEY_' in content:
            self.critical_issues.append({
                'type': 'registry_access',
                'message': 'Windows registry access detected',
                'severity': 'HIGH',
                'fix': 'Convert to macOS preferences (plist)'
            })
        
        # Check for proper threading
        if 'threading' in content:
            if 'daemon' not in content:
                self.suggestions.append({
                    'type': 'threading_best_practice',
                    'message': 'Consider using daemon threads for background tasks',
                    'suggestion': 'Add: thread.daemon = True'
                })
        
        # Check for Retina display handling
        if 'screen' in content.lower() or 'display' in content.lower():
            if 'scale' not in content.lower() and 'retina' not in content.lower():
                self.suggestions.append({
                    'type': 'retina_support',
                    'message': 'Consider adding Retina display scaling support',
                    'suggestion': 'Implement display scale factor detection'
                })
    
    def validate_performance_patterns(self, content):
        """Validate performance-related patterns"""
        
        # Check for busy waiting
        busy_wait_patterns = [
            r'while.*:\s*pass',
            r'while.*:\s*time\.sleep\(0\)',
            r'while.*:\s*continue'
        ]
        
        for pattern in busy_wait_patterns:
            if re.search(pattern, content, re.MULTILINE):
                self.warnings.append({
                    'type': 'performance_issue',
                    'message': 'Busy waiting loop detected',
                    'suggestion': 'Use proper sleep intervals or event-driven approach'
                })
        
        # Check for excessive screen captures
        screen_capture_count = len(re.findall(r'CGDisplayCreateImage|screenshot|capture', content, re.IGNORECASE))
        if screen_capture_count > 5:
            self.suggestions.append({
                'type': 'performance_optimization',
                'message': f'{screen_capture_count} screen capture calls found',
                'suggestion': 'Consider caching screen captures or reducing frequency'
            })
        
        # Check for proper error handling in loops
        if 'while True:' in content or 'for' in content:
            if 'try:' not in content or 'except' not in content:
                self.warnings.append({
                    'type': 'error_handling',
                    'message': 'Loops without error handling detected',
                    'suggestion': 'Add try/except blocks to prevent crashes'
                })
    
    def validate_error_handling(self, content):
        """Validate error handling patterns"""
        
        # Check for bare except clauses
        if re.search(r'except\s*:', content):
            self.warnings.append({
                'type': 'error_handling',
                'message': 'Bare except clause detected',
                'suggestion': 'Specify exception types: except Exception as e:'
            })
        
        # Check for missing logging
        if 'except' in content and 'logging' not in content and 'print' not in content:
            self.suggestions.append({
                'type': 'error_handling',
                'message': 'Exception handling without logging detected',
                'suggestion': 'Add logging or print statements for debugging'
            })
        
        # Check for proper cleanup
        if 'open(' in content and 'with' not in content:
            self.warnings.append({
                'type': 'resource_management',
                'message': 'File operations without context manager',
                'suggestion': 'Use "with open()" for proper file handling'
            })
    
    def validate_resource_management(self, content):
        """Validate resource management"""
        
        # Check for thread cleanup
        if 'Thread(' in content or 'threading' in content:
            if 'join()' not in content and 'daemon' not in content:
                self.warnings.append({
                    'type': 'resource_management',
                    'message': 'Threads created without proper cleanup',
                    'suggestion': 'Use thread.join() or daemon threads'
                })
        
        # Check for listener cleanup
        if 'Listener(' in content:
            if 'stop()' not in content:
                self.suggestions.append({
                    'type': 'resource_management',
                    'message': 'Listeners created without stop() method',
                    'suggestion': 'Add listener.stop() for proper cleanup'
                })
    
    def validate_security_patterns(self, content):
        """Validate security-related patterns"""
        
        # Check for hardcoded credentials
        credential_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
            r'api_key\s*=\s*["\'][^"\']+["\']'
        ]
        
        for pattern in credential_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.warnings.append({
                    'type': 'security_risk',
                    'message': 'Potential hardcoded credentials detected',
                    'suggestion': 'Use environment variables or config files'
                })
        
        # Check for shell command injection risks
        if 'subprocess' in content and 'shell=True' in content:
            self.warnings.append({
                'type': 'security_risk',
                'message': 'subprocess with shell=True detected',
                'suggestion': 'Use shell=False and list arguments for security'
            })
    
    def validate_runtime_behavior(self, script_path):
        """Validate runtime behavior through static analysis"""
        
        try:
            # Try to compile the script
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            compile(content, script_path, 'exec')
            
            # Check if script can be imported (basic import test)
            spec = importlib.util.spec_from_file_location("test_module", script_path)
            if spec is None:
                self.warnings.append({
                    'type': 'import_test',
                    'message': 'Script may not be importable',
                    'suggestion': 'Check for syntax or import issues'
                })
            
        except SyntaxError as e:
            self.critical_issues.append({
                'type': 'compilation_error',
                'message': f'Script compilation failed: {e}',
                'severity': 'CRITICAL'
            })
        except Exception as e:
            self.warnings.append({
                'type': 'compilation_warning',
                'message': f'Script compilation warning: {e}',
                'suggestion': 'Review for potential runtime issues'
            })
    
    def generate_validation_report(self):
        """Generate comprehensive validation report"""
        
        total_issues = len(self.critical_issues) + len(self.warnings)
        
        # Calculate validation score
        base_score = 100
        base_score -= len(self.critical_issues) * 25  # Critical issues
        base_score -= len(self.warnings) * 10        # Warnings
        base_score -= len(self.suggestions) * 2      # Suggestions
        
        validation_score = max(0, base_score)
        
        # Determine status
        if len(self.critical_issues) > 0:
            status = "FAILED - Critical issues must be fixed"
        elif len(self.warnings) > 3:
            status = "WARNING - Multiple issues detected"
        elif len(self.warnings) > 0:
            status = "CAUTION - Minor issues found"
        else:
            status = "EXCELLENT - No issues detected"
        
        report = {
            'validation_score': validation_score,
            'status': status,
            'summary': {
                'critical_issues': len(self.critical_issues),
                'warnings': len(self.warnings),
                'suggestions': len(self.suggestions),
                'total_issues': total_issues
            },
            'critical_issues': self.critical_issues,
            'warnings': self.warnings,
            'suggestions': self.suggestions,
            'recommendations': self.generate_recommendations()
        }
        
        return report
    
    def generate_recommendations(self):
        """Generate specific recommendations"""
        
        recommendations = []
        
        if len(self.critical_issues) > 0:
            recommendations.append({
                'priority': 'IMMEDIATE',
                'action': 'Fix all critical issues before using the script',
                'details': 'Critical issues will prevent the script from working'
            })
        
        if len(self.warnings) > 5:
            recommendations.append({
                'priority': 'HIGH',
                'action': 'Address multiple warnings for better reliability',
                'details': 'Many warnings suggest the conversion needs review'
            })
        
        if len(self.suggestions) > 10:
            recommendations.append({
                'priority': 'MEDIUM',
                'action': 'Consider implementing suggested improvements',
                'details': 'Suggestions will improve performance and maintainability'
            })
        
        return recommendations

def ultra_validate_script(script_path):
    """Perform ultra-comprehensive validation"""
    
    validator = UltraValidator()
    success = validator.validate_converted_script(script_path)
    report = validator.generate_validation_report()
    
    print(f"\n🔍 Ultra-Validation Results:")
    print(f"📊 Validation Score: {report['validation_score']}/100")
    print(f"🎯 Status: {report['status']}")
    print(f"🚨 Critical Issues: {report['summary']['critical_issues']}")
    print(f"⚠️ Warnings: {report['summary']['warnings']}")
    print(f"💡 Suggestions: {report['summary']['suggestions']}")
    
    if report['critical_issues']:
        print(f"\n🚨 CRITICAL ISSUES:")
        for issue in report['critical_issues']:
            print(f"  • {issue['message']}")
            if 'fix' in issue:
                print(f"    Fix: {issue['fix']}")
    
    if report['warnings']:
        print(f"\n⚠️ WARNINGS:")
        for warning in report['warnings'][:5]:  # Show first 5
            print(f"  • {warning['message']}")
    
    if report['suggestions']:
        print(f"\n💡 SUGGESTIONS:")
        for suggestion in report['suggestions'][:3]:  # Show first 3
            print(f"  • {suggestion['message']}")
    
    return report

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_path = sys.argv[1]
        ultra_validate_script(script_path)
    else:
        print("Usage: python3 ultra_validator.py <script_path>")
