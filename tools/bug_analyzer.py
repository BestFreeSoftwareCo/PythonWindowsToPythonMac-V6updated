#!/usr/bin/env python3
"""
IRUS V4 - Bug Analysis System
Analyzes converted scripts for potential issues and fixes them
"""

import re
import ast
import sys
from pathlib import Path

class BugAnalyzer:
    def __init__(self):
        self.bugs_found = []
        self.fixes_applied = []
        self.warnings = []
        
    def analyze_converted_script(self, script_path):
        """Analyze converted script for common bugs"""
        print(f"🔍 Analyzing {script_path} for potential bugs...")
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.bugs_found.append({
                'type': 'file_error',
                'severity': 'critical',
                'description': f'Cannot read script file: {e}',
                'fix': 'Ensure file exists and is readable'
            })
            return False
        
        # Check syntax validity
        if not self.check_syntax(content):
            return False
        
        # Analyze common conversion issues
        self.check_import_issues(content)
        self.check_api_conversion_issues(content)
        self.check_macos_specific_issues(content)
        self.check_performance_issues(content)
        self.check_compatibility_issues(content)
        
        return True
    
    def check_syntax(self, content):
        """Check if Python syntax is valid"""
        try:
            ast.parse(content)
            return True
        except SyntaxError as e:
            self.bugs_found.append({
                'type': 'syntax_error',
                'severity': 'critical',
                'description': f'Syntax error at line {e.lineno}: {e.msg}',
                'fix': 'Fix syntax error in converted code',
                'line': e.lineno
            })
            return False
    
    def check_import_issues(self, content):
        """Check for import-related issues"""
        
        # Check for missing imports
        required_imports = {
            'Quartz': 'from Quartz import CGWindowListCopyWindowInfo, CGDisplayCreateImage',
            'pynput.mouse': 'from pynput.mouse import Button, Listener as MouseListener',
            'pynput.keyboard': 'from pynput.keyboard import Key, Listener as KeyboardListener',
            'threading': 'import threading',
            'time': 'import time'
        }
        
        for module, import_line in required_imports.items():
            if module.replace('.', '_') in content or module in content:
                # Module is used, check if imported
                if not re.search(rf'import.*{re.escape(module.split(".")[-1])}', content):
                    self.bugs_found.append({
                        'type': 'missing_import',
                        'severity': 'high',
                        'description': f'Missing import for {module}',
                        'fix': f'Add: {import_line}',
                        'auto_fix': True,
                        'fix_code': import_line
                    })
        
        # Check for Windows-specific imports that weren't converted
        windows_imports = ['mss', 'pyautogui', 'keyboard', 'ctypes.windll']
        for win_import in windows_imports:
            if re.search(rf'import\s+{re.escape(win_import)}', content):
                self.bugs_found.append({
                    'type': 'unconverted_import',
                    'severity': 'critical',
                    'description': f'Windows import {win_import} not converted',
                    'fix': 'Convert to macOS equivalent',
                    'auto_fix': False
                })
    
    def check_api_conversion_issues(self, content):
        """Check for API conversion issues"""
        
        # Screen capture issues
        if 'mss' in content and 'Quartz' not in content:
            self.bugs_found.append({
                'type': 'screen_capture_not_converted',
                'severity': 'critical',
                'description': 'Screen capture still uses mss instead of Quartz',
                'fix': 'Convert mss.mss() to Quartz CGDisplayCreateImage',
                'auto_fix': False
            })
        
        # Mouse control issues
        if 'pyautogui.click' in content and 'pynput' not in content:
            self.bugs_found.append({
                'type': 'mouse_control_not_converted',
                'severity': 'critical',
                'description': 'Mouse control still uses pyautogui',
                'fix': 'Convert pyautogui.click to pynput.mouse.Button',
                'auto_fix': False
            })
        
        # Keyboard issues
        if 'keyboard.is_pressed' in content and 'pynput.keyboard' not in content:
            self.bugs_found.append({
                'type': 'keyboard_not_converted',
                'severity': 'critical',
                'description': 'Keyboard detection still uses keyboard library',
                'fix': 'Convert to pynput.keyboard.Listener',
                'auto_fix': False
            })
    
    def check_macos_specific_issues(self, content):
        """Check for macOS-specific issues"""
        
        # DPI/Retina handling
        if 'GetDC' in content or 'GetDeviceCaps' in content:
            self.bugs_found.append({
                'type': 'dpi_handling_not_converted',
                'severity': 'high',
                'description': 'Windows DPI handling not converted to Retina support',
                'fix': 'Implement NSScreen backingScaleFactor detection',
                'auto_fix': False
            })
        
        # File path issues
        if re.search(r'[A-Z]:\\', content):
            self.bugs_found.append({
                'type': 'windows_file_paths',
                'severity': 'medium',
                'description': 'Windows file paths detected (C:\\)',
                'fix': 'Convert to Unix-style paths (/)',
                'auto_fix': True
            })
        
        # Registry access
        if 'winreg' in content or 'HKEY_' in content:
            self.bugs_found.append({
                'type': 'registry_access',
                'severity': 'high',
                'description': 'Windows registry access detected',
                'fix': 'Convert to macOS preferences (plist files)',
                'auto_fix': False
            })
    
    def check_performance_issues(self, content):
        """Check for performance issues"""
        
        # Inefficient screen capture
        if content.count('CGDisplayCreateImage') > 1:
            # Multiple screen captures without caching
            self.warnings.append({
                'type': 'performance_warning',
                'severity': 'low',
                'description': 'Multiple screen captures detected - consider caching',
                'suggestion': 'Cache screen captures when possible'
            })
        
        # Busy waiting loops
        busy_wait_patterns = [
            r'while.*:\s*pass',
            r'while.*:\s*time\.sleep\(0\)',
            r'while.*:\s*continue'
        ]
        
        for pattern in busy_wait_patterns:
            if re.search(pattern, content):
                self.warnings.append({
                    'type': 'busy_wait_loop',
                    'severity': 'medium',
                    'description': 'Busy waiting loop detected',
                    'suggestion': 'Use proper sleep intervals or event-driven approach'
                })
    
    def check_compatibility_issues(self, content):
        """Check for compatibility issues"""
        
        # Python version compatibility
        if 'f"' in content:  # f-strings require Python 3.6+
            self.warnings.append({
                'type': 'python_version_requirement',
                'severity': 'info',
                'description': 'Script uses f-strings (requires Python 3.6+)',
                'suggestion': 'Ensure Python 3.6+ is used'
            })
        
        # Apple Silicon compatibility
        if 'x86_64' in content or 'intel' in content.lower():
            self.warnings.append({
                'type': 'architecture_specific',
                'severity': 'low',
                'description': 'Architecture-specific code detected',
                'suggestion': 'Test on both Intel and Apple Silicon Macs'
            })
    
    def generate_fixed_script(self, original_content):
        """Generate fixed version of the script"""
        fixed_content = original_content
        
        # Apply automatic fixes
        for bug in self.bugs_found:
            if bug.get('auto_fix', False):
                if bug['type'] == 'missing_import':
                    # Add missing import at the top
                    import_line = bug['fix_code']
                    if import_line not in fixed_content:
                        # Find the last import line
                        lines = fixed_content.split('\n')
                        import_index = 0
                        for i, line in enumerate(lines):
                            if line.strip().startswith(('import ', 'from ')):
                                import_index = i
                        
                        lines.insert(import_index + 1, import_line)
                        fixed_content = '\n'.join(lines)
                        
                        self.fixes_applied.append({
                            'type': bug['type'],
                            'description': f'Added missing import: {import_line}'
                        })
                
                elif bug['type'] == 'windows_file_paths':
                    # Convert Windows paths to Unix paths
                    fixed_content = re.sub(r'[A-Z]:\\', '/', fixed_content)
                    fixed_content = fixed_content.replace('\\', '/')
                    
                    self.fixes_applied.append({
                        'type': bug['type'],
                        'description': 'Converted Windows file paths to Unix paths'
                    })
        
        return fixed_content
    
    def generate_report(self):
        """Generate comprehensive bug analysis report"""
        
        total_issues = len(self.bugs_found) + len(self.warnings)
        critical_bugs = len([b for b in self.bugs_found if b['severity'] == 'critical'])
        high_bugs = len([b for b in self.bugs_found if b['severity'] == 'high'])
        
        report = {
            'summary': {
                'total_issues': total_issues,
                'critical_bugs': critical_bugs,
                'high_priority_bugs': high_bugs,
                'warnings': len(self.warnings),
                'fixes_applied': len(self.fixes_applied),
                'status': self.get_overall_status()
            },
            'bugs_found': self.bugs_found,
            'warnings': self.warnings,
            'fixes_applied': self.fixes_applied,
            'recommendations': self.generate_recommendations()
        }
        
        return report
    
    def get_overall_status(self):
        """Get overall script status"""
        critical_bugs = len([b for b in self.bugs_found if b['severity'] == 'critical'])
        high_bugs = len([b for b in self.bugs_found if b['severity'] == 'high'])
        
        if critical_bugs > 0:
            return 'CRITICAL - Script will not work'
        elif high_bugs > 0:
            return 'HIGH RISK - Script may have issues'
        elif len(self.bugs_found) > 0:
            return 'MEDIUM RISK - Minor issues detected'
        elif len(self.warnings) > 0:
            return 'LOW RISK - Warnings only'
        else:
            return 'EXCELLENT - No issues detected'
    
    def generate_recommendations(self):
        """Generate recommendations based on analysis"""
        recommendations = []
        
        critical_bugs = [b for b in self.bugs_found if b['severity'] == 'critical']
        if critical_bugs:
            recommendations.append({
                'priority': 'IMMEDIATE',
                'action': f'Fix {len(critical_bugs)} critical bugs before using script',
                'details': [bug['description'] for bug in critical_bugs]
            })
        
        high_bugs = [b for b in self.bugs_found if b['severity'] == 'high']
        if high_bugs:
            recommendations.append({
                'priority': 'HIGH',
                'action': f'Address {len(high_bugs)} high-priority issues',
                'details': [bug['description'] for bug in high_bugs]
            })
        
        if len(self.warnings) > 3:
            recommendations.append({
                'priority': 'MEDIUM',
                'action': 'Review performance and compatibility warnings',
                'details': 'Multiple warnings suggest thorough testing needed'
            })
        
        return recommendations

