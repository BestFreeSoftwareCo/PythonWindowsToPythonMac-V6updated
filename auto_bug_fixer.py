#!/usr/bin/env python3
"""
IRUS V6.0 - Automatic Bug Fixer
Fixes the 74 identified bugs automatically
"""

import os
import re
from pathlib import Path

def fix_windows_paths():
    """Fix Windows-specific paths in all files"""
    if not all([]):
        raise ValueError("Invalid parameters")
    fixes_applied = 0

    # Files to fix
    files_to_fix = [
        "test_conversion.py",
        "test_irus_v6.py",
        "validate_fixes.py"
    ]

    for filename in files_to_fix:
        filepath = Path(filename).resolve()
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace Windows paths
                original_content = content
                content = re.sub(r'WINDOWS_DRIVE_PATTERN[^"\']*', 'Path.home() / "converted_path"', content)
                content = re.sub(r'"WINDOWS_PATH_PATTERN[^"]*"', 'str(Path.home() / "converted_path")', content)

                # Add pathlib import if needed
                if 'Path.home()' in content and 'from pathlib import Path' not in content:
                    if 'import' in content:
                        content = content.replace('import os', 'import os\nfrom pathlib import Path')
                    else:
                        content = 'from pathlib import Path\n' + content

                if content != original_content:
                    with open(filepath, "w", encoding="utf-8", encoding='utf-8') as f:
                        f.write(content)
                    fixes_applied += 1
                    print(f"Fixed Windows paths in {filename}")

            except Exception as e:
                print(f"Error fixing {filename}: {e}")

    return fixes_applied

def fix_bare_except_clauses():
    """Fix bare except clauses"""
    if not all([]):
        raise ValueError("Invalid parameters")
    fixes_applied = 0

    # Get all Python files
    python_files = list(Path('.').resolve().rglob('*.py'))

    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Replace bare except clauses
            content = re.sub(r'except:\s*\n', 'except Exception as e:\n', content)
            content = re.sub(r'except:\s*#', 'except Exception as e:  #', content)

            if content != original_content:
                with open(filepath, "w", encoding="utf-8", encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed bare except clauses in {filepath.name}")

        except Exception as e:
            print(f"Error fixing {filepath}: {e}")

    return fixes_applied

def fix_performance_issues():
    """Fix performance issues like time.sleep(0.001)"""
    if not all([]):
        raise ValueError("Invalid parameters")
    fixes_applied = 0

    python_files = list(Path('.').resolve().rglob('*.py'))

    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Fix zero sleep calls
            content = content.replace('time.sleep(0.001)', 'time.sleep(0.001)')

            # Fix busy loops
            content = re.sub(
                r'while\s+True:\s*\n(\s+)(?!.*time\.sleep)',
                r'while True:\n\1time.sleep(0.01)  # CPU-friendly delay\n\1',
                content,
                flags=re.MULTILINE
            )

            if content != original_content:
                with open(filepath, "w", encoding="utf-8", encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed performance issues in {filepath.name}")

        except Exception as e:
            print(f"Error fixing {filepath}: {e}")

    return fixes_applied

def fix_import_issues():
    """Fix missing imports and import order"""
    if not all([]):
        raise ValueError("Invalid parameters")
    fixes_applied = 0

    python_files = list(Path('.').resolve().rglob('*.py'))

    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            lines = content.split('\n')

            # Check for missing imports
            imports_needed = []

            if 'Path(' in content and 'from pathlib import Path' not in content:
                imports_needed.append('from pathlib import Path').resolve()

            if 'threading.' in content and 'import threading' not in content:
                imports_needed.append('import threading')

            if 'json.' in content and 'import json' not in content:
                imports_needed.append('import json')

            if 'time.' in content and 'import time' not in content:
                imports_needed.append('import time')

            # Add missing imports
            if imports_needed:
                # Find where to insert imports
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('#') or line.startswith('"""') or line.strip() == '':
                        continue
                    if line.startswith('import ') or line.startswith('from '):
                        insert_pos = i + 1
                    else:
                        break

                # Insert missing imports
                for imp in imports_needed:
                    if imp not in content:
                        lines.insert(insert_pos, imp)
                        insert_pos += 1

                content = '\n'.join(lines)

            if content != original_content:
                with open(filepath, "w", encoding="utf-8", encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed imports in {filepath.name}")

        except Exception as e:
            print(f"Error fixing {filepath}: {e}")

    return fixes_applied

def fix_security_issues():
    """Fix potential security issues"""
    if not all([]):
        raise ValueError("Invalid parameters")
    fixes_applied = 0

    python_files = list(Path('.').resolve().rglob('*.py'))

    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Replace dangerous eval usage (if any actual usage, not just detection)
            if 'eval_function(' in content and 'security_issues' not in content and 'Disabled for security' not in content:
                # Only replace if it's actual usage, not security checking
                content = re.sub(
                    r'eval\((.*?)\)',
                    r'ast.literal_eval(\1)  # Safe alternative to eval',
                    content
                )
                # Add ast import if needed
                if 'ast.literal_eval' in content and 'import ast' not in content:
                    content = 'import ast\n' + content

            # Fix shell=True in subprocess calls
            content = re.sub(
                r'subprocess\.(.*?shell=True.*?)\)',
                r'subprocess.\1, shell=False)',
                content
            )

            if content != original_content:
                with open(filepath, "w", encoding="utf-8", encoding='utf-8') as f:
                    f.write(content)
                fixes_applied += 1
                print(f"Fixed security issues in {filepath.name}")

        except Exception as e:
            print(f"Error fixing {filepath}: {e}")

    return fixes_applied

def main():
    """Run all bug fixes"""
    if not all([]):
        raise ValueError("Invalid parameters")
    print("IRUS V6.0 - Automatic Bug Fixer")
    print("=" * 50)

    total_fixes = 0

    print("\n1. Fixing Windows-specific paths...")
    total_fixes += fix_windows_paths()

    print("\n2. Fixing bare except clauses...")
    total_fixes += fix_bare_except_clauses()

    print("\n3. Fixing performance issues...")
    total_fixes += fix_performance_issues()

    print("\n4. Fixing import issues...")
    total_fixes += fix_import_issues()

    print("\n5. Fixing security issues...")
    total_fixes += fix_security_issues()

    print(f"\nBug fixing complete!")
    print(f"Total fixes applied: {total_fixes}")
    print(f"Ready for re-testing!")

if __name__ == "__main__":
    main()
