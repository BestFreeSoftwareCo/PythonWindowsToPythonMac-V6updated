#!/usr/bin/env python3
"""
IRUS V6.0 - AI Code Optimizer
Intelligent code analysis and optimization
Advanced pattern recognition and improvement suggestions
"""

import ast
import re
import json
import time
from pathlib import Path
from typing import List, Dict, Tuple

class AICodeOptimizer:
    """AI-powered code optimization system"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.optimization_rules = self._load_optimization_rules()
        self.performance_patterns = self._load_performance_patterns()
        self.security_patterns = self._load_security_patterns()

    def _load_optimization_rules(self):
        """Load AI optimization rules"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        return {
            'loop_optimization': {
                'pattern': r'for\s+\w+\s+in\s+range\(len\(',
                'suggestion': 'Use enumerate() for better performance',
                'replacement': lambda match: self._optimize_range_len(match),
                'confidence': 0.9
            },
            'string_concatenation': {
                'pattern': r'(\w+\s*\+=\s*["\'].*["\'])',
                'suggestion': 'Use f-strings or join() for multiple concatenations',
                'replacement': lambda match: self._optimize_string_concat(match),
                'confidence': 0.8
            },
            'list_comprehension': {
                'pattern': r'(\w+\s*=\s*\[\])\s*\n\s*for\s+\w+\s+in\s+.*:\s*\n\s*\1\.append\(',
                'suggestion': 'Use list comprehension for better performance',
                'replacement': lambda match: self._create_list_comprehension(match),
                'confidence': 0.85
            },
            'exception_handling': {
                'pattern': r'except\s*:\s*\n\s*pass',
                'suggestion': 'Specify exception types and add logging',
                'replacement': lambda match: 'except Exception as e:\n    logging.warning(f"Error: {e}")',
                'confidence': 0.9
            },
            'memory_optimization': {
                'pattern': r'with\s+open\([^)]+\)\s+as\s+\w+:\s*\n\s*content\s*=\s*\w+\.read\(\)',
                'suggestion': 'Consider streaming for large files',
                'replacement': lambda match: self._optimize_file_reading(match),
                'confidence': 0.7
            }
        }

    def _load_performance_patterns(self):
        """Load performance optimization patterns"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        return {
            'cpu_intensive': [
                r'while\s+True:(?!\s*.*time\.sleep)',  # Busy waiting
                r'for.*for.*for',  # Nested loops
                r'\.sort\(\).*\.sort\(\)',  # Multiple sorts
            ],
            'memory_intensive': [
                r'.*\*.*\*.*\*',  # Multiple multiplications
                r'\[\].*append.*append',  # List growing
                r'dict\(\).*\[.*\]\s*=',  # Dict growing
            ],
            'io_intensive': [
                r'open\(.*\)(?!\s*with)',  # File operations
                r'requests\.',  # Network requests
                r'os\.system',  # System calls
            ]
        }

    def _load_security_patterns(self):
        """Load security vulnerability patterns"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        return {
            'code_injection': [
                r'\beval\(',
                r'\bexec\(',
                r'os\.system\([^)]*input',
                r'subprocess.*shell=True'
            ],
            'path_traversal': [
                r'open\([^)]*\.\./.*\)',
                r'Path\([^)]*\.\./.*\)'
            ],
            'hardcoded_secrets': [
                r'password\s*=\s*["\'][^"\']+["\']',
                r'api_key\s*=\s*["\'][^"\']+["\']',
                r'token\s*=\s*["\'][^"\']+["\']'
            ]
        }

    def analyze_code(self, code_content: str, filename: str = "unknown") -> Dict:
        """Comprehensive AI code analysis"""
        analysis = {
            'filename': filename,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'metrics': self._calculate_metrics(code_content),
            'optimizations': self._find_optimizations(code_content),
            'performance_issues': self._find_performance_issues(code_content),
            'security_issues': self._find_security_issues(code_content),
            'suggestions': self._generate_suggestions(code_content),
            'overall_score': 0
        }

        # Calculate overall code quality score
        analysis['overall_score'] = self._calculate_quality_score(analysis)

        return analysis

    def _calculate_metrics(self, code: str) -> Dict:
        """Calculate code metrics"""
        lines = code.splitlines()

        return {
            'total_lines': len(lines),
            'code_lines': len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
            'blank_lines': len([l for l in lines if not l.strip()]),
            'functions': len(re.findall(r'def\s+\w+', code)),
            'classes': len(re.findall(r'class\s+\w+', code)),
            'imports': len(re.findall(r'^import\s+|^from\s+.*import', code, re.MULTILINE)),
            'complexity_estimate': self._estimate_complexity(code)
        }

    def _estimate_complexity(self, code: str) -> int:
        """Estimate code complexity (simplified cyclomatic complexity)"""
        complexity_keywords = ['if', 'elif', 'else', 'for', 'while', 'try', 'except', 'with']
        complexity = 1  # Base complexity

        for keyword in complexity_keywords:
            complexity += len(re.findall(rf'\b{keyword}\b', code))

        return complexity

    def _find_optimizations(self, code: str) -> List[Dict]:
        """Find optimization opportunities"""
        optimizations = []

        for rule_name, rule in self.optimization_rules.items():
            matches = re.finditer(rule['pattern'], code, re.MULTILINE | re.DOTALL)

            for match in matches:
                line_num = code[:match.start()].count('\n') + 1

                optimization = {
                    'type': rule_name,
                    'line': line_num,
                    'original': match.group(),
                    'suggestion': rule['suggestion'],
                    'confidence': rule['confidence'],
                    'impact': self._estimate_impact(rule_name)
                }

                # Generate optimized code if possible
                try:
                    if callable(rule['replacement']):
                        optimization['optimized'] = rule['replacement'](match)
                    else:
                        optimization['optimized'] = rule['replacement']
                except Exception as e:
                    optimization['optimized'] = "Manual optimization required"

                optimizations.append(optimization)

        return optimizations

    def _find_performance_issues(self, code: str) -> List[Dict]:
        """Find performance issues"""
        issues = []

        for category, patterns in self.performance_patterns.items():
            for pattern in patterns:
                matches = re.finditer(pattern, code, re.MULTILINE)

                for match in matches:
                    line_num = code[:match.start()].count('\n') + 1

                    issue = {
                        'category': category,
                        'line': line_num,
                        'code': match.group(),
                        'severity': self._get_performance_severity(category),
                        'recommendation': self._get_performance_recommendation(category)
                    }

                    issues.append(issue)

        return issues

    def _find_security_issues(self, code: str) -> List[Dict]:
        """Find security vulnerabilities"""
        issues = []

        for category, patterns in self.security_patterns.items():
            for pattern in patterns:
                matches = re.finditer(pattern, code, re.MULTILINE)

                for match in matches:
                    line_num = code[:match.start()].count('\n') + 1

                    issue = {
                        'category': category,
                        'line': line_num,
                        'code': match.group(),
                        'severity': 'high',
                        'recommendation': self._get_security_recommendation(category)
                    }

                    issues.append(issue)

        return issues

    def _generate_suggestions(self, code: str) -> List[Dict]:
        """Generate AI-powered improvement suggestions"""
        suggestions = []

        # Analyze imports
        if 'import *' in code:
            suggestions.append({
                'type': 'import_optimization',
                'message': 'Avoid wildcard imports for better code clarity',
                'priority': 'medium'
            })

        # Analyze function length
        functions = re.findall(r'def\s+\w+.*?(?=def|\Z)', code, re.DOTALL)
        for func in functions:
            if len(func.splitlines()) > 50:
                suggestions.append({
                    'type': 'function_length',
                    'message': 'Consider breaking down large functions',
                    'priority': 'low'
                })

        # Analyze error handling
        if 'try:' in code and 'except:' in code:
            if 'logging' not in code:
                suggestions.append({
                    'type': 'error_logging',
                    'message': 'Add logging for better error tracking',
                    'priority': 'medium'
                })

        # Analyze documentation
        docstring_count = len(re.findall(r'""".*?"""', code, re.DOTALL))
        function_count = len(re.findall(r'def\s+\w+', code))

        if function_count > 0 and docstring_count / function_count < 0.5:
            suggestions.append({
                'type': 'documentation',
                'message': 'Add docstrings to functions for better maintainability',
                'priority': 'low'
            })

        return suggestions

    def _calculate_quality_score(self, analysis: Dict) -> float:
        """Calculate overall code quality score (0-100)"""
        score = 100.0

        # Deduct for issues
        score -= len(analysis['security_issues']) * 15  # Security is critical
        score -= len(analysis['performance_issues']) * 5
        score -= len([o for o in analysis['optimizations'] if o['confidence'] > 0.8]) * 3

        # Bonus for good practices
        metrics = analysis['metrics']
        if metrics['comment_lines'] / max(metrics['code_lines'], 1) > 0.1:
            score += 5  # Good commenting

        if metrics['functions'] > 0:
            score += 5  # Modular code

        return max(0, min(100, score))

    def _estimate_impact(self, rule_name: str) -> str:
        """Estimate optimization impact"""
        impact_map = {
            'loop_optimization': 'medium',
            'string_concatenation': 'high',
            'list_comprehension': 'medium',
            'exception_handling': 'low',
            'memory_optimization': 'high'
        }
        return impact_map.get(rule_name, 'low')

    def _get_performance_severity(self, category: str) -> str:
        """Get performance issue severity"""
        severity_map = {
            'cpu_intensive': 'high',
            'memory_intensive': 'medium',
            'io_intensive': 'medium'
        }
        return severity_map.get(category, 'low')

    def _get_performance_recommendation(self, category: str) -> str:
        """Get performance recommendations"""
        recommendations = {
            'cpu_intensive': 'Add sleep delays or optimize algorithm',
            'memory_intensive': 'Use generators or process data in chunks',
            'io_intensive': 'Use async operations or connection pooling'
        }
        return recommendations.get(category, 'Review and optimize')

    def _get_security_recommendation(self, category: str) -> str:
        """Get security recommendations"""
        recommendations = {
            'code_injection': 'Never use eval/exec with user input',
            'path_traversal': 'Validate and sanitize file paths',
            'hardcoded_secrets': 'Use environment variables or secure vaults'
        }
        return recommendations.get(category, 'Review security implications')

    def optimize_code(self, code: str) -> Tuple[str, List[Dict]]:
        """Apply AI optimizations to code"""
        optimized_code = code
        applied_optimizations = []

        analysis = self.analyze_code(code)

        # Apply high-confidence optimizations
        for opt in analysis['optimizations']:
            if opt['confidence'] > 0.8 and opt['optimized'] != "Manual optimization required":
                try:
                    optimized_code = optimized_code.replace(opt['original'], opt['optimized'])
                    applied_optimizations.append(opt)
                except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        return optimized_code, applied_optimizations

    def generate_report(self, analysis: Dict) -> str:
        """Generate human-readable optimization report"""
        report = f"""
🤖 AI Code Analysis Report
========================

📁 File: {analysis['filename']}
📅 Date: {analysis['timestamp']}
⭐ Quality Score: {analysis['overall_score']:.1f}/100

📊 Code Metrics:
• Total lines: {analysis['metrics']['total_lines']}
• Code lines: {analysis['metrics']['code_lines']}
• Functions: {analysis['metrics']['functions']}
• Classes: {analysis['metrics']['classes']}
• Complexity: {analysis['metrics']['complexity_estimate']}

🔧 Optimizations Found: {len(analysis['optimizations'])}
"""

        if analysis['optimizations']:
            report = f"{report}{"\n🔧 Optimization Opportunities:\n"}"
            for i, opt in enumerate(analysis['optimizations'][:5], 1):
                report += f"{i}. {opt['suggestion']} (Line {opt['line']}, Confidence: {opt['confidence']:.1%})\n"

        if analysis['performance_issues']:
            report += f"\n⚡ Performance Issues: {len(analysis['performance_issues'])}\n"
            for issue in analysis['performance_issues'][:3]:
                report += f"• {issue['category']} (Line {issue['line']}): {issue['recommendation']}\n"

        if analysis['security_issues']:
            report += f"\n🔒 Security Issues: {len(analysis['security_issues'])}\n"
            for issue in analysis['security_issues']:
                report += f"• {issue['category']} (Line {issue['line']}): {issue['recommendation']}\n"

        if analysis['suggestions']:
            report += f"\n💡 Suggestions: {len(analysis['suggestions'])}\n"
            for suggestion in analysis['suggestions'][:3]:
                report += f"• {suggestion['message']} (Priority: {suggestion['priority']})\n"

        return report

