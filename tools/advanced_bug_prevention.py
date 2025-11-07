#!/usr/bin/env python3
"""
IRUS V5.0 - Advanced Bug Prevention System
Comprehensive bug prevention with predictive analysis and auto-fixing
"""

import ast
import sys
import os
import re
import json
import time
import subprocess
import threading
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import hashlib
import psutil

class PredictiveBugAnalyzer:
    """Advanced predictive bug analysis system"""
    
    def __init__(self):
        self.bug_patterns = self.load_bug_patterns()
        self.system_vulnerabilities = []
        self.runtime_monitors = []
        self.prevention_rules = self.load_prevention_rules()
        
    def load_bug_patterns(self) -> Dict:
        """Load comprehensive bug patterns database"""
        
        return {
            'syntax_patterns': {
                'missing_imports': [
                    r'(?:^|\n)(?!import|from).*\b(PIL|numpy|cv2|pynput|Quartz)\b',
                    r'(?:^|\n)(?!import|from).*\b(threading|time|os|sys)\b'
                ],
                'incorrect_indentation': [
                    r'\n\t+ +',  # Mixed tabs and spaces
                    r'\n {1,3}[^\s]',  # Incorrect indentation levels
                ],
                'missing_colons': [
                    r'(?:if|elif|else|for|while|def|class|try|except|finally|with)\s+[^:\n]*\n',
                ],
                'unclosed_brackets': [
                    r'\([^)]*\n[^)]*$',  # Unclosed parentheses
                    r'\[[^\]]*\n[^\]]*$',  # Unclosed brackets
                    r'\{[^}]*\n[^}]*$',  # Unclosed braces
                ]
            },
            'api_conversion_issues': {
                'windows_remnants': [
                    r'\bpyautogui\.',
                    r'\bmss\.',
                    r'\bkeyboard\.is_pressed',
                    r'\bctypes\.windll',
                    r'\bwin32\w+',
                    r'\bGetDC\(',
                    r'\bReleaseDC\(',
                ],
                'incomplete_macos_conversion': [
                    r'import\s+Quartz\s*$',  # Import without usage
                    r'from\s+pynput\s+import\s+\w+\s*$',  # Import without controller
                ],
                'missing_macos_apis': [
                    r'screenshot|capture.*screen',  # Screen capture without Quartz
                    r'click|mouse.*move',  # Mouse control without pynput
                    r'key.*press|keyboard',  # Keyboard without pynput
                ]
            },
            'performance_issues': {
                'blocking_operations': [
                    r'while\s+True\s*:\s*\n\s*(?!.*sleep)',  # Busy waiting
                    r'for\s+.*\s+in\s+range\(\d{4,}\)',  # Large loops
                ],
                'resource_leaks': [
                    r'open\([^)]*\)(?!\s*as|\s*with)',  # File not closed
                    r'Thread\([^)]*\)(?!.*daemon)',  # Non-daemon threads
                ],
                'inefficient_patterns': [
                    r'time\.sleep\(0\)',  # Ineffective sleep
                    r'\.append\(.*\)\s*\n.*\.append\(.*\)\s*\n.*\.append\(.*\)',  # Repeated appends
                ]
            },
            'security_vulnerabilities': {
                'code_injection': [
                    r'eval\s*\(',
                    r'exec\s*\(',
                    r'subprocess\.[^(]*shell\s*=\s*True',
                ],
                'hardcoded_secrets': [
                    r'password\s*=\s*["\'][^"\']{8,}["\']',
                    r'token\s*=\s*["\'][^"\']{20,}["\']',
                    r'api_key\s*=\s*["\'][^"\']{15,}["\']',
                ],
                'unsafe_operations': [
                    r'pickle\.loads?\(',
                    r'__import__\(',
                    r'getattr\([^,]*,\s*["\'][^"\']*["\']',
                ]
            },
            'macos_specific_issues': {
                'permission_problems': [
                    r'CGDisplayCreateImage',  # Needs screen recording permission
                    r'pynput\.mouse\.Controller',  # Needs accessibility permission
                    r'pynput\.keyboard\.Listener',  # Needs input monitoring permission
                ],
                'path_issues': [
                    r'[A-Z]:\\\\',  # Windows paths
                    r'\\\\[^n]',  # Backslashes (not \n)
                ],
                'compatibility_issues': [
                    r'import\s+winreg',
                    r'HKEY_\w+',
                    r'\.exe["\']',
                ]
            }
        }
    
    def load_prevention_rules(self) -> Dict:
        """Load bug prevention rules"""
        
        return {
            'auto_fixes': {
                'add_missing_imports': {
                    'PIL': 'from PIL import Image',
                    'numpy': 'import numpy as np',
                    'cv2': 'import cv2',
                    'pynput.mouse': 'from pynput.mouse import Button, Listener as MouseListener\nfrom pynput import mouse',
                    'pynput.keyboard': 'from pynput.keyboard import Key, Listener as KeyboardListener\nfrom pynput import keyboard',
                    'Quartz': 'from Quartz import CGWindowListCopyWindowInfo, CGDisplayCreateImage, CGMainDisplayID\nfrom Quartz.CoreGraphics import CGRectMake',
                    'threading': 'import threading',
                    'time': 'import time',
                    'os': 'import os',
                    'sys': 'import sys'
                },
                'replace_windows_apis': {
                    'pyautogui.click': 'mouse_controller.click(Button.left, 1)',
                    'pyautogui.move': 'mouse_controller.position = ',
                    'pyautogui.screenshot': 'capture_screen_region()',
                    'keyboard.is_pressed': 'is_key_pressed',
                    'mss.mss().grab': 'capture_screen_region',
                },
                'fix_indentation': {
                    'pattern': r'\t',
                    'replacement': '    '  # Convert tabs to 4 spaces
                },
                'add_error_handling': {
                    'pattern': r'(def\s+\w+\([^)]*\):\s*\n(?:\s*"""[^"]*"""\s*\n)?)(\s*)(.*)',
                    'replacement': r'\1\2try:\n\2    \3\n\2except Exception as e:\n\2    print(f"Error in function: {e}")\n\2    return None'
                }
            },
            'validation_checks': {
                'required_functions': [
                    'capture_screen_region',
                    'mouse_controller',
                    'keyboard_listener'
                ],
                'required_imports': [
                    'Quartz',
                    'pynput',
                    'PIL',
                    'numpy'
                ],
                'forbidden_patterns': [
                    'eval(',
                    'exec(',
                    'shell=True'
                ]
            }
        }
    
    def analyze_code_structure(self, content: str) -> Dict:
        """Deep analysis of code structure"""
        
        analysis = {
            'ast_analysis': {},
            'complexity_metrics': {},
            'dependency_graph': {},
            'potential_issues': []
        }
        
        try:
            # Parse AST
            tree = ast.parse(content)
            
            # Analyze AST structure
            analysis['ast_analysis'] = {
                'functions': len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]),
                'classes': len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]),
                'imports': len([n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]),
                'loops': len([n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))]),
                'conditionals': len([n for n in ast.walk(tree) if isinstance(n, ast.If)]),
                'try_blocks': len([n for n in ast.walk(tree) if isinstance(n, ast.Try)])
            }
            
            # Calculate complexity metrics
            total_nodes = len(list(ast.walk(tree)))
            analysis['complexity_metrics'] = {
                'total_nodes': total_nodes,
                'complexity_score': total_nodes / 100,  # Rough complexity measure
                'nesting_depth': self.calculate_nesting_depth(tree),
                'function_complexity': self.analyze_function_complexity(tree)
            }
            
            # Check for potential issues
            for node in ast.walk(tree):
                # Dangerous function calls
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name):
                        if node.func.id in ['eval', 'exec']:
                            analysis['potential_issues'].append({
                                'type': 'security_risk',
                                'message': f'Dangerous function call: {node.func.id}',
                                'line': getattr(node, 'lineno', 'unknown')
                            })
                
                # Long functions (potential complexity issue)
                if isinstance(node, ast.FunctionDef):
                    if hasattr(node, 'end_lineno') and hasattr(node, 'lineno'):
                        length = node.end_lineno - node.lineno
                        if length > 50:
                            analysis['potential_issues'].append({
                                'type': 'complexity_warning',
                                'message': f'Long function: {node.name} ({length} lines)',
                                'line': node.lineno
                            })
        
        except SyntaxError as e:
            analysis['potential_issues'].append({
                'type': 'syntax_error',
                'message': f'Syntax error: {e.msg}',
                'line': e.lineno
            })
        
        return analysis
    
    def calculate_nesting_depth(self, tree: ast.AST) -> int:
        """Calculate maximum nesting depth"""
        
        def get_depth(node, current_depth=0):
            max_depth = current_depth
            
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
                    child_depth = get_depth(child, current_depth + 1)
                    max_depth = max(max_depth, child_depth)
                else:
                    child_depth = get_depth(child, current_depth)
                    max_depth = max(max_depth, child_depth)
            
            return max_depth
        
        return get_depth(tree)
    
    def analyze_function_complexity(self, tree: ast.AST) -> Dict:
        """Analyze complexity of individual functions"""
        
        function_complexities = {}
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                complexity = 1  # Base complexity
                
                # Count decision points
                for child in ast.walk(node):
                    if isinstance(child, (ast.If, ast.For, ast.While)):
                        complexity += 1
                    elif isinstance(child, ast.BoolOp):
                        complexity += len(child.values) - 1
                
                function_complexities[node.name] = complexity
        
        return function_complexities
    
    def predict_runtime_issues(self, content: str, system_info: Dict) -> List[Dict]:
        """Predict potential runtime issues"""
        
        predictions = []
        
        # Memory usage prediction
        if 'numpy' in content and 'array' in content:
            if system_info.get('memory_total_gb', 8) < 4:
                predictions.append({
                    'type': 'memory_warning',
                    'severity': 'MEDIUM',
                    'message': 'NumPy operations may consume significant memory',
                    'suggestion': 'Monitor memory usage during execution'
                })
        
        # Performance predictions
        screen_captures = len(re.findall(r'capture|screenshot', content, re.IGNORECASE))
        if screen_captures > 10:
            predictions.append({
                'type': 'performance_warning',
                'severity': 'MEDIUM',
                'message': f'{screen_captures} screen capture operations detected',
                'suggestion': 'Consider caching or reducing capture frequency'
            })
        
        # Threading issues
        if 'threading' in content and 'join()' not in content:
            predictions.append({
                'type': 'threading_warning',
                'severity': 'HIGH',
                'message': 'Threads created without proper cleanup',
                'suggestion': 'Add thread.join() or use daemon threads'
            })
        
        # macOS-specific predictions
        if system_info.get('os') == 'Darwin':
            if 'CGDisplayCreateImage' in content:
                predictions.append({
                    'type': 'permission_requirement',
                    'severity': 'HIGH',
                    'message': 'Screen Recording permission required',
                    'suggestion': 'Grant permission in System Preferences'
                })
            
            if 'pynput' in content:
                predictions.append({
                    'type': 'permission_requirement',
                    'severity': 'HIGH',
                    'message': 'Accessibility permission required',
                    'suggestion': 'Grant permission in System Preferences'
                })
        
        return predictions
    
    def comprehensive_analysis(self, script_path: str, system_info: Dict = None) -> Dict:
        """Perform comprehensive bug analysis"""
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {
                'success': False,
                'error': f'Cannot read script: {e}',
                'analysis': {}
            }
        
        analysis = {
            'file_info': {
                'path': script_path,
                'size_bytes': len(content.encode('utf-8')),
                'lines': len(content.split('\n')),
                'hash': hashlib.md5(content.encode()).hexdigest()
            },
            'syntax_issues': [],
            'api_issues': [],
            'performance_issues': [],
            'security_issues': [],
            'macos_issues': [],
            'structure_analysis': {},
            'runtime_predictions': [],
            'auto_fixes_available': [],
            'overall_score': 0
        }
        
        # Analyze each category
        for category, patterns in self.bug_patterns.items():
            for subcategory, pattern_list in patterns.items():
                for pattern in pattern_list:
                    matches = re.finditer(pattern, content, re.MULTILINE | re.IGNORECASE)
                    for match in matches:
                        line_num = content[:match.start()].count('\n') + 1
                        
                        issue = {
                            'pattern': pattern,
                            'match': match.group(0)[:50],
                            'line': line_num,
                            'category': category,
                            'subcategory': subcategory
                        }
                        
                        # Categorize issues
                        if category == 'syntax_patterns':
                            analysis['syntax_issues'].append(issue)
                        elif category == 'api_conversion_issues':
                            analysis['api_issues'].append(issue)
                        elif category == 'performance_issues':
                            analysis['performance_issues'].append(issue)
                        elif category == 'security_vulnerabilities':
                            analysis['security_issues'].append(issue)
                        elif category == 'macos_specific_issues':
                            analysis['macos_issues'].append(issue)
        
        # Structure analysis
        analysis['structure_analysis'] = self.analyze_code_structure(content)
        
        # Runtime predictions
        if system_info:
            analysis['runtime_predictions'] = self.predict_runtime_issues(content, system_info)
        
        # Calculate overall score
        total_issues = (len(analysis['syntax_issues']) * 3 +
                       len(analysis['api_issues']) * 2 +
                       len(analysis['performance_issues']) * 1 +
                       len(analysis['security_issues']) * 4 +
                       len(analysis['macos_issues']) * 2)
        
        analysis['overall_score'] = max(0, 100 - total_issues)
        
        return {
            'success': True,
            'analysis': analysis
        }

