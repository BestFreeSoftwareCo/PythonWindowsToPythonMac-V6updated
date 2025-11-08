from functools import lru_cache
#!/usr/bin/env python3
"""
IRUS V6.0 - Custom Template Manager
Create, edit, and share conversion templates
Advanced template system with community sharing
"""

import json
import time
import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
try:
    import requests
except ImportError:
    requests = None
    print("Warning: requests module not available - Discord features disabled")

class TemplateManager:
    """Advanced template management system"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.templates_dir = Path("templates").resolve()
        self.templates_dir.mkdir(exist_ok=True)
        self.templates = {}
        self.load_templates()

    def load_templates(self):
        """Load all templates from disk"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.templates = {}

        # Load built-in templates
        self.templates.update(self._get_builtin_templates())

        # Load user templates
        for template_file in self.templates_dir.glob("*.json"):
            try:
                with open(template_file, 'r') as f:
                    template_data = json.load(f)
                    self.templates[template_data['name']] = template_data
            except Exception as e:
                print(f"Error loading template {template_file}: {e}")

    def _get_builtin_templates(self):
        """Get built-in conversion templates"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        return {
            "Basic macOS": {
                "name": "Basic macOS",
                "description": "Basic Windows to macOS conversion",
                "author": "IRUS Team",
                "version": "1.0",
                "created": "2025-01-01",
                "category": "macOS",
                "rules": [
                    {
                        "type": "import_replacement",
                        "pattern": "import win32api",
                        "replacement": "# import win32api  # Not available on macOS",
                        "description": "Replace Windows-specific imports"
                    },
                    {
                        "type": "path_conversion",
                        "pattern": r"C:\\\\",
                        "replacement": "/Users/",
                        "description": "Convert Windows paths to macOS"
                    },
                    {
                        "type": "performance_fix",
                        "pattern": "time.sleep(0.001)",
                        "replacement": "time.sleep(0.001)",
                        "description": "Fix zero-delay sleep calls"
                    }
                ]
            },
            "Gaming Macro": {
                "name": "Gaming Macro",
                "description": "Specialized template for gaming macros",
                "author": "IRUS Team",
                "version": "1.0",
                "created": "2025-01-01",
                "category": "Gaming",
                "rules": [
                    {
                        "type": "input_replacement",
                        "pattern": "import win32gui",
                        "replacement": "from pynput import mouse, keyboard",
                        "description": "Replace Windows input with cross-platform"
                    },
                    {
                        "type": "screen_capture",
                        "pattern": "import win32ui",
                        "replacement": "from PIL import ImageGrab",
                        "description": "Replace Windows screen capture"
                    }
                ]
            },
            "Web Automation": {
                "name": "Web Automation",
                "description": "Template for web automation scripts",
                "author": "IRUS Team",
                "version": "1.0",
                "created": "2025-01-01",
                "category": "Web",
                "rules": [
                    {
                        "type": "browser_setup",
                        "pattern": "webdriver.Chrome()",
                        "replacement": "webdriver.Chrome(options=chrome_options)",
                        "description": "Add Chrome options for better compatibility"
                    }
                ]
            }
        }

    def create_template(self, name, description, author, category, rules):
        """Create a new custom template"""
        if not all([self, name, description, author, category, rules]):
            raise ValueError("Invalid parameters")
        template = {
            "name": name,
            "description": description,
            "author": author,
            "version": "1.0",
            "created": time.strftime('%Y-%m-%d'),
            "category": category,
            "rules": rules
        }

        # Save to file
        filename = self.templates_dir / f"{name.replace(' ', '_').lower()}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(template, f, indent=2)

        # Add to memory
        self.templates[name] = template

        return template

    def apply_template(self, code, template_name):
        """Apply a template to code"""
        if not all([self, code, template_name]):
            raise ValueError("Invalid parameters")
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found")

        template = self.templates[template_name]
        modified_code = code
        applied_rules = []

        for rule in template['rules']:
            try:
                import re
                pattern = rule['pattern']
                replacement = rule['replacement']

                if rule['type'] == 'regex':
                    modified_code = re.sub(pattern, replacement, modified_code)
                else:
                    modified_code = modified_code.replace(pattern, replacement)

                # Check if rule was applied
                if pattern in code and pattern not in modified_code:
                    applied_rules.append(rule)

            except Exception as e:
                print(f"Error applying rule {rule}: {e}")

        return modified_code, applied_rules
    @lru_cache(maxsize=128)

    def get_template_list(self):
        """Get list of available templates"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        return list(self.templates.keys())
    @lru_cache(maxsize=128)

    def get_template(self, name):
        """Get specific template"""
        if not all([self, name]):
            raise ValueError("Invalid parameters")
        return self.templates.get(name)

    def delete_template(self, name):
        """Delete a custom template"""
        if not all([self, name]):
            raise ValueError("Invalid parameters")
        if name in self.templates:
            # Don't delete built-in templates
            if self.templates[name].get('author') == 'IRUS Team':
                raise ValueError("Cannot delete built-in templates")

            # Delete file
            filename = self.templates_dir / f"{name.replace(' ', '_').lower()}.json"
            if filename.exists():
                filename.unlink()

            # Remove from memory
            del self.templates[name]

    def export_template(self, name, filepath):
        """Export template to file"""
        if not all([self, name, filepath]):
            raise ValueError("Invalid parameters")
        if name not in self.templates:
            raise ValueError(f"Template '{name}' not found")

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.templates[name], f, indent=2)

    def import_template(self, filepath):
        """Import template from file"""
        if not all([self, filepath]):
            raise ValueError("Invalid parameters")
        with open(filepath, 'r') as f:
            template_data = json.load(f)

        # Validate template
        required_fields = ['name', 'description', 'rules']
        for field in required_fields:
            if field not in template_data:
                raise ValueError(f"Template missing required field: {field}")

        # Add to templates
        name = template_data['name']
        self.templates[name] = template_data

        # Save to templates directory
        filename = self.templates_dir / f"{name.replace(' ', '_').lower()}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(template_data, f, indent=2)

        return template_data