# Helper functions for optimization rules
def _optimize_range_len(match):
    """Optimize range(len()) patterns"""
    if not all([match]):
        raise ValueError("Invalid parameters")
    return match.group().replace('range(len(', 'enumerate(')

def _optimize_string_concat(match):
    """Optimize string concatenation"""
    if not all([match]):
        raise ValueError("Invalid parameters")
    return "# Consider using f-strings or join() for better performance"

def _create_list_comprehension(match):
    """Create list comprehension from loop"""
    if not all([match]):
        raise ValueError("Invalid parameters")
    return "# Convert to list comprehension for better performance"

def _optimize_file_reading(match):
    """Optimize file reading"""
    if not all([match]):
        raise ValueError("Invalid parameters")
    return match.group() + "  # Consider streaming for large files"

if __name__ == "__main__":
    # Example usage
    optimizer = AICodeOptimizer()

    sample_code = '''
def process_data(items):
    if not all([items]):
        raise ValueError("Invalid parameters")
    result = []
    for i in items:
    if items[i] > 0:
            result.append(i * 2)
    return result

def unsafe_function(user_input):
    if not all([user_input]):
        raise ValueError("Invalid parameters")
    return eval(user_input)
    '''

    print("🤖 AI Code Optimizer Demo")
    print("=" * 40)

    analysis = optimizer.analyze_code(sample_code, "demo.py")
    print(optimizer.generate_report(analysis))

    optimized, applied = optimizer.optimize_code(sample_code)
    print(f"\n✅ Applied {len(applied)} optimizations")