class AutoBugFixer:
    """Automatic bug fixing system"""
    
    def __init__(self):
        self.fix_patterns = self.load_fix_patterns()
        self.fixes_applied = []
        
    def load_fix_patterns(self) -> Dict:
        """Load automatic fix patterns"""
        
        return {
            'import_fixes': {
                # Add missing imports at the top
                'PIL_usage': {
                    'pattern': r'(?:Image\.|PIL\.)',
                    'fix': 'from PIL import Image',
                    'position': 'top'
                },
                'numpy_usage': {
                    'pattern': r'(?:np\.|numpy\.)',
                    'fix': 'import numpy as np',
                    'position': 'top'
                },
                'cv2_usage': {
                    'pattern': r'cv2\.',
                    'fix': 'import cv2',
                    'position': 'top'
                }
            },
            'api_replacements': {
                'pyautogui_click': {
                    'pattern': r'pyautogui\.click\(([^)]*)\)',
                    'replacement': r'mouse_controller.click(Button.left, 1)  # Position: \1'
                },
                'pyautogui_move': {
                    'pattern': r'pyautogui\.moveTo\(([^)]*)\)',
                    'replacement': r'mouse_controller.position = (\1)'
                },
                'keyboard_is_pressed': {
                    'pattern': r'keyboard\.is_pressed\([\'"]([^\'"]+)[\'"]\)',
                    'replacement': r'is_key_pressed("\1")'
                }
            },
            'syntax_fixes': {
                'tabs_to_spaces': {
                    'pattern': r'\t',
                    'replacement': '    '
                },
                'print_statements': {
                    'pattern': r'print\s+([^(][^\n]*)',
                    'replacement': r'print(\1)'
                }
            },
            'security_fixes': {
                'eval_removal': {
                    'pattern': r'eval\s*\([^)]*\)',
                    'replacement': '# eval() removed for security - implement safe alternative'
                },
                'exec_removal': {
                    'pattern': r'exec\s*\([^)]*\)',
                    'replacement': '# exec() removed for security - implement safe alternative'
                }
            }
        }
    
    def apply_automatic_fixes(self, content: str) -> Tuple[str, List[str]]:
        """Apply automatic fixes to code"""
        
        fixed_content = content
        fixes_applied = []
        
        # Apply import fixes
        for fix_name, fix_data in self.fix_patterns['import_fixes'].items():
            if re.search(fix_data['pattern'], fixed_content):
                # Check if import already exists
                if fix_data['fix'] not in fixed_content:
                    # Add import at the top
                    lines = fixed_content.split('\n')
                    
                    # Find position after existing imports
                    insert_pos = 0
                    for i, line in enumerate(lines):
                        if line.strip().startswith(('import ', 'from ')):
                            insert_pos = i + 1
                        elif line.strip() and not line.strip().startswith('#'):
                            break
                    
                    lines.insert(insert_pos, fix_data['fix'])
                    fixed_content = '\n'.join(lines)
                    fixes_applied.append(f"Added missing import: {fix_data['fix']}")
        
        # Apply API replacements
        for fix_name, fix_data in self.fix_patterns['api_replacements'].items():
            if re.search(fix_data['pattern'], fixed_content):
                fixed_content = re.sub(fix_data['pattern'], fix_data['replacement'], fixed_content)
                fixes_applied.append(f"Replaced API call: {fix_name}")
        
        # Apply syntax fixes
        for fix_name, fix_data in self.fix_patterns['syntax_fixes'].items():
            if re.search(fix_data['pattern'], fixed_content):
                fixed_content = re.sub(fix_data['pattern'], fix_data['replacement'], fixed_content)
                fixes_applied.append(f"Fixed syntax: {fix_name}")
        
        # Apply security fixes
        for fix_name, fix_data in self.fix_patterns['security_fixes'].items():
            if re.search(fix_data['pattern'], fixed_content):
                fixed_content = re.sub(fix_data['pattern'], fix_data['replacement'], fixed_content)
                fixes_applied.append(f"Security fix: {fix_name}")
        
        return fixed_content, fixes_applied
    
    def add_error_handling(self, content: str) -> str:
        """Add comprehensive error handling"""
        
        lines = content.split('\n')
        enhanced_lines = []
        
        in_function = False
        function_indent = 0
        
        for i, line in enumerate(lines):
            enhanced_lines.append(line)
            
            # Detect function definitions
            if re.match(r'\s*def\s+\w+', line):
                in_function = True
                function_indent = len(line) - len(line.lstrip())
                
                # Add try block after function definition
                if i + 1 < len(lines) and not lines[i + 1].strip().startswith('"""'):
                    enhanced_lines.append(' ' * (function_indent + 4) + 'try:')
            
            # End of function
            elif in_function and line.strip() and len(line) - len(line.lstrip()) <= function_indent:
                if not line.strip().startswith(('except', 'finally')):
                    # Add except block before function ends
                    enhanced_lines.insert(-1, ' ' * (function_indent + 4) + 'except Exception as e:')
                    enhanced_lines.insert(-1, ' ' * (function_indent + 8) + 'print(f"Error in function: {e}")')
                    enhanced_lines.insert(-1, ' ' * (function_indent + 8) + 'return None')
                    in_function = False
        
        return '\n'.join(enhanced_lines)

