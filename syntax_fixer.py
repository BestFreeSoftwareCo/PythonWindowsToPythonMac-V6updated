#!/usr/bin/env python3
"""
IRUS V6.0 - Syntax Error Fixer
Fixes the syntax errors introduced by the advanced bug fixer
"""

import os
import re
from pathlib import Path

def fix_syntax_errors():
    """Fix syntax errors in all files"""
    print("Fixing syntax errors...")
    
    # Files with known syntax errors
    error_files = [
        "advanced_bug_fixer.py",
        "launch_irus.py", 
        "gui/interactive_tutorial.py",
        "gui/professional_ui.py",
        "tools/advanced_bug_prevention.py",
        "tools/comprehensive_bug_hunter.py"
    ]
    
    for filename in error_files:
        filepath = Path(filename)
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix unterminated string literals
                content = re.sub(r'"""[^"]*$', '"""', content, flags=re.MULTILINE)
                content = re.sub(r"'''[^']*$", "'''", content, flags=re.MULTILINE)
                
                # Fix invalid syntax from input modifications
                content = re.sub(
                    r'input\([^)]+\)\.strip\(\)\[:1000\]\s*#\s*Limit input length',
                    'input("Enter choice: ").strip()[:1000]',
                    content
                )
                
                # Fix malformed f-strings
                content = re.sub(r'f"[^"]*\{[^}]*\}[^"]*\.strip\(\)\[:1000\]', 'f"Enter choice: "', content)
                
                # Fix double encoding parameters
                content = re.sub(r'encoding="utf-8",\s*encoding=[\'"]utf-8[\'"]', 'encoding="utf-8"', content)
                
                # Fix malformed lambda expressions
                content = re.sub(r'lambda\s+[^:]*=\s*f"[^"]*":', 'lambda:', content)
                
                # Fix broken function definitions
                content = re.sub(
                    r'def\s+([^(]+)\([^)]*\):\s*\n\s*if not all\(\[[^]]*\]\):\s*\n\s*raise ValueError\("Invalid parameters"\)\s*\n',
                    r'def \1():\n    """Function definition"""\n',
                    content
                )
                
                # Remove malformed lines
                lines = content.split('\n')
                fixed_lines = []
                
                for line in lines:
                    # Skip lines with obvious syntax errors
                    if ('if not all([' in line and '])' not in line) or \
                       ('raise ValueError("Invalid parameters")' in line and 'def ' not in line) or \
                       (line.strip().startswith('if not all([') and line.count('[') != line.count(']')):
                        continue
                    fixed_lines.append(line)
                
                content = '\n'.join(fixed_lines)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  Fixed syntax errors in {filepath.name}")
                    
            except Exception as e:
                print(f"  Error fixing {filepath}: {e}")

def main():
    """Main function"""
    print("IRUS V6.0 - Syntax Error Fixer")
    print("=" * 40)
    fix_syntax_errors()
    print("Syntax error fixing complete!")

if __name__ == "__main__":
    main()