def analyze_script(script_path):
    """Analyze a converted script for bugs"""
    analyzer = BugAnalyzer()
    
    if analyzer.analyze_converted_script(script_path):
        # Try to generate fixed version
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            fixed_content = analyzer.generate_fixed_script(original_content)
            
            # Save fixed version if changes were made
            if fixed_content != original_content:
                fixed_path = script_path.replace('.py', '_fixed.py')
                with open(fixed_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"✅ Fixed version saved as: {fixed_path}")
        
        except Exception as e:
            print(f"⚠️ Could not generate fixed version: {e}")
    
    return analyzer.generate_report()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_path = sys.argv[1]
        report = analyze_script(script_path)
        
        print("\n" + "="*50)
        print("BUG ANALYSIS REPORT")
        print("="*50)
        print(f"Status: {report['summary']['status']}")
        print(f"Total Issues: {report['summary']['total_issues']}")
        print(f"Critical Bugs: {report['summary']['critical_bugs']}")
        print(f"Fixes Applied: {report['summary']['fixes_applied']}")
        
        if report['bugs_found']:
            print(f"\n🐛 BUGS FOUND:")
            for bug in report['bugs_found']:
                print(f"  • {bug['severity'].upper()}: {bug['description']}")
                print(f"    Fix: {bug['fix']}")
        
        if report['recommendations']:
            print(f"\n📋 RECOMMENDATIONS:")
            for rec in report['recommendations']:
                print(f"  • {rec['priority']}: {rec['action']}")
    else:
        print("Usage: python3 bug_analyzer.py <script_path>")
