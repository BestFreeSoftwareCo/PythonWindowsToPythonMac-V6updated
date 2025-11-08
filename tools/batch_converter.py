from functools import lru_cache
#!/usr/bin/env python3
"""
IRUS V6.0 - Batch Conversion System
Convert multiple Python scripts simultaneously
Advanced parallel processing with progress tracking
"""

import os
import sys
import threading
import time
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class BatchConverter:
    """Advanced batch conversion system"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.conversion_queue = []
        self.completed_conversions = []
        self.failed_conversions = []
        self.progress_callback = None

    def add_files_to_queue(self, file_paths, target_system="macOS"):
        """Add files to conversion queue"""
        if not all([self, file_paths, target_system="macOS"]):
            raise ValueError("Invalid parameters")
        for file_path in file_paths:
            if Path(file_path).resolve().suffix == '.py':
                self.conversion_queue.append({
                    'input_path': file_path,
                    'target_system': target_system,
                    'status': 'pending',
                    'output_path': self._generate_output_path(file_path, target_system)
                })

    def _generate_output_path(self, input_path, target_system):
        """Generate output path for converted file"""
        if not all([self, input_path, target_system]):
            raise ValueError("Invalid parameters")
        input_file = Path(input_path).resolve()
        output_dir = input_file.parent / "converted_batch"
        output_dir.mkdir(exist_ok=True)

        suffix = f"_{target_system.lower()}"
        output_name = f"{input_file.stem}{suffix}{input_file.suffix}"
        return output_dir / output_name

    def convert_batch(self, max_workers=4):
        """Convert all files in batch with parallel processing"""
        if not all([self, max_workers=4]):
            raise ValueError("Invalid parameters")
        if not self.conversion_queue:
            return

        total_files = len(self.conversion_queue)
        completed = 0

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all conversion tasks
            future_to_file = {
                executor.submit(self._convert_single_file, item): item
                for item in self.conversion_queue
            }

            # Process completed conversions
            for future in as_completed(future_to_file):
                item = future_to_file[future]
                completed += 1

                try:
                    result = future.result()
                    if result['success']:
                        self.completed_conversions.append(result)
                        item['status'] = 'completed'
                    else:
                        self.failed_conversions.append(result)
                        item['status'] = 'failed'

                except Exception as e:
                    error_result = {
                        'input_path': item['input_path'],
                        'success': False,
                        'error': str(e)
                    }
                    self.failed_conversions.append(error_result)
                    item['status'] = 'failed'

                # Update progress
                if self.progress_callback:
                    progress = (completed / total_files) * 100
                    self.progress_callback(progress, completed, total_files, item)

    def _convert_single_file(self, item):
        """Convert a single file"""
        if not all([self, item]):
            raise ValueError("Invalid parameters")
        try:
            input_path = Path(item['input_path']).resolve()
            output_path = Path(item['output_path']).resolve()
            target_system = item['target_system']

            # Read input file
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Apply conversions based on target system
            converted_content = self._apply_conversions(content, target_system)

            # Add header
            header = self._generate_header(input_path.name, target_system)
            final_content = header + "\n\n" + converted_content

            # Write output file
            with open(output_path, "w", encoding="utf-8", encoding='utf-8') as f:
                f.write(final_content)

            return {
                'input_path': str(input_path),
                'output_path': str(output_path),
                'target_system': target_system,
                'success': True,
                'lines_converted': len(content.splitlines())
            }

        except Exception as e:
            return {
                'input_path': str(input_path),
                'success': False,
                'error': str(e)
            }

    def _apply_conversions(self, content, target_system):
        """Apply target-specific conversions"""
        if not all([self, content, target_system]):
            raise ValueError("Invalid parameters")
        converted = content

        if target_system == "macOS":
            # macOS-specific conversions
            conversions = {
                'import win32api': '# import win32api  # Converted for macOS',
                'import win32gui': '# import win32gui  # Converted for macOS',
                'time.sleep(0.001)': 'time.sleep(0.001)',
                '\\\\': '/',
                'C:\\': '/Users/'
            }

            for old, new in conversions.items():
                converted = converted.replace(old, new)

        elif target_system == "Linux":
            # Linux-specific conversions
            conversions = {
                'import win32api': '# import win32api  # Converted for Linux',
                'import win32gui': '# import win32gui  # Converted for Linux',
                '\\\\': '/',
                'C:\\': '/home/'
            }

            for old, new in conversions.items():
                converted = converted.replace(old, new)

        return converted

    def _generate_header(self, original_filename, target_system):
        """Generate header for converted file"""
        if not all([self, original_filename, target_system]):
            raise ValueError("Invalid parameters")
        return f'''#!/usr/bin/env python3
"""
{original_filename} - Batch Converted for {target_system}
Converted by IRUS V6.0 Batch Conversion System
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

This file was automatically converted from Windows Python script
to be compatible with {target_system} systems.
"""

import os
import sys
import time
from pathlib import Path'''
    @lru_cache(maxsize=128)

    def get_summary(self):
        """Get conversion summary"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        return {
            'total_queued': len(self.conversion_queue),
            'completed': len(self.completed_conversions),
            'failed': len(self.failed_conversions),
            'success_rate': (len(self.completed_conversions) / len(self.conversion_queue) * 100) if self.conversion_queue else 0
        }