class SystemVulnerabilityScanner:
    """Scan for system-level vulnerabilities"""
    
    def __init__(self):
        self.vulnerabilities = []
        
    def scan_system_security(self) -> List[Dict]:
        """Scan for system security issues"""
        
        vulnerabilities = []
        
        # Check Python version
        python_version = sys.version_info
        if python_version < (3, 8):
            vulnerabilities.append({
                'type': 'python_version',
                'severity': 'HIGH',
                'message': f'Python {python_version.major}.{python_version.minor} has known security vulnerabilities',
                'suggestion': 'Upgrade to Python 3.8 or newer'
            })
        
        # Check for writable system directories
        try:
            if os.access('/usr/local/bin', os.W_OK):
                vulnerabilities.append({
                    'type': 'file_permissions',
                    'severity': 'MEDIUM',
                    'message': 'System directories are writable',
                    'suggestion': 'Check file permissions'
                })
        except:
            pass
        
        # Check for running processes
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if 'keylogger' in proc.info['name'].lower():
                    vulnerabilities.append({
                        'type': 'suspicious_process',
                        'severity': 'HIGH',
                        'message': f'Suspicious process detected: {proc.info["name"]}',
                        'suggestion': 'Investigate running processes'
                    })
        except:
            pass
        
        return vulnerabilities
    
    def scan_network_security(self) -> List[Dict]:
        """Scan for network security issues"""
        
        vulnerabilities = []
        
        # Check for open ports (basic check)
        try:
            import socket
            
            dangerous_ports = [22, 23, 135, 139, 445, 1433, 3389]
            for port in dangerous_ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex(('localhost', port))
                if result == 0:
                    vulnerabilities.append({
                        'type': 'open_port',
                        'severity': 'MEDIUM',
                        'message': f'Port {port} is open',
                        'suggestion': 'Review open ports and services'
                    })
                sock.close()
        except:
            pass
        
        return vulnerabilities

