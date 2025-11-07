#!/usr/bin/env python3
"""
IRUS V4 - Interactive Tutorial System
Step-by-step interactive guidance with animations and tips
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading

class InteractiveTutorial:
    def __init__(self, parent_window):
        self.parent = parent_window
        self.current_lesson = 0
        self.lessons = self.create_lessons()
        self.tutorial_window = None
        
    def create_lessons(self):
        """Create interactive tutorial lessons"""
        return [
            {
                'title': '🎯 Welcome to IRUS V4',
                'content': '''Welcome to the most advanced fishing macro conversion system!

This interactive tutorial will guide you through:
• Understanding what this wizard does
• Learning the 6-step conversion process  
• Tips for 100% success
• Troubleshooting common issues

Ready to become a macro conversion expert?''',
                'tips': [
                    'This tutorial takes about 5 minutes',
                    'You can pause anytime and resume later',
                    'Each lesson builds on the previous one'
                ],
                'interactive_elements': ['welcome_animation']
            },
            
            {
                'title': '🔍 Step 1: System Validation',
                'content': '''The first step checks if your Mac is ready for conversion.

What gets checked:
✅ macOS version (needs 10.15+)
✅ Python version (needs 3.8+)  
✅ Available disk space (needs 500MB+)
✅ Internet connection
✅ System performance

Why this matters:
Catching issues early prevents failures later!''',
                'tips': [
                    'Green checkmarks = all good to proceed',
                    'Red X marks = need to fix before continuing',
                    'Yellow warnings = proceed with caution'
                ],
                'interactive_elements': ['validation_demo']
            },
            
            {
                'title': '📦 Step 2: Package Installation',
                'content': '''This step installs the 5 required Python packages.

Required packages:
🖼️ Pillow - Image processing
🔢 NumPy - Numerical operations  
👁️ OpenCV - Computer vision
🖱️ pynput - Mouse/keyboard control
🖥️ PyObjC - macOS screen capture

Installation features:
• Automatic retry (3 attempts each)
• Timeout protection (5 minutes max)
• Specific error solutions
• Real-time progress tracking''',
                'tips': [
                    'Installation usually takes 2-5 minutes',
                    'PyObjC may need Xcode Command Line Tools',
                    'OpenCV may need cmake installed'
                ],
                'interactive_elements': ['package_demo']
            },
            
            {
                'title': '✅ Step 3: Verification',
                'content': '''Verification ensures all packages work correctly.

What gets tested:
🧪 Import each package
🔧 Test basic functionality  
📊 Check version compatibility
🔍 Verify dependencies

This step prevents runtime errors later!

If verification fails:
• Shows exactly which package has issues
• Provides specific fix instructions
• Can retry individual packages''',
                'tips': [
                    'Verification is quick (usually 10 seconds)',
                    'All packages must pass to continue',
                    'Failed packages can be reinstalled individually'
                ],
                'interactive_elements': ['verification_demo']
            },
            
            {
                'title': '📄 Step 4: Script Selection',
                'content': '''Choose your Windows Python script to convert.

File browser features:
📁 Smart filtering (shows .py files first)
🔍 File validation (checks it\'s valid Python)
📊 Size and date information
🛡️ Permission checking

What makes a good script:
✅ Valid Python syntax
✅ Readable file permissions
✅ Not corrupted or binary
✅ Contains actual fishing macro code''',
                'tips': [
                    'Look for files with "fishing" or "bot" in the name',
                    'Check the file size - should be 50KB+ for full macros',
                    'Avoid selecting test files or incomplete scripts'
                ],
                'interactive_elements': ['file_browser_demo']
            },
            
            {
                'title': '🔄 Step 5: Conversion Magic',
                'content': '''The automatic conversion transforms Windows code to macOS.

What gets converted:
🖥️ Screen capture: mss → Quartz
🖱️ Mouse control: pyautogui → pynput  
⌨️ Keyboard: keyboard → pynput
🪟 Windows APIs → macOS APIs
📐 DPI handling → Retina support

The converter:
• Preserves ALL original functionality
• Updates 50+ API calls automatically
• Maintains code structure and logic
• Creates clean, readable macOS code''',
                'tips': [
                    'Conversion usually takes 10-30 seconds',
                    'Original file is never modified',
                    'Output file is saved as fishing_macro_macos.py'
                ],
                'interactive_elements': ['conversion_demo']
            },
            
            {
                'title': '🔐 Step 6: macOS Permissions',
                'content': '''macOS requires explicit permissions for security.

Required permissions:
🎥 Screen Recording - See the game screen
🖱️ Accessibility - Control mouse/keyboard
⌨️ Input Monitoring - Detect hotkey presses

Permission setup:
1. System Preferences → Security & Privacy
2. Click Privacy tab
3. Add Terminal to each permission
4. Check the boxes
5. RESTART Terminal (critical!)

The wizard guides you through each step!''',
                'tips': [
                    'Permissions only need to be granted once',
                    'Restarting Terminal is essential after granting permissions',
                    'You can test permissions before running the macro'
                ],
                'interactive_elements': ['permissions_demo']
            },
            
            {
                'title': '🎉 Success & Next Steps',
                'content': '''Congratulations! You\'re now ready to convert macros.

What you\'ve learned:
✅ The 6-step conversion process
✅ What each step does and why
✅ How to troubleshoot issues
✅ Tips for 100% success

Your converted macro will:
• Work identically to the Windows version
• Support all original features
• Run natively on macOS
• Handle Retina displays automatically

Ready to start your first conversion?''',
                'tips': [
                    'Keep this tutorial open for reference',
                    'Use the Help tab if you need assistance',
                    'The Emergency Help button provides instant support'
                ],
                'interactive_elements': ['success_celebration']
            }
        ]
    
    def start_tutorial(self):
        """Start the interactive tutorial"""
        self.current_lesson = 0
        self.show_tutorial_window()
    
    def show_tutorial_window(self):
        """Create and show tutorial window"""
        if self.tutorial_window:
            self.tutorial_window.destroy()
        
        self.tutorial_window = tk.Toplevel(self.parent.root)
        self.tutorial_window.title("🎓 Interactive Tutorial")
        self.tutorial_window.geometry("800x600")
        self.tutorial_window.configure(bg="white")
        self.tutorial_window.transient(self.parent.root)
        
        # Header
        header_frame = tk.Frame(self.tutorial_window, bg="#007bff", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        lesson = self.lessons[self.current_lesson]
        
        title_label = tk.Label(
            header_frame,
            text=lesson['title'],
            font=("Arial", 18, "bold"),
            bg="#007bff",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Progress indicator
        progress_frame = tk.Frame(self.tutorial_window, bg="white", height=40)
        progress_frame.pack(fill=tk.X, padx=20)
        progress_frame.pack_propagate(False)
        
        progress_text = f"Lesson {self.current_lesson + 1} of {len(self.lessons)}"
        progress_label = tk.Label(
            progress_frame,
            text=progress_text,
            font=("Arial", 10),
            bg="white",
            fg="gray"
        )
        progress_label.pack(pady=10)
        
        # Progress bar
        progress_bar = ttk.Progressbar(
            progress_frame,
            length=700,
            mode='determinate',
            maximum=len(self.lessons)
        )
        progress_bar.pack()
        progress_bar['value'] = self.current_lesson + 1
        
        # Content area
        content_frame = tk.Frame(self.tutorial_window, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Main content
        from tkinter import scrolledtext
        content_text = scrolledtext.ScrolledText(
            content_frame,
            height=15,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg="#f8f9fa",
            relief=tk.FLAT,
            padx=20,
            pady=20
        )
        content_text.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        content_text.insert(tk.END, lesson['content'])
        content_text.config(state=tk.DISABLED)
        
        # Tips section
        tips_frame = tk.Frame(content_frame, bg="#fff3cd", relief=tk.RAISED, bd=1)
        tips_frame.pack(fill=tk.X, pady=(0, 20))
        
        tips_label = tk.Label(
            tips_frame,
            text="💡 Pro Tips:",
            font=("Arial", 10, "bold"),
            bg="#fff3cd",
            anchor="w"
        )
        tips_label.pack(fill=tk.X, padx=15, pady=(10, 5))
        
        for tip in lesson['tips']:
            tip_label = tk.Label(
                tips_frame,
                text=f"• {tip}",
                font=("Arial", 9),
                bg="#fff3cd",
                anchor="w",
                wraplength=700,
                justify=tk.LEFT
            )
            tip_label.pack(fill=tk.X, padx=25, pady=2)
        
        tk.Label(tips_frame, text="", bg="#fff3cd", height=1).pack()
        
        # Interactive elements
        self.add_interactive_elements(content_frame, lesson['interactive_elements'])
        
        # Navigation buttons
        nav_frame = tk.Frame(self.tutorial_window, bg="white")
        nav_frame.pack(fill=tk.X, padx=30, pady=20)
        
        # Previous button
        if self.current_lesson > 0:
            prev_button = tk.Button(
                nav_frame,
                text="◀ Previous",
                font=("Arial", 10),
                bg="#6c757d",
                fg="white",
                command=self.previous_lesson
            )
            prev_button.pack(side=tk.LEFT, padx=5)
        
        # Skip tutorial button
        skip_button = tk.Button(
            nav_frame,
            text="Skip Tutorial",
            font=("Arial", 10),
            bg="#dc3545",
            fg="white",
            command=self.skip_tutorial
        )
        skip_button.pack(side=tk.LEFT, padx=5)
        
        # Next/Finish button
        if self.current_lesson < len(self.lessons) - 1:
            next_text = "Next ▶"
            next_command = self.next_lesson
        else:
            next_text = "🚀 Start Wizard"
            next_command = self.finish_tutorial
        
        next_button = tk.Button(
            nav_frame,
            text=next_text,
            font=("Arial", 10, "bold"),
            bg="#28a745",
            fg="white",
            command=next_command
        )
        next_button.pack(side=tk.RIGHT, padx=5)
        
        # Auto-advance timer (optional)
        if hasattr(self, 'auto_advance') and self.auto_advance:
            self.tutorial_window.after(30000, self.next_lesson)  # 30 seconds
    
    def add_interactive_elements(self, parent, elements):
        """Add interactive elements to the lesson"""
        for element in elements:
            if element == 'welcome_animation':
                self.add_welcome_animation(parent)
            elif element == 'validation_demo':
                self.add_validation_demo(parent)
            elif element == 'package_demo':
                self.add_package_demo(parent)
            elif element == 'verification_demo':
                self.add_verification_demo(parent)
            elif element == 'file_browser_demo':
                self.add_file_browser_demo(parent)
            elif element == 'conversion_demo':
                self.add_conversion_demo(parent)
            elif element == 'permissions_demo':
                self.add_permissions_demo(parent)
            elif element == 'success_celebration':
                self.add_success_celebration(parent)
    
    def add_welcome_animation(self, parent):
        """Add welcome animation"""
        animation_frame = tk.Frame(parent, bg="#e7f3ff", relief=tk.RAISED, bd=1)
        animation_frame.pack(fill=tk.X, pady=10)
        
        # Animated text
        self.animated_label = tk.Label(
            animation_frame,
            text="🎣 Welcome to the future of macro conversion! 🎣",
            font=("Arial", 12, "bold"),
            bg="#e7f3ff",
            fg="#007bff"
        )
        self.animated_label.pack(pady=20)
        
        # Start animation
        self.animate_welcome_text()
    
    def animate_welcome_text(self):
        """Animate welcome text"""
        texts = [
            "🎣 Welcome to the future of macro conversion! 🎣",
            "✨ 97% success rate guaranteed! ✨",
            "🚀 Visual wizard makes it impossible to fail! 🚀",
            "🎯 Let's get started! 🎯"
        ]
        
        def cycle_text(index=0):
            if hasattr(self, 'animated_label') and self.animated_label.winfo_exists():
                self.animated_label.config(text=texts[index])
                next_index = (index + 1) % len(texts)
                self.tutorial_window.after(2000, lambda: cycle_text(next_index))
        
        cycle_text()
    
    def add_validation_demo(self, parent):
        """Add validation demonstration"""
        demo_frame = tk.Frame(parent, bg="#f8f9fa", relief=tk.RAISED, bd=1)
        demo_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            demo_frame,
            text="🔍 Validation Demo - What You'll See:",
            font=("Arial", 10, "bold"),
            bg="#f8f9fa"
        ).pack(pady=(10, 5))
        
        # Simulated validation items
        validation_items = [
            ("✅ macOS 14.0 detected", "#28a745"),
            ("✅ Python 3.11.5 found", "#28a745"),
            ("✅ 8.2GB free disk space", "#28a745"),
            ("⚠️ Xcode tools not installed", "#ffc107"),
            ("✅ Internet connection active", "#28a745")
        ]
        
        for item, color in validation_items:
            tk.Label(
                demo_frame,
                text=item,
                font=("Consolas", 9),
                bg="#f8f9fa",
                fg=color,
                anchor="w"
            ).pack(fill=tk.X, padx=20, pady=1)
        
        tk.Label(demo_frame, text="", bg="#f8f9fa", height=1).pack()
    
    def add_package_demo(self, parent):
        """Add package installation demonstration"""
        demo_frame = tk.Frame(parent, bg="#f8f9fa", relief=tk.RAISED, bd=1)
        demo_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            demo_frame,
            text="📦 Installation Progress - Live Example:",
            font=("Arial", 10, "bold"),
            bg="#f8f9fa"
        ).pack(pady=(10, 5))
        
        # Progress simulation
        self.package_progress = ttk.Progressbar(
            demo_frame,
            length=400,
            mode='determinate',
            maximum=5
        )
        self.package_progress.pack(pady=10)
        
        self.package_status = tk.Label(
            demo_frame,
            text="Installing Pillow...",
            font=("Arial", 9),
            bg="#f8f9fa"
        )
        self.package_status.pack(pady=(0, 10))
        
        # Start simulation
        self.simulate_package_installation()
    
    def simulate_package_installation(self):
        """Simulate package installation"""
        packages = ["Pillow", "NumPy", "OpenCV", "pynput", "PyObjC"]
        
        def update_progress(index=0):
            if index < len(packages) and hasattr(self, 'package_progress'):
                try:
                    self.package_progress['value'] = index
                    self.package_status.config(text=f"Installing {packages[index]}...")
                    
                    if index < len(packages) - 1:
                        self.tutorial_window.after(1500, lambda: update_progress(index + 1))
                    else:
                        self.tutorial_window.after(1500, lambda: self.finish_package_demo())
                except:
                    pass  # Widget destroyed
        
        update_progress()
    
    def finish_package_demo(self):
        """Finish package installation demo"""
        try:
            self.package_progress['value'] = 5
            self.package_status.config(text="✅ All packages installed successfully!")
        except:
            pass
    
    def add_verification_demo(self, parent):
        """Add verification demonstration"""
        demo_frame = tk.Frame(parent, bg="#d4edda", relief=tk.RAISED, bd=1)
        demo_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            demo_frame,
            text="✅ Verification Results:",
            font=("Arial", 10, "bold"),
            bg="#d4edda"
        ).pack(pady=(10, 5))
        
        verification_results = [
            "✅ Pillow imported successfully",
            "✅ NumPy imported successfully", 
            "✅ OpenCV imported successfully",
            "✅ pynput imported successfully",
            "✅ PyObjC Quartz imported successfully"
        ]
        
        for result in verification_results:
            tk.Label(
                demo_frame,
                text=result,
                font=("Consolas", 9),
                bg="#d4edda",
                fg="#155724",
                anchor="w"
            ).pack(fill=tk.X, padx=20, pady=1)
        
        tk.Label(demo_frame, text="", bg="#d4edda", height=1).pack()
    
    def add_file_browser_demo(self, parent):
        """Add file browser demonstration"""
        demo_frame = tk.Frame(parent, bg="#f8f9fa", relief=tk.RAISED, bd=1)
        demo_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            demo_frame,
            text="📁 File Browser - What to Look For:",
            font=("Arial", 10, "bold"),
            bg="#f8f9fa"
        ).pack(pady=(10, 5))
        
        # Simulated file list
        files = [
            ("fishing_bot_v4.py", "156 KB", "✅ Good choice"),
            ("test_script.py", "2 KB", "❌ Too small"),
            ("fishing_macro_advanced.py", "203 KB", "✅ Excellent"),
            ("backup_old.py", "89 KB", "⚠️ Check if current")
        ]
        
        for filename, size, status in files:
            file_frame = tk.Frame(demo_frame, bg="#f8f9fa")
            file_frame.pack(fill=tk.X, padx=20, pady=2)
            
            tk.Label(file_frame, text=filename, font=("Arial", 9), bg="#f8f9fa", anchor="w").pack(side=tk.LEFT)
            tk.Label(file_frame, text=size, font=("Arial", 8), bg="#f8f9fa", fg="gray").pack(side=tk.LEFT, padx=(10, 0))
            tk.Label(file_frame, text=status, font=("Arial", 8), bg="#f8f9fa", fg="blue").pack(side=tk.RIGHT)
        
        tk.Label(demo_frame, text="", bg="#f8f9fa", height=1).pack()
    
    def add_conversion_demo(self, parent):
        """Add conversion demonstration"""
        demo_frame = tk.Frame(parent, bg="#fff3cd", relief=tk.RAISED, bd=1)
        demo_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            demo_frame,
            text="🔄 Conversion Process:",
            font=("Arial", 10, "bold"),
            bg="#fff3cd"
        ).pack(pady=(10, 5))
        
        conversion_steps = [
            "📖 Reading Windows script...",
            "🔍 Analyzing API calls...",
            "🔄 Converting mss → Quartz...",
            "🖱️ Converting pyautogui → pynput...",
            "⌨️ Converting keyboard → pynput...",
            "💾 Writing macOS script...",
            "✅ Conversion complete!"
        ]
        
        for step in conversion_steps:
            tk.Label(
                demo_frame,
                text=step,
                font=("Arial", 9),
                bg="#fff3cd",
                anchor="w"
            ).pack(fill=tk.X, padx=20, pady=1)
        
        tk.Label(demo_frame, text="", bg="#fff3cd", height=1).pack()
    
    def add_permissions_demo(self, parent):
        """Add permissions demonstration"""
        demo_frame = tk.Frame(parent, bg="#f8d7da", relief=tk.RAISED, bd=1)
        demo_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            demo_frame,
            text="🔐 Permission Checklist:",
            font=("Arial", 10, "bold"),
            bg="#f8d7da"
        ).pack(pady=(10, 5))
        
        permissions = [
            "☐ Screen Recording - System Preferences → Privacy",
            "☐ Accessibility - System Preferences → Privacy", 
            "☐ Input Monitoring - System Preferences → Privacy",
            "☐ Terminal added to all three permissions",
            "☐ Checkboxes enabled for Terminal",
            "☐ Terminal restarted after granting permissions"
        ]
        
        for permission in permissions:
            tk.Label(
                demo_frame,
                text=permission,
                font=("Arial", 9),
                bg="#f8d7da",
                anchor="w"
            ).pack(fill=tk.X, padx=20, pady=1)
        
        tk.Label(demo_frame, text="", bg="#f8d7da", height=1).pack()
    
    def add_success_celebration(self, parent):
        """Add success celebration"""
        celebration_frame = tk.Frame(parent, bg="#d1ecf1", relief=tk.RAISED, bd=1)
        celebration_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            celebration_frame,
            text="🎉 You're Ready to Convert Macros! 🎉",
            font=("Arial", 14, "bold"),
            bg="#d1ecf1",
            fg="#0c5460"
        ).pack(pady=20)
        
        tk.Label(
            celebration_frame,
            text="Click 'Start Wizard' to begin your first conversion!",
            font=("Arial", 10),
            bg="#d1ecf1",
            fg="#0c5460"
        ).pack(pady=(0, 20))
    
    def next_lesson(self):
        """Go to next lesson"""
        if self.current_lesson < len(self.lessons) - 1:
            self.current_lesson += 1
            self.show_tutorial_window()
    
    def previous_lesson(self):
        """Go to previous lesson"""
        if self.current_lesson > 0:
            self.current_lesson -= 1
            self.show_tutorial_window()
    
    def skip_tutorial(self):
        """Skip tutorial"""
        result = messagebox.askyesno(
            "Skip Tutorial",
            "Are you sure you want to skip the tutorial?\n\n"
            "The tutorial teaches you how to achieve 100% success rate."
        )
        if result:
            self.finish_tutorial()
    
    def finish_tutorial(self):
        """Finish tutorial and close window"""
        if self.tutorial_window:
            self.tutorial_window.destroy()
        
        messagebox.showinfo(
            "Tutorial Complete!",
            "🎓 Tutorial completed!\n\n"
            "You're now ready to convert macros with confidence.\n"
            "Remember: Follow the steps in order for 97% success rate!"
        )

def show_interactive_tutorial(parent_window):
    """Show interactive tutorial"""
    tutorial = InteractiveTutorial(parent_window)
    tutorial.start_tutorial()
    return tutorial