class TemplateManagerGUI:
    """GUI for template management"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root = tk.Tk()
        self.manager = TemplateManager()
        self.setup_gui()

    def setup_gui(self):
        """Setup template manager GUI"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root.title("📝 IRUS V6.0 - Template Manager")
        self.root.geometry("900x700")

        # Main frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="📝 Custom Conversion Templates",
            font=('Arial', 18, 'bold')
        )
        header_label.pack(pady=(0, 20))

        # Create notebook
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True)

        # Templates list tab
        self.create_templates_tab()

        # Create template tab
        self.create_new_template_tab()

        # Template editor tab
        self.create_editor_tab()

    def create_templates_tab(self):
        """Create templates list tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        templates_frame = ttk.Frame(self.notebook)
        self.notebook.add(templates_frame, text="📋 Templates")

        # Controls
        controls_frame = ttk.Frame(templates_frame)
        controls_frame.pack(fill='x', pady=(0, 15))

        ttk.Button(
            controls_frame,
            text="🔄 Refresh",
            command=self.refresh_templates
        ).pack(side='left', padx=(0, 10))

        ttk.Button(
            controls_frame,
            text="📥 Import",
            command=self.import_template
        ).pack(side='left', padx=(0, 10))

        ttk.Button(
            controls_frame,
            text="📤 Export",
            command=self.export_template
        ).pack(side='left', padx=(0, 10))

        ttk.Button(
            controls_frame,
            text="🗑️ Delete",
            command=self.delete_template
        ).pack(side='left')

        # Templates list
        list_frame = ttk.LabelFrame(templates_frame, text="Available Templates", padding=15)
        list_frame.pack(fill='both', expand=True)

        # Treeview for templates
        columns = ('Name', 'Category', 'Author', 'Rules', 'Created')
        self.templates_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)

        for col in columns:
            self.templates_tree.heading(col, text=col)
            self.templates_tree.column(col, width=150)

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.templates_tree.yview)
        self.templates_tree.configure(yscrollcommand=scrollbar.set)

        self.templates_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Template details
        details_frame = ttk.LabelFrame(templates_frame, text="Template Details", padding=15)
        details_frame.pack(fill='x', pady=(15, 0))

        self.details_text = tk.Text(details_frame, height=8, font=('Courier', 10))
        details_scrollbar = ttk.Scrollbar(details_frame, orient='vertical', command=self.details_text.yview)
        self.details_text.configure(yscrollcommand=details_scrollbar.set)

        self.details_text.pack(side='left', fill='both', expand=True)
        details_scrollbar.pack(side='right', fill='y')

        # Bind selection event
        self.templates_tree.bind('<<TreeviewSelect>>', self.on_template_select)

        # Load templates
        self.refresh_templates()

    def create_new_template_tab(self):
        """Create new template tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        new_frame = ttk.Frame(self.notebook)
        self.notebook.add(new_frame, text="➕ Create New")

        # Template info
        info_frame = ttk.LabelFrame(new_frame, text="Template Information", padding=15)
        info_frame.pack(fill='x', pady=(0, 15))

        # Name
        ttk.Label(info_frame, text="Template Name:").grid(row=0, column=0, sticky='w', pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.name_var, width=40).grid(row=0, column=1, sticky='ew', padx=(10, 0))

        # Description
        ttk.Label(info_frame, text="Description:").grid(row=1, column=0, sticky='w', pady=5)
        self.desc_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.desc_var, width=40).grid(row=1, column=1, sticky='ew', padx=(10, 0))

        # Author
        ttk.Label(info_frame, text="Author:").grid(row=2, column=0, sticky='w', pady=5)
        self.author_var = tk.StringVar(value="User")
        ttk.Entry(info_frame, textvariable=self.author_var, width=40).grid(row=2, column=1, sticky='ew', padx=(10, 0))

        # Category
        ttk.Label(info_frame, text="Category:").grid(row=3, column=0, sticky='w', pady=5)
        self.category_var = tk.StringVar()
        category_combo = ttk.Combobox(
            info_frame,
            textvariable=self.category_var,
            values=["macOS", "Linux", "Gaming", "Web", "Automation", "Custom"],
            width=37
        )
        category_combo.grid(row=3, column=1, sticky='ew', padx=(10, 0))

        info_frame.columnconfigure(1, weight=1)

        # Rules
        rules_frame = ttk.LabelFrame(new_frame, text="Conversion Rules", padding=15)
        rules_frame.pack(fill='both', expand=True, pady=(0, 15))

        # Rules list
        rules_list_frame = ttk.Frame(rules_frame)
        rules_list_frame.pack(fill='both', expand=True)

        columns = ('Type', 'Pattern', 'Replacement', 'Description')
        self.rules_tree = ttk.Treeview(rules_list_frame, columns=columns, show='headings', height=10)

        for col in columns:
            self.rules_tree.heading(col, text=col)
            self.rules_tree.column(col, width=180)

        rules_scrollbar = ttk.Scrollbar(rules_list_frame, orient='vertical', command=self.rules_tree.yview)
        self.rules_tree.configure(yscrollcommand=rules_scrollbar.set)

        self.rules_tree.pack(side='left', fill='both', expand=True)
        rules_scrollbar.pack(side='right', fill='y')

        # Rule controls
        rule_controls = ttk.Frame(rules_frame)
        rule_controls.pack(fill='x', pady=(10, 0))

        ttk.Button(rule_controls, text="➕ Add Rule", command=self.add_rule).pack(side='left', padx=(0, 10))
        ttk.Button(rule_controls, text="✏️ Edit Rule", command=self.edit_rule).pack(side='left', padx=(0, 10))
        ttk.Button(rule_controls, text="🗑️ Remove Rule", command=self.remove_rule).pack(side='left')

        # Create template button
        create_frame = ttk.Frame(new_frame)
        create_frame.pack(fill='x')

        ttk.Button(
            create_frame,
            text="✅ Create Template",
            command=self.create_template
        ).pack(side='right')

    def create_editor_tab(self):
        """Create template editor tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        editor_frame = ttk.Frame(self.notebook)
        self.notebook.add(editor_frame, text="✏️ Editor")

        ttk.Label(
            editor_frame,
            text="Advanced template editor coming soon!",
            font=('Arial', 14)
        ).pack(expand=True)

    def refresh_templates(self):
        """Refresh templates list"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.manager.load_templates()

        # Clear existing items
        for item in self.templates_tree.get_children():
            self.templates_tree.delete(item)

        # Add templates
        for name, template in self.manager.templates.items():
            self.templates_tree.insert('', 'end', values=(
                name,
                template.get('category', 'Unknown'),
                template.get('author', 'Unknown'),
                len(template.get('rules', [])),
                template.get('created', 'Unknown')
            ))

    def on_template_select(self, event):
        """Handle template selection"""
        if not all([self, event]):
            raise ValueError("Invalid parameters")
        selection = self.templates_tree.selection()
        if not selection:
            return

        item = self.templates_tree.item(selection[0])
        template_name = item['values'][0]

        template = self.manager.get_template(template_name)
        if template:
            details = f"Template: {template['name']}\n"
            details += f"Description: {template['description']}\n"
            details += f"Author: {template.get('author', 'Unknown')}\n"
            details += f"Category: {template.get('category', 'Unknown')}\n"
            details += f"Version: {template.get('version', '1.0')}\n"
            details += f"Created: {template.get('created', 'Unknown')}\n\n"
            details += f"Rules ({len(template['rules'])}):\n"
            details = f"{details}{"-"}" * 40 + "\n"

            for i, rule in enumerate(template['rules'], 1):
                details += f"{i}. {rule.get('description', 'No description')}\n"
                details += f"   Type: {rule.get('type', 'Unknown')}\n"
                details += f"   Pattern: {rule.get('pattern', '')}\n"
                details += f"   Replacement: {rule.get('replacement', '')}\n\n"

            self.details_text.delete('1.0', tk.END)
            self.details_text.insert('1.0', details)

    def add_rule(self):
        """Add new rule dialog"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.rule_dialog("Add Rule")

    def edit_rule(self):
        """Edit selected rule"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        selection = self.rules_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a rule to edit")
            return

        self.rule_dialog("Edit Rule", selection[0])

    def rule_dialog(self, title, item_id=None):
        """Show rule creation/editing dialog"""
        if not all([self, title, item_id=None]):
            raise ValueError("Invalid parameters")
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("500x400")
        dialog.transient(self.root)
        dialog.grab_set()

        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (400 // 2)
        dialog.geometry(f"500x400+{x}+{y}")

        # Rule form
        form_frame = ttk.Frame(dialog, padding=20)
        form_frame.pack(fill='both', expand=True)

        # Type
        ttk.Label(form_frame, text="Rule Type:").grid(row=0, column=0, sticky='w', pady=5)
        type_var = tk.StringVar()
        type_combo = ttk.Combobox(
            form_frame,
            textvariable=type_var,
            values=["import_replacement", "path_conversion", "performance_fix", "regex", "simple_replace"],
            width=30
        )
        type_combo.grid(row=0, column=1, sticky='ew', padx=(10, 0))

        # Pattern
        ttk.Label(form_frame, text="Pattern:").grid(row=1, column=0, sticky='w', pady=5)
        pattern_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=pattern_var, width=40).grid(row=1, column=1, sticky='ew', padx=(10, 0))

        # Replacement
        ttk.Label(form_frame, text="Replacement:").grid(row=2, column=0, sticky='w', pady=5)
        replacement_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=replacement_var, width=40).grid(row=2, column=1, sticky='ew', padx=(10, 0))

        # Description
        ttk.Label(form_frame, text="Description:").grid(row=3, column=0, sticky='w', pady=5)
        desc_text = tk.Text(form_frame, height=4, width=40)
        desc_text.grid(row=3, column=1, sticky='ew', padx=(10, 0))

        form_frame.columnconfigure(1, weight=1)

        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(20, 0))

        def save_rule():
            if not all([]):
                raise ValueError("Invalid parameters")
            rule = {
                'type': type_var.get(),
                'pattern': pattern_var.get(),
                'replacement': replacement_var.get(),
                'description': desc_text.get('1.0', 'end-1c')
            }

            if not all([rule['type'], rule['pattern'], rule['replacement']]):
                messagebox.showwarning("Missing Fields", "Please fill in all required fields")
                return

            if item_id:
                # Edit existing rule
                self.rules_tree.item(item_id, values=(
                    rule['type'], rule['pattern'], rule['replacement'], rule['description']
                ))
            else:
                # Add new rule
                self.rules_tree.insert('', 'end', values=(
                    rule['type'], rule['pattern'], rule['replacement'], rule['description']
                ))

            dialog.destroy()

        ttk.Button(button_frame, text="💾 Save", command=save_rule).pack(side='right', padx=(10, 0))
        ttk.Button(button_frame, text="❌ Cancel", command=dialog.destroy).pack(side='right')

    def remove_rule(self):
        """Remove selected rule"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        selection = self.rules_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a rule to remove")
            return

        self.rules_tree.delete(selection[0])

    def create_template(self):
        """Create new template"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        name = self.name_var.get().strip()
        description = self.desc_var.get().strip()
        author = self.author_var.get().strip()
        category = self.category_var.get().strip()

        if not all([name, description, category]):
            messagebox.showwarning("Missing Information", "Please fill in all template information")
            return

        # Get rules
        rules = []
        for item in self.rules_tree.get_children():
            values = self.rules_tree.item(item)['values']
            rule = {
                'type': values[0],
                'pattern': values[1],
                'replacement': values[2],
                'description': values[3]
            }
            rules.append(rule)

        if not rules:
            messagebox.showwarning("No Rules", "Please add at least one conversion rule")
            return

        try:
            template = self.manager.create_template(name, description, author, category, rules)
            messagebox.showinfo("Template Created", f"Template '{name}' created successfully!")

            # Clear form
            self.name_var.set("")
            self.desc_var.set("")
            self.category_var.set("")

            # Clear rules
            for item in self.rules_tree.get_children():
                self.rules_tree.delete(item)

            # Refresh templates list
            self.refresh_templates()

        except Exception as e:
            messagebox.showerror("Error", f"Could not create template:\n{e}")

    def import_template(self):
        """Import template from file"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        filename = filedialog.askopenfilename(
            title="Import Template",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if filename:
            try:
                template = self.manager.import_template(filename)
                messagebox.showinfo("Template Imported", f"Template '{template['name']}' imported successfully!")
                self.refresh_templates()
            except Exception as e:
                messagebox.showerror("Import Error", f"Could not import template:\n{e}")

    def export_template(self):
        """Export selected template"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        selection = self.templates_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a template to export")
            return

        item = self.templates_tree.item(selection[0])
        template_name = item['values'][0]

        filename = filedialog.asksaveasfilename(
            title="Export Template",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if filename:
            try:
                self.manager.export_template(template_name, filename)
                messagebox.showinfo("Template Exported", f"Template exported to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Could not export template:\n{e}")

    def delete_template(self):
        """Delete selected template"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        selection = self.templates_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a template to delete")
            return

        item = self.templates_tree.item(selection[0])
        template_name = item['values'][0]

        if messagebox.askyesno("Confirm Delete", f"Delete template '{template_name}'?"):
            try:
                self.manager.delete_template(template_name)
                messagebox.showinfo("Template Deleted", f"Template '{template_name}' deleted successfully!")
                self.refresh_templates()
            except Exception as e:
                messagebox.showerror("Delete Error", f"Could not delete template:\n{e}")

    def run(self):
        """Run the template manager GUI"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root.mainloop()

if __name__ == "__main__":
    app = TemplateManagerGUI()
    app.run()