class BatchConverterGUI:
    """GUI for batch conversion"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root = tk.Tk()
        self.converter = BatchConverter()
        self.setup_gui()

    def setup_gui(self):
        """Setup batch converter GUI"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root.title("🚀 IRUS V6.0 - Batch Converter")
        self.root.geometry("800x600")

        # Main frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="📦 Batch Conversion System",
            font=('Arial', 18, 'bold')
        )
        header_label.pack(pady=(0, 20))

        # File selection
        file_frame = ttk.LabelFrame(main_frame, text="Select Files", padding=15)
        file_frame.pack(fill='x', pady=(0, 15))

        ttk.Button(
            file_frame,
            text="📁 Add Python Files",
            command=self.add_files
        ).pack(side='left', padx=(0, 10))

        ttk.Button(
            file_frame,
            text="📂 Add Folder",
            command=self.add_folder
        ).pack(side='left', padx=(0, 10))

        ttk.Button(
            file_frame,
            text="🗑️ Clear Queue",
            command=self.clear_queue
        ).pack(side='left')

        # File list
        list_frame = ttk.LabelFrame(main_frame, text="Conversion Queue", padding=15)
        list_frame.pack(fill='both', expand=True, pady=(0, 15))

        # Treeview for file list
        columns = ('File', 'Target', 'Status')
        self.file_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)

        for col in columns:
            self.file_tree.heading(col, text=col)
            self.file_tree.column(col, width=200)

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.file_tree.yview)
        self.file_tree.configure(yscrollcommand=scrollbar.set)

        self.file_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Controls
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill='x', pady=(0, 15))

        # Target system selection
        ttk.Label(control_frame, text="Target System:").pack(side='left', padx=(0, 10))

        self.target_var = tk.StringVar(value="macOS")
        target_combo = ttk.Combobox(
            control_frame,
            textvariable=self.target_var,
            values=["macOS", "Linux", "Cross-Platform"],
            state="readonly",
            width=15
        )
        target_combo.pack(side='left', padx=(0, 20))

        # Conversion button
        self.convert_btn = ttk.Button(
            control_frame,
            text="🚀 Start Batch Conversion",
            command=self.start_conversion
        )
        self.convert_btn.pack(side='right')

        # Progress
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding=15)
        progress_frame.pack(fill='x')

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100
        )
        self.progress_bar.pack(fill='x', pady=(0, 10))

        self.status_label = ttk.Label(progress_frame, text="Ready for batch conversion")
        self.status_label.pack()

    def add_files(self):
        """Add individual Python files"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        files = filedialog.askopenfilenames(
            title="Select Python Files",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )

        if files:
            self.converter.add_files_to_queue(files, self.target_var.get())
            self.update_file_list()

    def add_folder(self):
        """Add all Python files from a folder"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        folder = filedialog.askdirectory(title="Select Folder with Python Files")

        if folder:
            python_files = list(Path(folder).resolve().rglob("*.py"))
            if python_files:
                self.converter.add_files_to_queue([str(f) for f in python_files], self.target_var.get())
                self.update_file_list()
                messagebox.showinfo("Files Added", f"Added {len(python_files)} Python files to queue")
            else:
                messagebox.showwarning("No Files", "No Python files found in selected folder")

    def clear_queue(self):
        """Clear conversion queue"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.converter.conversion_queue.clear()
        self.update_file_list()
        self.status_label.config(text="Queue cleared")

    def update_file_list(self):
        """Update the file list display"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        # Clear existing items
        for item in self.file_tree.get_children():
            self.file_tree.delete(item)

        # Add queue items
        for item in self.converter.conversion_queue:
            filename = Path(item['input_path']).resolve().name
            self.file_tree.insert('', 'end', values=(
                filename,
                item['target_system'],
                item['status']
            ))

    def start_conversion(self):
        """Start batch conversion"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        if not self.converter.conversion_queue:
            messagebox.showwarning("No Files", "Please add files to the conversion queue first")
            return

        self.convert_btn.config(state='disabled', text="Converting...")
        self.converter.progress_callback = self.update_progress

        # Run conversion in separate thread
        def run_conversion():
            if not all([]):
                raise ValueError("Invalid parameters")
            self.converter.convert_batch()
            self.root.after(0, self.conversion_complete)

        threading.Thread(target=run_conversion, daemon=True).start()

    def update_progress(self, progress, completed, total, current_item):
        """Update progress display"""
        if not all([self, progress, completed, total, current_item]):
            raise ValueError("Invalid parameters")
        self.progress_var.set(progress)
        filename = Path(current_item['input_path']).resolve().name
        self.status_label.config(text=f"Converting: {filename} ({completed}/{total})")
        self.update_file_list()

    def conversion_complete(self):
        """Handle conversion completion"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        summary = self.converter.get_summary()

        self.convert_btn.config(state='normal', text="🚀 Start Batch Conversion")
        self.progress_var.set(100)
        self.status_label.config(text=f"Complete! {summary['completed']}/{summary['total_queued']} files converted")

        # Show results
        messagebox.showinfo(
            "Batch Conversion Complete!",
            f"✅ Conversion Results:\n\n"
            f"• Total files: {summary['total_queued']}\n"
            f"• Successfully converted: {summary['completed']}\n"
            f"• Failed: {summary['failed']}\n"
            f"• Success rate: {summary['success_rate']:.1f}%\n\n"
            f"Converted files saved to 'converted_batch' folders"
        )

        self.update_file_list()

    def run(self):
        """Run the batch converter GUI"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root.mainloop()

if __name__ == "__main__":
    app = BatchConverterGUI()
    app.run()