def comprehensive_bug_prevention(script_path: str, system_info: Dict = None) -> Dict:
    """Perform comprehensive bug prevention analysis"""
    
    print("🔍 Starting comprehensive bug prevention analysis...")
    
    # Initialize analyzers
    bug_analyzer = PredictiveBugAnalyzer()
    auto_fixer = AutoBugFixer()
    security_scanner = SystemVulnerabilityScanner()
    
    # Perform analysis
    analysis_result = bug_analyzer.comprehensive_analysis(script_path, system_info)
    
    if not analysis_result['success']:
        return analysis_result
    
    analysis = analysis_result['analysis']
    
    # Apply automatic fixes if requested
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content, fixes_applied = auto_fixer.apply_automatic_fixes(original_content)
        
        # Add error handling
        enhanced_content = auto_fixer.add_error_handling(fixed_content)
        
        # Save fixed version
        fixed_path = script_path.replace('.py', '_fixed.py')
        with open(fixed_path, 'w', encoding='utf-8') as f:
            f.write(enhanced_content)
        
        analysis['auto_fixes'] = {
            'fixes_applied': fixes_applied,
            'fixed_file': fixed_path,
            'original_preserved': True
        }
        
    except Exception as e:
        analysis['auto_fixes'] = {
            'error': f'Could not apply fixes: {e}',
            'fixes_applied': []
        }
    
    # System security scan
    analysis['system_vulnerabilities'] = security_scanner.scan_system_security()
    analysis['network_vulnerabilities'] = security_scanner.scan_network_security()
    
    # Generate comprehensive report
    total_critical = len([i for i in analysis['syntax_issues'] + analysis['security_issues'] if 'critical' in str(i).lower()])
    total_warnings = len(analysis['performance_issues'] + analysis['macos_issues'])
    
    analysis['summary'] = {
        'overall_score': analysis['overall_score'],
        'critical_issues': total_critical,
        'warnings': total_warnings,
        'fixes_available': len(analysis['auto_fixes'].get('fixes_applied', [])),
        'recommendation': 'EXCELLENT' if analysis['overall_score'] > 90 else
                        'GOOD' if analysis['overall_score'] > 70 else
                        'NEEDS_IMPROVEMENT' if analysis['overall_score'] > 50 else
                        'CRITICAL_ISSUES'
    }
    
    return {
        'success': True,
        'analysis': analysis
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_path = sys.argv[1]
        result = comprehensive_bug_prevention(script_path)
        
        if result['success']:
            analysis = result['analysis']
            print(f"\n📊 Bug Prevention Analysis Complete:")
            print(f"🎯 Overall Score: {analysis['overall_score']}/100")
            print(f"🚨 Critical Issues: {analysis['summary']['critical_issues']}")
            print(f"⚠️ Warnings: {analysis['summary']['warnings']}")
            print(f"🔧 Auto-fixes Applied: {analysis['summary']['fixes_available']}")
            print(f"💡 Recommendation: {analysis['summary']['recommendation']}")
        else:
            print(f"❌ Analysis failed: {result['error']}")
    else:
        print("Usage: python3 advanced_bug_prevention.py <script_path>")
