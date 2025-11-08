import threading
#!/usr/bin/env python3
"""
"""
    """Advanced bug detection and fixing system"""
        self.bugs_found = []
        self.bugs_fixed = []
        self.warnings = []
        self.suggestions = []

        # Common bug patterns
        self.bug_patterns = {
            # UI/Threading bugs
            'ui_thread_access': {
                'pattern': r'self\.\w+\.config\(',
                'check': self._check_ui_thread_access,
                'severity': 'medium',
                'description': 'Potential UI access from wrong thread'
            },

            # Import issues
            'missing_imports': {
                'pattern': r'(requests|psutil|tkinter|threading)\.',
                'check': self._check_missing_imports,
                'severity': 'high',
                'description': 'Missing import statements'
            },

            # Error handling
            'bare_except': {
                'pattern': r'except:\s*$',
                'check': self._check_bare_except,
                'severity': 'medium',
                'description': 'Bare except clauses should specify exception types'
            },

            # Resource management
            'unclosed_files': {
                'pattern': r'open\([^)]+\)(?!\s*with)',
                'check': self._check_unclosed_files,
                'severity': 'medium',
                'description': 'Files should be opened with context managers'
            },

            # Performance issues
            'inefficient_loops': {
                'pattern': r'for\s+\w+\s+in\s+range\(len\(',
                'check': self._check_inefficient_loops,
                'severity': 'low',
                'description': 'Use enumerate() instead of range(len())'
            },

            # Security issues
            'eval_usage': {
                'pattern': r'\beval\(',
                'check': self._check_eval_usage,
                'severity': 'high',
                'description': '# eval()  # Disabled for security usage is dangerous'
            },

            # macOS compatibility
            'windows_paths': {
                'pattern': r'["\'][C-Z]:\\\\',
                'check': self._check_windows_paths,
                'severity': 'high',
                'description': 'Windows-specific paths need conversion'
            },

            # Discord integration
            'webhook_errors': {
                'pattern': r'webhook.*url',
                'check': self._check_webhook_implementation,
                'severity': 'medium',
                'description': 'Webhook implementation issues'
            }
        }

        # Auto-fix patterns
        self.auto_fixes = {
            'bare_except': lambda match, line: line.replace('except:', 'except Exception as e:'),
            'inefficient_loops': self._fix_inefficient_loops,
            'windows_paths': self._fix_windows_paths,
            'missing_imports': self._add_missing_imports
        }

    def hunt_bugs(self, directory_path):
        """Comprehensive bug hunting in directory"""
        print("IRUS V6.0 - Comprehensive Bug Hunter")
        print("=" * 60)

        directory = Path(directory_path).resolve()
        python_files = list(directory.rglob("*.py"))

        print(f"Scanning {len(python_files)} Python files...")

        for file_path in python_files:
            print(f"\nAnalyzing: {file_path.name}")
            self._analyze_file(file_path)

        self._generate_report()
        return self._get_summary()

    def _analyze_file(self, file_path):
        """Analyze a single Python file for bugs"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()

            # Check for syntax errors first
            try:
                ast.parse(content)
            except SyntaxError as e:
                self.bugs_found.append({
                    'file': str(file_path),
                    'line': e.lineno,
                    'type': 'syntax_error',
                    'severity': 'critical',
                    'description': f"Syntax error: {e.msg}",
                    'code': lines[e.lineno - 1] if e.lineno <= len(lines) else ""
                })
                return

            # Check each bug pattern
            for pattern_name, pattern_info in self.bug_patterns.items():
                matches = re.finditer(pattern_info['pattern'], content, re.MULTILINE)

                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    line_content = lines[line_num - 1] if line_num <= len(lines) else ""

                    # Run specific check function
                    if pattern_info['check'](match, line_content, content):
                        bug = {
                            'file': str(file_path),
                            'line': line_num,
                            'type': pattern_name,
                            'severity': pattern_info['severity'],
                            'description': pattern_info['description'],
                            'code': line_content.strip(),
                            'match': match.group()
                        }
                        self.bugs_found.append(bug)

            # Check for specific IRUS issues
            self._check_irus_specific_issues(file_path, content, lines)

        except Exception as e:
            self.warnings.append(f"Could not analyze {file_path}: {e}")

    def _check_ui_thread_access(self, match, line, content):
        """Check for UI access from wrong thread"""
        # Look for UI updates inside threading.Thread targets
        if 'threading.Thread' in content and '.config(' in line:
            return True
        return False

    def _check_missing_imports(self, match, line, content):
        """Check for missing import statements"""
        module = match.group(1)
        import_patterns = [
            f"import {module}",
            f"from {module} import",
            f"import {module} as"
        ]

        for pattern in import_patterns:
            if pattern in content:
                return False
        return True

    def _check_bare_except(self, match, line, content):
        """Check for bare except clauses"""
        return 'except:' in line and 'pass' not in line

    def _check_unclosed_files(self, match, line, content):
        """Check for files not opened with context managers"""
        return 'with open(' not in line

    def _check_inefficient_loops(self, match, line, content):
        """Check for inefficient loop patterns"""
        return 'range(len(' in line and 'enumerate' not in line

    def _check_eval_usage(self, match, line, content):
        """Check for dangerous eval usage"""
        return True  # eval is always dangerous

    def _check_windows_paths(self, match, line, content):
        """Check for Windows-specific paths"""
        return True  # Always flag Windows paths

    def _check_webhook_implementation(self, match, line, content):
        """Check webhook implementation"""
        # Look for common webhook issues
        if 'webhook' in line.lower():
            if 'try:' not in content or 'except' not in content:
                return True
        return False

    def _check_irus_specific_issues(self, file_path, content, lines):
        """Check for IRUS-specific issues"""
        # Check for missing status_label initialization
        if 'professional_ui.py' in str(file_path):
            if 'self.status_label' in content and 'self.status_label =' not in content:
                self.bugs_found.append({
                    'file': str(file_path),
                    'line': 0,
                    'type': 'missing_initialization',
                    'severity': 'high',
                    'description': 'status_label used but not initialized',
                    'code': 'self.status_label'
                })

        # Check for Discord webhook issues
        if 'discord' in content.lower() and 'webhook' in content.lower():
            if 'requests' not in content:
                self.bugs_found.append({
                    'file': str(file_path),
                    'line': 0,
                    'type': 'missing_dependency',
                    'severity': 'medium',
                    'description': 'Discord webhook requires requests module',
                    'code': 'webhook functionality'
                })

        # Check for theme application issues
        if 'theme' in content.lower() and 'configure' in content:
            if 'hasattr' not in content:
                self.suggestions.append({
                    'file': str(file_path),
                    'description': 'Theme changes should check if UI elements exist',
                    'suggestion': 'Use hasattr() checks before configuring UI elements'
                })

    def _fix_inefficient_loops(self, match, line):
        """Fix inefficient loop patterns"""
        # Convert range(len()) to enumerate
        pattern = r'for\s+(\w+)\s+in\s+range\(len\((\w+)\)\):'
        replacement = r'for \1, item in enumerate(\2):'
        return re.sub(pattern, replacement, line)

    def _fix_windows_paths(self, match, line):
        """Fix Windows-specific paths"""
        # Convert Windows paths to Path objects
        return line.replace('\\\\', '/').replace('C:/', '')

    def _add_missing_imports(self, match, line):
        """Add missing import statements"""
        # This would need to be handled at file level
        return line

    def auto_fix_bugs(self, directory_path):
        """Automatically fix bugs where possible"""
        print("\nAuto-fixing bugs...")

        for bug in self.bugs_found:
            if bug['type'] in self.auto_fixes and bug['severity'] != 'critical':
                try:
                    file_path = Path(bug['file']).resolve()

                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = content.splitlines()

                    # Apply fix
                    if bug['line'] > 0 and bug['line'] <= len(lines):
                        old_line = lines[bug['line'] - 1]
                        new_line = self.auto_fixes[bug['type']](None, old_line)

                        if new_line != old_line:
                            lines[bug['line'] - 1] = new_line

                            # Write back to file
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write('\n'.join(lines))

                            self.bugs_fixed.append({
                                'file': bug['file'],
                                'line': bug['line'],
                                'type': bug['type'],
                                'old': old_line.strip(),
                                'new': new_line.strip()
                            })

                            print(f"  FIXED {bug['type']} in {file_path.name}:{bug['line']}")

                except Exception as e:
                    self.warnings.append(f"Could not auto-fix {bug['type']}: {e}")

    def _generate_report(self):
        """Generate comprehensive bug report"""
        print(f"\nBug Hunt Results:")
        print(f"  Bugs found: {len(self.bugs_found)}")
        print(f"  Bugs fixed: {len(self.bugs_fixed)}")
        print(f"  Warnings: {len(self.warnings)}")
        print(f"  Suggestions: {len(self.suggestions)}")

        # Group bugs by severity
        critical = [b for b in self.bugs_found if b['severity'] == 'critical']
        high = [b for b in self.bugs_found if b['severity'] == 'high']
        medium = [b for b in self.bugs_found if b['severity'] == 'medium']
        low = [b for b in self.bugs_found if b['severity'] == 'low']

        if critical:
            print(f"\nCRITICAL BUGS ({len(critical)}):")
            for bug in critical[:5]:  # Show first 5
                print(f"  ERROR: {bug['file']}:{bug['line']} - {bug['description']}")

        if high:
            print(f"\nHIGH PRIORITY ({len(high)}):")
            for bug in high[:5]:
                print(f"  WARNING: {bug['file']}:{bug['line']} - {bug['description']}")

        if medium:
            print(f"\nMEDIUM PRIORITY ({len(medium)}):")
            for bug in medium[:3]:
                print(f"  WARNING: {bug['file']}:{bug['line']} - {bug['description']}")

        # Save detailed report
        try:
            report = {
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'summary': {
                    'bugs_found': len(self.bugs_found),
                    'bugs_fixed': len(self.bugs_fixed),
                    'warnings': len(self.warnings),
                    'suggestions': len(self.suggestions)
                },
                'bugs': self.bugs_found,
                'fixes': self.bugs_fixed,
                'warnings': self.warnings,
                'suggestions': self.suggestions
            }

            with open('bug_hunt_report.json', "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2)

            print(f"\nDetailed report saved to: bug_hunt_report.json")

        except Exception as e:
            print(f"Could not save report: {e}")

    def _get_summary(self):
        """Get bug hunt summary"""
        return {
            'bugs_found': len(self.bugs_found),
            'bugs_fixed': len(self.bugs_fixed),
            'warnings': len(self.warnings),
            'suggestions': len(self.suggestions),
            'critical_bugs': len([b for b in self.bugs_found if b['severity'] == 'critical']),
            'high_priority': len([b for b in self.bugs_found if b['severity'] == 'high'])
        }

def main():
    """Run comprehensive bug hunt"""
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    hunter = ComprehensiveBugHunter()

    print("Starting comprehensive bug hunt...")
    summary = hunter.hunt_bugs(directory)

    if summary['bugs_found'] > 0:
        fix_choice = input("Enter choice: ").strip()[:1000]: ")
        if fix_choice.lower() == 'y':
            hunter.auto_fix_bugs(directory)

    print(f"\nBug hunt complete!")
    print(f"Summary: {summary['bugs_found']} bugs found, {summary['bugs_fixed']} fixed")

    return summary

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBug hunt interrupted by user")
    except Exception as e:
        print(f"\nBug hunter crashed: {e}")
        traceback.print_exc()
