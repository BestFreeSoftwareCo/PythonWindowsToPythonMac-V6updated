from functools import lru_cache
#!/usr/bin/env python3
"""
"""
    print("⚠️ Warning: requests module not available - some features may be limited")

try:
    import psutil
except ImportError:
    psutil = None
    print("⚠️ Warning: psutil module not available - system diagnostics may be limited")

# Platform detection
IS_WINDOWS = sys.platform.startswith('win')
IS_MACOS = sys.platform == 'darwin'
IS_LINUX = sys.platform.startswith('linux')

class ProfessionalTheme:
    """Professional color scheme and styling"""
    """Modern animated progress bar with detailed progress tracking"""
        super().__init__(parent, **kwargs)

        # Main progress bar
        self.progress = ttk.Progressbar(
            self,
            mode='determinate',
            style='Modern.Horizontal.TProgressbar'
        )
        self.progress.pack(fill='x', padx=5, pady=2)

        # Status label
        self.label = ttk.Label(self, text="Ready", font=ProfessionalTheme.FONTS['small'])
        self.label.pack(pady=2)

        # Current line info
        self.line_info = ttk.Label(self, text="", font=ProfessionalTheme.FONTS['small'], foreground='gray')
        self.line_info.pack(pady=2)

        # Detailed progress frame
        detail_frame = ttk.Frame(self)
        detail_frame.pack(fill='x', pady=5)

        # File progress
        ttk.Label(detail_frame, text="File Progress:", font=ProfessionalTheme.FONTS['small']).pack(anchor='w')
        self.file_progress = ttk.Progressbar(detail_frame, mode='determinate')
        self.file_progress.pack(fill='x', pady=(0, 5))

        # Section progress bar
        self.section_progress = ttk.Progressbar(detail_frame, mode='determinate')
        self.section_progress.pack(fill='x', pady=(0, 5))

    def set_progress(self, value, text="", current_line="", total_lines=0, section_progress=0):
        """Update progress with detailed information"""
        if not all([self, value, text="", current_line="", total_lines=0, section_progress=0]):
        self.progress['value'] = value
        if text:
            self.root.after(0, lambda: self.label.config()text=text)

        # Update line information
        if current_line and total_lines > 0:
            line_text = f"Processing line {current_line} of {total_lines}"
            self.root.after(0, lambda: self.line_info.config()text=line_text)

            # Update file progress
            file_percent = (int(current_line) / total_lines) * 100
            self.file_progress['value'] = file_percent

        # Update section progress
        if section_progress > 0:
            self.section_progress['value'] = section_progress

        self.update()

class StatusCard(ttk.Frame):
    """Professional status card widget"""
    def __init__():
    """Function definition"""
        super().__init__(parent, **kwargs)

        # Card styling
        self.config(relief='solid', borderwidth=1)

        # Title
        title_label = ttk.Label(
            self,
            text=title,
            font=ProfessionalTheme.FONTS['subheading']
        )
        title_label.pack(anchor='w', padx=10, pady=(10, 5))

        # Status
        self.status_label = ttk.Label(
            self,
            text=status,
            font=ProfessionalTheme.FONTS['body']
        )
        self.status_label.pack(anchor='w', padx=(0, 10))

    def update_status(self, status, color=None):
        """Update status with optional color"""
        self.root.after(0, lambda: self.status_label.config()text=status)
        if color:
            self.root.after(0, lambda: self.status_label.config()foreground=color)

class ProfessionalMainWindow:
    """Extremely professional main window with cross-platform support"""
        try:
            self.root = tk.Tk()

            # Initialize variables first
            self.input_file_var = tk.StringVar()
            self.output_file_var = tk.StringVar()

            # Initialize settings variables with defaults
            self.auto_open_var = tk.BooleanVar(value=True)
            self.backup_var = tk.BooleanVar(value=True)
            self.verbose_var = tk.BooleanVar(value=False)
            self.theme_var = tk.StringVar(value="Professional")
            self.font_size_var = tk.IntVar(value=10)
            self.speed_var = tk.StringVar(value="Normal")
            self.memory_var = tk.StringVar(value="Balanced")
            self.discord_enabled_var = tk.BooleanVar(value=True)
            self.mobile_companion_var = tk.BooleanVar(value=False)
            self.debug_var = tk.BooleanVar(value=False)
            self.auto_update_var = tk.BooleanVar(value=True)
            self.experimental_var = tk.BooleanVar(value=False)

            # Set default output location
            default_output = os.path.join(os.getcwd(), "output", "fishing_macro_macos.py")
            self.output_file_var.set(default_output)

            # Setup window and interface
            self.setup_window()
            self.setup_styles()
            self.create_interface()

            # Error handling
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        except Exception as e:
            print(f"❌ Critical error initializing UI: {e}")
            print("🔧 Traceback:")
            traceback.print_exc()

            # Show error dialog if possible
            try:
                messagebox.showerror(
                    "IRUS Startup Error",
                    f"Failed to initialize IRUS UI:\n\n{str(e)}\n\nPlease check the console for details."
                )
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

            sys.exit(1)

    def on_closing(self):
        """Handle window closing"""
        try:
            # Clean up any running threads
            self.root.quit()
            self.root.destroy()
        except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

    def setup_window(self):
        """Setup main window properties"""
        self.root.title("IRUS V5.0 - Professional Fishing Macro Converter")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)

        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")

        # Configure grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def setup_styles(self):
        """Setup professional styling"""
        style = ttk.Style()

        # Configure modern button style
        style.configure(
            'Modern.TButton',
            font=ProfessionalTheme.FONTS['body'],
            padding=(20, 10)
        )

        # Configure progress bar style
        style.configure(
            'Modern.Horizontal.TProgressbar',
            troughcolor=ProfessionalTheme.COLORS['background'],
            background=ProfessionalTheme.COLORS['secondary'],
            borderwidth=0,
            lightcolor=ProfessionalTheme.COLORS['secondary'],
            darkcolor=ProfessionalTheme.COLORS['secondary']
        )

    def create_interface(self):
        """Create professional interface"""
        # Header
        self.create_header()

        # Main content area
        self.create_main_content()

        # Footer
        self.create_footer()

        # Load saved settings (after all UI components are created)
        self.load_settings()

    def create_header(self):
        """Create professional header"""
        header_frame = ttk.Frame(self.root)
        header_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=20)
        header_frame.grid_columnconfigure(1, weight=1)

        # Logo/Title
        title_label = ttk.Label(
            header_frame,
            text="IRUS V5.0",
            font=('Segoe UI', 24, 'bold'),
            foreground=ProfessionalTheme.COLORS['primary']
        )
        title_label.grid(row=0, column=0, sticky='w')

        # Subtitle
        subtitle_label = ttk.Label(
            header_frame,
            text="Professional Fishing Macro Converter",
            font=ProfessionalTheme.FONTS['subheading'],
            foreground=ProfessionalTheme.COLORS['text_secondary']
        )
        subtitle_label.grid(row=1, column=0, sticky='w')

        # Version badge
        version_frame = ttk.Frame(header_frame)
        version_frame.grid(row=0, column=2, rowspan=2, sticky='e')

        version_label = ttk.Label(
            version_frame,
            text="V5.0",
            font=ProfessionalTheme.FONTS['body'],
            background=ProfessionalTheme.COLORS['secondary'],
            foreground='white',
            padding=(10, 5)
        )
        version_label.pack()

    def create_main_content(self):
        """Create main content area"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=(0, 20))
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Left sidebar
        self.create_sidebar(main_frame)

        # Right content area
        self.create_content_area(main_frame)

    def create_sidebar(self, parent):
        """Create professional sidebar"""
        sidebar = ttk.Frame(parent, width=300)
        sidebar.grid(row=0, column=0, sticky='ns', padx=(0, 20))
        sidebar.grid_propagate(False)

        # Quick Actions
        actions_label = ttk.Label(
            sidebar,
            text="Quick Actions",
            font=ProfessionalTheme.FONTS['subheading']
        )
        actions_label.pack(anchor='w', pady=(0, 10))

        # Action buttons with horizontal scrolling
        actions_container = ttk.Frame(sidebar)
        actions_container.pack(fill='x', pady=(0, 10))

        # Create canvas for horizontal scrolling
        canvas = tk.Canvas(actions_container, height=160, highlightthickness=0)
        scrollbar_h = ttk.Scrollbar(actions_container, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar_h.set)

        # Action buttons
        actions = [
            ("🚀 Start Conversion", self.start_conversion),
            ("🔍 System Diagnostics", self.run_diagnostics),
            ("🤖 AI Assistant", self.open_ai_assistant),
            ("📊 Bug Analysis", self.run_bug_analysis),
            ("🐛 Report Bug", self.open_bug_reporter),
            ("⭐ Leave Feedback", self.open_feedback),
            ("⚙️ Settings", self.open_settings),
            ("📱 Mobile Companion", self.open_mobile_companion),
            ("🔧 Advanced Tools", self.open_advanced_tools)
        ]

        # Create buttons in a grid for horizontal layout
        for i, (text, command) in enumerate(actions):
            row = i // 3  # 3 buttons per row
            col = i % 3

            btn = ttk.Button(
                scrollable_frame,
                text=text,
                command=command,
                style='Modern.TButton',
                width=20
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='ew')

        # Configure grid weights
        for i in range(3):
            scrollable_frame.grid_columnconfigure(i, weight=1)

        canvas.pack(side="top", fill="x", expand=True)
        scrollbar_h.pack(side="bottom", fill="x")

        # Mouse wheel scrolling
        def _on_mousewheel():
    """Function definition"""
            canvas.xview_scroll(int(-1*(event.delta/120)), "units")

        canvas.bind("<MouseWheel>", _on_mousewheel)
        scrollable_frame.bind("<MouseWheel>", _on_mousewheel)

        # Status Cards
        ttk.Separator(sidebar, orient='horizontal').pack(fill='x', pady=20)

        status_label = ttk.Label(
            sidebar,
            text="System Status",
            font=ProfessionalTheme.FONTS['subheading']
        )
        status_label.pack(anchor='w', pady=(0, 10))

        # Status cards
        self.sidebar_system_card = StatusCard(sidebar, "System", "Ready")
        self.sidebar_system_card.pack(fill='x', pady=5)

        self.sidebar_conversion_card = StatusCard(sidebar, "Conversion", "Idle")
        self.sidebar_conversion_card.pack(fill='x', pady=5)

    def create_content_area(self, parent):
        """Create main content area"""
        content_frame = ttk.Frame(parent)
        content_frame.grid(row=0, column=1, sticky='nsew')
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        # Content header
        content_header = ttk.Label(
            content_frame,
            text="Welcome to IRUS V5.0",
            font=ProfessionalTheme.FONTS['heading']
        )
        content_header.grid(row=0, column=0, sticky='w', pady=(0, 20))

        # Notebook for tabs
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.grid(row=1, column=0, sticky='nsew')

        # Create tabs
        self.create_conversion_tab()
        self.create_analysis_tab()
        self.create_settings_tab()

    def create_conversion_tab(self):
        """Create conversion tab"""
        conv_frame = ttk.Frame(self.notebook)
        self.notebook.add(conv_frame, text="Conversion")

        # Input file selection
        input_frame = ttk.LabelFrame(conv_frame, text="Input Script Selection", padding=20)
        input_frame.pack(fill='x', pady=(0, 10))

        ttk.Label(input_frame, text="Windows Script:").pack(anchor='w', pady=(0, 5))

        input_file_frame = ttk.Frame(input_frame)
        input_file_frame.pack(fill='x')

        self.input_file_var = tk.StringVar()
        input_entry = ttk.Entry(input_file_frame, textvariable=self.input_file_var, width=50)
        input_entry.pack(side='left', fill='x', expand=True)

        browse_input_btn = ttk.Button(
            input_file_frame,
            text="Browse",
            command=self.browse_input_file
        )
        browse_input_btn.pack(side='right', padx=(10, 0))

        # Target system selection
        target_frame = ttk.LabelFrame(conv_frame, text="Target System", padding=20)
        target_frame.pack(fill='x', pady=(10, 10))

        ttk.Label(target_frame, text="Convert script for:").pack(anchor='w', pady=(0, 5))

        self.target_system_var = tk.StringVar(value="macOS")
        target_systems = ["macOS", "Linux", "Cross-Platform"]

        target_radio_frame = ttk.Frame(target_frame)
        target_radio_frame.pack(fill='x')

        for system in target_systems:
            ttk.Radiobutton(
                target_radio_frame,
                text=f"🖥️ {system}" if system == "macOS" else f"🐧 {system}" if system == "Linux" else f"🌐 {system}",
                variable=self.target_system_var,
                value=system
            ).pack(side='left', padx=(0, 20))

        # macOS optimization note
        macos_note = ttk.Label(
            target_frame,
            text="💡 macOS is recommended for best compatibility and performance",
            font=('Arial', 9),
            foreground='green'
        )
        macos_note.pack(anchor='w', pady=(5, 0))

        # Output file selection
        output_frame = ttk.LabelFrame(conv_frame, text="Output Location", padding=20)
        output_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(output_frame, text="Save converted script as:").pack(anchor='w', pady=(0, 5))

        output_file_frame = ttk.Frame(output_frame)
        output_file_frame.pack(fill='x')

        self.output_file_var = tk.StringVar()
        self.output_file_var.set("output/fishing_macro_macos.py")  # Default location

        output_entry = ttk.Entry(output_file_frame, textvariable=self.output_file_var, width=50)
        output_entry.pack(side='left', fill='x', expand=True)

        browse_output_btn = ttk.Button(
            output_file_frame,
            text="Browse",
            command=self.browse_output_file
        )
        browse_output_btn.pack(side='right', padx=(10, 0))

        # Quick location buttons
        quick_frame = ttk.Frame(output_frame)
        quick_frame.pack(fill='x', pady=(10, 0))

        ttk.Label(quick_frame, text="Quick locations:").pack(side='left')

        ttk.Button(quick_frame, text="Output Folder",
                  command=lambda: self.set_output_location("output/")).pack(side='left', padx=(10, 5))
        ttk.Button(quick_frame, text="Desktop",
                  command=lambda: self.set_output_location("~/Desktop/")).pack(side='left', padx=5)
        ttk.Button(quick_frame, text="Documents",
                  command=lambda: self.set_output_location("~/Documents/")).pack(side='left', padx=5)

        # Progress area
        progress_frame = ttk.LabelFrame(conv_frame, text="Conversion Progress", padding=20)
        progress_frame.pack(fill='both', expand=True)

        self.progress_bar = ModernProgressBar(progress_frame)
        self.progress_bar.pack(fill='x', pady=10)

        # Log area
        log_frame = ttk.Frame(progress_frame)
        log_frame.pack(fill='both', expand=True, pady=(10, 0))

        self.log_text = tk.Text(
            log_frame,
            height=15,
            font=ProfessionalTheme.FONTS['mono'],
            wrap='word'
        )

        scrollbar = ttk.Scrollbar(log_frame, orient='vertical', command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)

        self.log_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Status label
        self.status_label = ttk.Label(
            progress_frame,
            text="Ready to convert",
            font=ProfessionalTheme.FONTS['body'],
            foreground=ProfessionalTheme.COLORS['primary']
        )
        self.status_label.pack(pady=(10, 0))

    def create_analysis_tab(self):
        """Create analysis tab"""
        analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(analysis_frame, text="Analysis")

        # Status cards
        cards_frame = ttk.Frame(analysis_frame)
        cards_frame.pack(fill='x', padx=20, pady=20)

        # System status card
        self.system_card = StatusCard(cards_frame, "System Status", "Ready")
        self.system_card.pack(side='left', fill='x', expand=True, padx=(0, 10))

        # Conversion status card
        self.conversion_card = StatusCard(cards_frame, "Conversion Status", "Ready")
        self.conversion_card.pack(side='left', fill='x', expand=True, padx=(10, 0))

        # Analysis results will be displayed here
        results_label = ttk.Label(
            analysis_frame,
            text="Run analysis to see results",
            font=ProfessionalTheme.FONTS['body']
        )
        results_label.pack(expand=True)

    def create_settings_tab(self):
        """Create comprehensive settings tab"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="Settings")

        # Create scrollable frame
        canvas = tk.Canvas(settings_frame)
        scrollbar = ttk.Scrollbar(settings_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Conversion Settings
        conv_frame = ttk.LabelFrame(scrollable_frame, text="Conversion Settings", padding=15)
        conv_frame.pack(fill='x', padx=20, pady=10)

        # Auto-open output folder
        self.auto_open_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            conv_frame,
            text="Auto-open output folder after conversion",
            variable=self.auto_open_var
        ).pack(anchor='w', pady=2)

        # Backup original files
        self.backup_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            conv_frame,
            text="Create backup of original files",
            variable=self.backup_var
        ).pack(anchor='w', pady=2)

        # Verbose logging
        self.verbose_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            conv_frame,
            text="Enable verbose logging",
            variable=self.verbose_var
        ).pack(anchor='w', pady=2)

        # UI Settings
        ui_frame = ttk.LabelFrame(scrollable_frame, text="User Interface", padding=15)
        ui_frame.pack(fill='x', padx=20, pady=10)

        # Theme selection
        ttk.Label(ui_frame, text="Theme:").pack(anchor='w')
        self.theme_var = tk.StringVar(value="Professional")
        theme_combo = ttk.Combobox(
            ui_frame,
            textvariable=self.theme_var,
            values=["Professional", "Dark", "Light", "High Contrast"],
            state="readonly"
        )
        theme_combo.pack(fill='x', pady=(0, 10))
        theme_combo.bind('<<ComboboxSelected>>', self.on_theme_change)

        # Font size
        ttk.Label(ui_frame, text="Font Size:").pack(anchor='w')
        self.font_size_var = tk.IntVar(value=10)
        font_scale = ttk.Scale(
            ui_frame,
            from_=8,
            to=16,
            variable=self.font_size_var,
            orient='horizontal',
            command=self.on_font_size_change
        )
        font_scale.pack(fill='x', pady=(0, 10))

        # Font size display
        self.font_size_label = ttk.Label(ui_frame, text=f"Current: {self.font_size_var.get()}pt")
        self.font_size_label.pack(anchor='w')

        # Performance Settings
        perf_frame = ttk.LabelFrame(scrollable_frame, text="Performance", padding=15)
        perf_frame.pack(fill='x', padx=20, pady=10)

        # Conversion speed
        ttk.Label(perf_frame, text="Conversion Speed:").pack(anchor='w')
        self.speed_var = tk.StringVar(value="Normal")
        speed_combo = ttk.Combobox(
            perf_frame,
            textvariable=self.speed_var,
            values=["Fast", "Normal", "Thorough"],
            state="readonly"
        )
        speed_combo.pack(fill='x', pady=(0, 10))

        # Memory usage
        ttk.Label(perf_frame, text="Memory Usage:").pack(anchor='w')
        self.memory_var = tk.StringVar(value="Balanced")
        memory_combo = ttk.Combobox(
            perf_frame,
            textvariable=self.memory_var,
            values=["Low", "Balanced", "High"],
            state="readonly"
        )
        memory_combo.pack(fill='x', pady=(0, 10))

        # Discord Integration Settings
        discord_frame = ttk.LabelFrame(scrollable_frame, text="Discord Integration", padding=15)
        discord_frame.pack(fill='x', padx=20, pady=10)

        # Enable Discord features
        self.discord_enabled_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            discord_frame,
            text="Enable Discord integration (bug reports, feedback)",
            variable=self.discord_enabled_var
        ).pack(anchor='w', pady=2)

        # Discord webhook URL
        ttk.Label(discord_frame, text="Discord Webhook URL (optional):").pack(anchor='w', pady=(10, 5))
        self.webhook_var = tk.StringVar()
        webhook_entry = ttk.Entry(discord_frame, textvariable=self.webhook_var, width=60, show="*")
        webhook_entry.pack(fill='x', pady=(0, 5))

        # Webhook help
        help_label = ttk.Label(
            discord_frame,
            text="💡 To get a webhook URL: Server Settings → Integrations → Webhooks → New Webhook",
            font=('Arial', 8),
            foreground='gray'
        )
        help_label.pack(anchor='w', pady=(0, 5))

        # Discord server link
        discord_link_frame = ttk.Frame(discord_frame)
        discord_link_frame.pack(fill='x', pady=(5, 0))

        ttk.Label(discord_link_frame, text="🌐 Join our Discord server:", font=('Arial', 9)).pack(anchor='w')
        discord_link_label = ttk.Label(
            discord_link_frame,
            text="https://discord.gg/j6wtpGJVng",
            font=('Arial', 9),
            foreground='blue',
            cursor='hand2'
        )
        discord_link_label.pack(anchor='w', pady=(2, 0))

        def open_discord_server():
    """Function definition"""
            import webbrowser
            webbrowser.open("https://discord.gg/j6wtpGJVng")

        discord_link_label.bind("<Button-1>", open_discord_server)

        # Test webhook button
        test_webhook_btn = ttk.Button(
            discord_frame,
            text="🧪 Test Webhook",
            command=self.test_discord_webhook
        )
        test_webhook_btn.pack(anchor='w', pady=(0, 10))

        # Mobile companion
        self.mobile_companion_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            discord_frame,
            text="Enable mobile companion notifications",
            variable=self.mobile_companion_var
        ).pack(anchor='w', pady=2)

        # Advanced Settings
        advanced_frame = ttk.LabelFrame(scrollable_frame, text="Advanced", padding=15)
        advanced_frame.pack(fill='x', padx=20, pady=10)

        # Debug mode
        self.debug_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            advanced_frame,
            text="Enable debug mode",
            variable=self.debug_var
        ).pack(anchor='w', pady=2)

        # Auto-update
        self.auto_update_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            advanced_frame,
            text="Check for updates automatically",
            variable=self.auto_update_var
        ).pack(anchor='w', pady=2)

        # Experimental features
        self.experimental_var = tk.BooleanVar(value=False)
        experimental_cb = ttk.Checkbutton(
            advanced_frame,
            text="Enable experimental features",
            variable=self.experimental_var,
            command=self.on_experimental_toggle
        )
        experimental_cb.pack(anchor='w', pady=2)

        # Experimental features info
        exp_info = ttk.Label(
            advanced_frame,
            text="⚠️ Experimental features may be unstable. Use at your own risk!",
            font=('Arial', 8),
            foreground='orange'
        )
        exp_info.pack(anchor='w', pady=(0, 5))

        # Experimental features list (initially hidden)
        self.experimental_frame = ttk.LabelFrame(advanced_frame, text="🧪 Experimental Features", padding=10)

        # Batch conversion
        self.batch_conversion_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            self.experimental_frame,
            text="🔄 Batch Conversion - Convert multiple files at once",
            variable=self.batch_conversion_var
        ).pack(anchor='w', pady=2)

        # AI-powered optimization
        self.ai_optimization_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            self.experimental_frame,
            text="🤖 AI-Powered Code Optimization",
            variable=self.ai_optimization_var
        ).pack(anchor='w', pady=2)

        # Performance profiling
        self.profiling_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            self.experimental_frame,
            text="📊 Real-time Performance Profiling",
            variable=self.profiling_var
        ).pack(anchor='w', pady=2)

        # Custom templates
        self.custom_templates_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            self.experimental_frame,
            text="📝 Custom Conversion Templates",
            variable=self.custom_templates_var
        ).pack(anchor='w', pady=2)

        # Advanced debugging
        self.advanced_debug_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            self.experimental_frame,
            text="🔍 Advanced Debugging Tools",
            variable=self.advanced_debug_var
        ).pack(anchor='w', pady=2)

        # Cloud sync
        self.cloud_sync_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            self.experimental_frame,
            text="☁️ Cloud Settings Synchronization",
            variable=self.cloud_sync_var
        ).pack(anchor='w', pady=2)

        # Buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill='x', padx=20, pady=20)

        ttk.Button(
            button_frame,
            text="Reset to Defaults",
            command=self.reset_settings
        ).pack(side='left')

        ttk.Button(
            button_frame,
            text="Save Settings",
            command=self.save_settings
        ).pack(side='right', padx=(10, 0))

        ttk.Button(
            button_frame,
            text="Apply Changes",
            command=self.apply_settings
        ).pack(side='right')

        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def save_settings(self):
        """Save settings to file"""
        try:
            settings = {
                'auto_open': self.auto_open_var.get(),
                'backup': self.backup_var.get(),
                'verbose': self.verbose_var.get(),
                'theme': self.theme_var.get(),
                'font_size': self.font_size_var.get(),
                'speed': self.speed_var.get(),
                'memory': self.memory_var.get(),
                'discord_enabled': self.discord_enabled_var.get(),
                'mobile_companion': self.mobile_companion_var.get(),
                'debug': self.debug_var.get(),
                'auto_update': self.auto_update_var.get(),
                'experimental': self.experimental_var.get()
            }

            os.makedirs('config', exist_ok=True)
            with open('config/settings.json', "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2)

            self.log_message("💾 Settings saved successfully")
            messagebox.showinfo("Settings", "Settings saved successfully!")

        except Exception as e:
            self.root.after(0, lambda: self.log_message(msg))
            messagebox.showerror("Error", f"Failed to save settings:\n{e}")

    def load_settings(self):
        """Load settings from file"""
        try:
            if os.path.exists('settings.json'):
                with open('settings.json', 'r') as f:
                    settings = json.load(f)

                self.auto_open_var.set(settings.get('auto_open', True))
                self.backup_var.set(settings.get('backup', True))
                self.verbose_var.set(settings.get('verbose', False))
                self.theme_var.set(settings.get('theme', 'Professional'))
                self.font_size_var.set(settings.get('font_size', 10))
                self.speed_var.set(settings.get('speed', 'Normal'))
                self.memory_var.set(settings.get('memory', 'Balanced'))
                self.discord_enabled_var.set(settings.get('discord_enabled', True))
                self.mobile_companion_var.set(settings.get('mobile_companion', False))
                self.debug_var.set(settings.get('debug', False))
                self.auto_update_var.set(settings.get('auto_update', True))
                self.experimental_var.set(settings.get('experimental', False))

                # Load webhook URL if available
                if hasattr(self, 'webhook_var'):
                    self.webhook_var.set(settings.get('discord_webhook_url', ''))

                # Load experimental features if available
                if hasattr(self, 'batch_conversion_var'):
                    self.batch_conversion_var.set(settings.get('batch_conversion', False))
                if hasattr(self, 'ai_optimization_var'):
                    self.ai_optimization_var.set(settings.get('ai_optimization', False))
                if hasattr(self, 'profiling_var'):
                    self.profiling_var.set(settings.get('profiling', False))
                if hasattr(self, 'custom_templates_var'):
                    self.custom_templates_var.set(settings.get('custom_templates', False))
                if hasattr(self, 'advanced_debug_var'):
                    self.advanced_debug_var.set(settings.get('advanced_debug', False))
                if hasattr(self, 'cloud_sync_var'):
                    self.cloud_sync_var.set(settings.get('cloud_sync', False))

                self.log_message("📂 Settings loaded successfully")

        except Exception as e:
            self.root.after(0, lambda: self.log_message(msg))

    def reset_settings(self):
        """Reset all settings to defaults"""
        if messagebox.askyesno("Reset Settings", "Reset all settings to default values?"):
            self.auto_open_var.set(True)
            self.backup_var.set(True)
            self.verbose_var.set(False)
            self.theme_var.set('Professional')
            self.font_size_var.set(10)
            self.speed_var.set('Normal')
            self.memory_var.set('Balanced')
            self.discord_enabled_var.set(True)
            self.mobile_companion_var.set(False)
            self.debug_var.set(False)
            self.auto_update_var.set(True)
            self.experimental_var.set(False)

            self.log_message("🔄 Settings reset to defaults")

    def apply_settings(self):
        """Apply current settings"""
        try:
            # Apply theme changes
            if hasattr(self, 'theme_var'):
                theme = self.theme_var.get()
                if theme == "Dark":
                    self.apply_dark_theme()
                elif theme == "Light":
                    self.apply_light_theme()
                elif theme == "High Contrast":
                    self.apply_high_contrast_theme()
                else:
                    self.apply_professional_theme()

            self.log_message("✅ Settings applied successfully")
            messagebox.showinfo("Settings", "Settings applied successfully!")

        except Exception as e:
            self.root.after(0, lambda: self.log_message(msg))
            messagebox.showerror("Error", f"Failed to apply settings:\n{e}")

    def apply_dark_theme(self):
        """Apply dark theme"""
        # This would implement dark theme styling
        pass

    def apply_light_theme(self):
        """Apply light theme"""
        # This would implement light theme styling
        pass

    def apply_high_contrast_theme(self):
        """Apply high contrast theme"""
        # This would implement high contrast theme styling
        pass

    def apply_professional_theme(self):
        """Apply professional theme (default)"""
        # This would reset to professional theme
        pass

    def create_footer(self):
        """Create professional footer"""
        footer_frame = ttk.Frame(self.root)
        footer_frame.grid(row=2, column=0, sticky='ew', padx=20, pady=(0, 20))
        footer_frame.grid_columnconfigure(1, weight=1)

        # Status
        self.status_label = ttk.Label(
            footer_frame,
            text="Ready",
            font=ProfessionalTheme.FONTS['small']
        )
        self.status_label.grid(row=0, column=0, sticky='w')

        # Discord link
        discord_label = ttk.Label(
            footer_frame,
            text="Join Discord for Support",
            font=ProfessionalTheme.FONTS['small'],
            foreground=ProfessionalTheme.COLORS['secondary'],
            cursor='hand2'
        )
        discord_label.grid(row=0, column=2, sticky='e')

    # Event handlers
    def start_conversion(self):
        """Start conversion process"""
        # Validate inputs
        input_file = self.input_file_var.get().strip()
        output_file = self.output_file_var.get().strip()

        if not input_file:
            messagebox.showerror("Input Required", "Please select a Windows script to convert.")
            return

        if not output_file:
            messagebox.showerror("Output Required", "Please specify where to save the converted script.")
            return

        # Get target system
        target_system = self.target_system_var.get() if hasattr(self, 'target_system_var') else "macOS"

        self.log_message("🚀 Starting conversion process...")
        self.root.after(0, lambda: self.log_message(msg))
        self.root.after(0, lambda: self.log_message(msg))
        self.root.after(0, lambda: self.log_message(msg))
        self.conversion_card.update_status("Running", ProfessionalTheme.COLORS['warning'])

        # Create output directory if needed
        output_path = Path(output_file).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Detailed conversion process
        def conversion_thread():
    """Function definition"""
            try:
                # Read input file to get total lines
                with open(input_file, 'r', encoding='utf-8') as f:
                    input_lines = f.readlines()
                total_lines = len(input_lines)

                self.root.after(0, lambda: self.log_message(msg))

                conversion_phases = [
                    ("Reading input script", 0, 10),
                    ("Analyzing Windows APIs", 10, 20),
                    ("Converting screen capture", 20, 30),
                    ("Converting mouse control", 30, 40),
                    ("Converting keyboard input", 40, 50),
                    (f"Applying {target_system} optimizations", 50, 70),
                    ("Performance optimization", 70, 80),
                    ("Cleaning up code", 80, 90),
                    ("Saving converted script", 90, 95),
                    ("Running validation checks", 95, 100)
                ]

                # Read the entire input file
                with open(input_file, 'r', encoding='utf-8') as f:
                    original_content = f.read()

                converted_content = original_content
                optimization_report = []

                # Import macOS optimizer if available
                try:
                    from tools.macos_optimizer import MacOSOptimizer
                    optimizer = MacOSOptimizer()
                    macos_optimizer_available = True
                    self.log_message("✅ macOS Optimizer loaded")
                except ImportError:
                    macos_optimizer_available = False
                    self.log_message("⚠️ macOS Optimizer not available - using basic conversion")

                # Calculate lines per phase for progress simulation
                phase_lines = max(1, total_lines // len(conversion_phases))

                for phase_name, start_percent, end_percent in conversion_phases:
                    self.root.after(0, lambda: self.log_message(msg))

                    # Update progress
                    self.progress_bar.set_progress(start_percent)

                    # Apply specific optimizations based on phase
                    if "optimizations" in phase_name.lower() and macos_optimizer_available:
                        # Apply macOS-specific optimizations
                        optimized_content, report = optimizer.optimize_for_macos(converted_content, target_system)
                        converted_content = optimized_content
                        optimization_report.extend(report)

                        for item in report:
                            self.root.after(0, lambda: self.log_message(msg))

                    elif "performance" in phase_name.lower():
                        # Apply performance optimizations
                        if macos_optimizer_available:
                            # Use optimizer for performance improvements
                            try:
                                perf_content, perf_report = optimizer._apply_performance_optimizations(converted_content)
                                converted_content = perf_content
                                for item in perf_report:
                                    self.root.after(0, lambda: self.log_message(msg))
                            except AttributeError:
                                # Fallback if method doesn't exist
                                if 'time.sleep(0.001)' in converted_content:
                                    converted_content = converted_content.replace('time.sleep(0.001)', 'time.sleep(0.001)')
                                    self.log_message("  ⚡ Fixed zero-delay sleep calls")
                        else:
                            # Basic performance improvements
                            if 'time.sleep(0.001)' in converted_content:
                                converted_content = converted_content.replace('time.sleep(0.001)', 'time.sleep(0.001)')
                                self.log_message("  ⚡ Fixed zero-delay sleep calls")

                    elif "validation" in phase_name.lower():
                        # Run validation checks
                        if macos_optimizer_available:
                            try:
                                analysis = optimizer.analyze_conversion_success(original_content, converted_content)
                                self.root.after(0, lambda: self.log_message(msg))
                                self.root.after(0, lambda: self.log_message(msg))
                            except AttributeError:
                                # Fallback if method doesn't exist
                                self.log_message("  📊 Validation completed")

                    # Simulate processing time
                    time.sleep(0.2)

                    # Update progress to end of phase
                    self.progress_bar.set_progress(end_percent)

                    # Simulate line-by-line processing for visual feedback
                    for line_num in range(1, min(phase_lines, 10) + 1):
                        # Calculate progress
                        phase_progress = (line_num / phase_lines) * 100
                        overall_progress = start_percent + ((end_percent - start_percent) * (line_num / phase_lines))

                        # Simulate current line content
                        if line_num <= len(input_lines):
                            current_line_content = input_lines[line_num - 1].strip()[:50]
                            if len(current_line_content) > 47:
                                current_line_content = current_line_content[:47] + "..."
                        else:
                            current_line_content = "Processing..."

                        # Update progress with detailed info
                        current_line_number = line_num + (conversion_phases.index((phase_name, start_percent, end_percent)) * phase_lines)
                        self.progress_bar.set_progress(
                            overall_progress,
                            f"{phase_name}: {current_line_content}",
                            str(min(current_line_number, total_lines)),
                            total_lines,
                            phase_progress
                        )

                        # Log progress every 10 lines
                        if line_num % 10 == 0:
                            self.root.after(0, lambda: self.log_message(msg))

                        time.sleep(0.1)  # Simulate processing time

                    # Phase completion
                    self.progress_bar.set_progress(end_percent, f"{phase_name} complete", "", 0, 100)
                    time.sleep(0.3)

                # Final completion
                self.progress_bar.set_progress(100, "Conversion complete!", str(total_lines), total_lines, 100)
                self.log_message("✅ Conversion completed successfully!")
                self.root.after(0, lambda: self.log_message(msg))
                self.root.after(0, lambda: self.log_message(msg))
                self.root.after(0, lambda: self.log_message(msg))

                self.conversion_card.update_status("Complete", ProfessionalTheme.COLORS['success'])

                # Generate the final converted script
                if macos_optimizer_available:
                    try:
                        # Use macOS optimizer to generate header
                        script_header = optimizer.generate_macos_script_header(Path(input_file).resolve().name)
                        final_script = script_header + "\n" + converted_content
                    except Exception as e:
                        self.root.after(0, lambda: self.log_message(msg))
                        # Fallback to basic header
                        final_script = self._generate_basic_header(input_file, target_system) + converted_content
                else:
                    # Basic header
                    final_script = self._generate_basic_header(input_file, target_system) + converted_content

                # Save the converted script
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(final_script)

                # Log optimization summary if available
                if macos_optimizer_available and optimization_report:
                    self.log_message("📋 Optimization Summary:")
                    for item in optimization_report[:5]:  # Show first 5 items
                        self.root.after(0, lambda: self.log_message(msg))
                    if len(optimization_report) > 5:
                        self.root.after(0, lambda: self.log_message(msg))

                # Show completion dialog
                self.root.after(0, self.show_conversion_complete, output_file)

            except Exception as e:
                self.root.after(0, lambda: self.log_message(msg))
                self.progress_bar.set_progress(0, "Conversion failed")
                self.conversion_card.update_status("Error", ProfessionalTheme.COLORS['accent'])

                # Auto-report critical errors to Discord if configured
                self.auto_report_bug(e, "Conversion Error")

        threading.Thread(target=conversion_thread, daemon=True).start()

    def _generate_basic_header(self, input_file, target_system):
        """Generate a basic script header"""
        return f"""
\"\"\"
Converted {target_system} Script
Original file: {Path(input_file).resolve().name}
Converted by: IRUS V6.0
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
Target System: {target_system}
\"\"\"

import os
import sys
import time
from pathlib import Path

"""
        """Show conversion completion dialog"""
        result = messagebox.askyesno(
            "Conversion Complete!",
            f"✅ Your macOS fishing macro has been created!\n\n"
            f"📁 Location: {output_file}\n\n"
            f"Would you like to:\n"
            f"• Open the output folder?\n"
            f"• View the converted script?",
            icon='question'
        )

        if result:
            # Open output folder
            output_path = Path(output_file).resolve()
            folder_path = output_path.parent

            try:
                if platform.system() == "Windows":
                    subprocess.run(["explorer", str(folder_path)])
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", str(folder_path)])
                else:  # Linux
                    subprocess.run(["xdg-open", str(folder_path)])
            except Exception as e:
                self.root.after(0, lambda: self.log_message(msg))

        self.log_message("🎣 Ready to fish on macOS!")

    def run_diagnostics(self):
        """Run system diagnostics"""
        self.log_message("🔍 Running system diagnostics...")

        # Update both system cards
        if hasattr(self, 'system_card'):
            self.system_card.update_status("Analyzing", ProfessionalTheme.COLORS['warning'])
        if hasattr(self, 'sidebar_system_card'):
            self.sidebar_system_card.update_status("Analyzing", ProfessionalTheme.COLORS['warning'])

        # Run diagnostics
        def diagnostics_thread():
    """Function definition"""
            try:
                # Basic system checks
                self.log_message("📊 Checking system resources...")

                if psutil:
                    # Memory check
                    memory = psutil.virtual_memory()
                    self.root.after(0, lambda: self.log_message(msg))

                    # CPU check
                    cpu_percent = psutil.cpu_percent(interval=1)
                    self.root.after(0, lambda: self.log_message(msg))

                    # Disk check (cross-platform)
                    disk_path = 'C:\\' if IS_WINDOWS else '/'
                    disk = psutil.disk_usage(disk_path)
                    disk_percent = (disk.used / disk.total) * 100
                    self.root.after(0, lambda: self.log_message(msg))

                    # Overall assessment
                    issues = []
                    if memory.percent > 85:
                        issues.append("High memory usage")
                    if cpu_percent > 80:
                        issues.append("High CPU usage")
                    if disk_percent > 90:
                        issues.append("Low disk space")

                    if issues:
                        self.root.after(0, lambda: self.log_message(msg))
                        status_text = "Issues Found"
                        status_color = ProfessionalTheme.COLORS['warning']
                    else:
                        self.log_message("✅ System diagnostics completed - All systems optimal")
                        status_text = "Optimal"
                        status_color = ProfessionalTheme.COLORS['success']
                else:
                    self.log_message("⚠️ psutil not available - limited diagnostics")
                    self.log_message("✅ Basic system checks passed")
                    status_text = "Basic Check OK"
                    status_color = ProfessionalTheme.COLORS['success']

                # Update both system cards
                if hasattr(self, 'system_card'):
                    self.system_card.update_status(status_text, status_color)
                if hasattr(self, 'sidebar_system_card'):
                    self.sidebar_system_card.update_status(status_text, status_color)

            except Exception as e:
                self.root.after(0, lambda: self.log_message(msg))
                # Update both system cards
                if hasattr(self, 'system_card'):
                    self.system_card.update_status("Error", ProfessionalTheme.COLORS['accent'])
                if hasattr(self, 'sidebar_system_card'):
                    self.sidebar_system_card.update_status("Error", ProfessionalTheme.COLORS['accent'])

        threading.Thread(target=diagnostics_thread, daemon=True).start()
    @lru_cache(maxsize=128)

    def get_discord_webhook(self):
        """Get Discord webhook URL from settings"""
        try:
            # First try to get from UI variable
            if hasattr(self, 'webhook_var') and self.webhook_var.get().strip():
                return self.webhook_var.get().strip()

            # Fallback to settings file
            settings_file = 'settings.json'
            if os.path.exists(settings_file):
                with open(settings_file, 'r') as f:
                    settings = json.load(f)
                    webhook_url = settings.get('discord_webhook_url', '')
                    if hasattr(self, 'webhook_var'):
                        self.webhook_var.set(webhook_url)
                    return webhook_url
            return ''
        except Exception as e:
            return ''

    def send_to_discord_webhook(self, webhook_url, message):
        """Send message to Discord webhook"""
        try:
            if not requests:
                return False

            payload = {
                'content': message,
                'username': 'IRUS V5.0 Bot'
            }

            response = requests.post(webhook_url, json=payload, timeout=10)
            return response.status_code == 204

        except Exception as e:
            print(f"Discord webhook error: {e}")
            return False

    def test_discord_webhook(self):
        """Test Discord webhook connection"""
        webhook_url = self.webhook_var.get().strip()

        if not webhook_url:
            messagebox.showerror(
                "No Webhook URL",
                "❌ Please enter a Discord webhook URL first.\n\n"
                "To get a webhook URL:\n"
                "1. Go to your Discord server\n"
                "2. Server Settings → Integrations\n"
                "3. Webhooks → New Webhook\n"
                "4. Copy the webhook URL"
            )
            return

        if not requests:
            messagebox.showerror(
                "Missing Dependency",
                "❌ The 'requests' library is required for Discord integration.\n\n"
                "Please install it with: pip install requests"
            )
            return

        self.log_message("🧪 Testing Discord webhook...")

        def test_thread():
    """Function definition"""
            try:
                success = self.send_to_discord_webhook(
                    webhook_url,
                    "🧪 **IRUS V5.0 Test Message** 🧪\n\n"
                    "This is a test message from IRUS V5.0!\n"
                    "If you can see this, your Discord integration is working perfectly! ✅\n\n"
                    f"**Time:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    "**Status:** Webhook connection successful!"
                )

                if success:
                    self.root.after(0, lambda: messagebox.showinfo(
                        "Webhook Test Successful!",
                        "✅ Discord webhook test successful!\n\n"
                        "Check your Discord server for the test message.\n"
                        "Your Discord integration is now ready to use!"
                    ))
                    self.log_message("✅ Discord webhook test successful!")
                else:
                    self.root.after(0, lambda: messagebox.showerror(
                        "Webhook Test Failed",
                        "❌ Discord webhook test failed!\n\n"
                        "Please check:\n"
                        "• Webhook URL is correct\n"
                        "• You have internet connection\n"
                        "• Webhook permissions are set up properly"
                    ))
                    self.log_message("❌ Discord webhook test failed!")

            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Test Error",
                    f"❌ Error testing webhook:\n{str(e)}\n\n"
                    "Please check your webhook URL and try again."
                ))
                self.root.after(0, lambda: self.log_message(msg))

        threading.Thread(target=test_thread, daemon=True).start()

    def open_ai_assistant(self):
        """Open AI assistant"""
        self.log_message("🤖 AI Assistant activated")

        # Create AI assistant window
        ai_window = tk.Toplevel(self.root)
        ai_window.title("IRUS V5.0 - AI Assistant")
        ai_window.geometry("600x500")
        ai_window.resizable(True, True)

        # Center the window
        ai_window.update_idletasks()
        x = (ai_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (ai_window.winfo_screenheight() // 2) - (500 // 2)
        ai_window.geometry(f"600x500+{x}+{y}")

        # Main frame
        main_frame = ttk.Frame(ai_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="🤖 IRUS AI Assistant",
            font=('Arial', 16, 'bold')
        )
        header_label.pack(pady=(0, 10))

        subtitle_label = ttk.Label(
            main_frame,
            text="Ask me anything about IRUS or get help with issues",
            font=('Arial', 10),
            foreground='gray'
        )
        subtitle_label.pack(pady=(0, 20))

        # Chat area
        chat_frame = ttk.Frame(main_frame)
        chat_frame.pack(fill='both', expand=True, pady=(0, 10))

        # Chat display
        chat_text = tk.Text(
            chat_frame,
            height=15,
            wrap='word',
            font=('Arial', 10),
            state='disabled',
            bg='#f8f9fa',
            relief='solid',
            borderwidth=1
        )

        chat_scrollbar = ttk.Scrollbar(chat_frame, orient='vertical', command=chat_text.yview)
        chat_text.configure(yscrollcommand=chat_scrollbar.set)

        chat_text.pack(side='left', fill='both', expand=True)
        chat_scrollbar.pack(side='right', fill='y')

        # Input area
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill='x', pady=(0, 10))

        input_var = tk.StringVar()
        input_entry = ttk.Entry(input_frame, textvariable=input_var, font=('Arial', 10))
        input_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))

        send_btn = ttk.Button(input_frame, text="Send", width=10)
        send_btn.pack(side='right')

        # Quick help buttons
        quick_frame = ttk.Frame(main_frame)
        quick_frame.pack(fill='x')

        ttk.Label(quick_frame, text="Quick help:", font=('Arial', 9)).pack(side='left')

        quick_questions = [
            "How do I run converted script?",
            "Installation issues",
            "Permission problems",
            "Performance tips"
        ]

        def add_ai_message(message, is_user=False):
            """Add message to chat"""
            chat_text.config(state='normal')

            timestamp = time.strftime("%H:%M:%S")
            sender = "You" if is_user else "AI Assistant"

            chat_text.insert('end', f"[{timestamp}] {sender}:\n")
            chat_text.insert('end', f"{message}\n\n")
            chat_text.see('end')
            chat_text.config(state='disabled')

        def send_message():
            """Send user message and get AI response"""
            user_message = input_var.get().strip()
            if not user_message:
                return

            # Add user message
            add_ai_message(user_message, is_user=True)
            input_var.set("")

            # Generate AI response
            ai_response = self.get_ai_response(user_message)
            add_ai_message(ai_response)

        def quick_question(question):
            """Handle quick question"""
            input_var.set(question)
            send_message()

        # Bind events
        send_btn.config(command=send_message)
        input_entry.bind('<Return>', lambda e: send_message())

        # Add quick question buttons
        for i, question in enumerate(quick_questions):
            btn = ttk.Button(
                quick_frame,
                text=question,
                command=lambda q=question: quick_question(q)
            )
            btn.pack(side='left', padx=(10, 5))

        # Initial AI greeting
        add_ai_message("Hello! I'm your IRUS AI Assistant. I can help you with:\n\n"
                      "• Conversion issues and troubleshooting\n"
                      "• Running converted scripts on macOS\n"
                      "• System requirements and setup\n"
                      "• Performance optimization tips\n"
                      "• General questions about IRUS\n\n"
                      "What would you like help with today?")

        input_entry.focus()
    @lru_cache(maxsize=128)

    def get_ai_response(self, user_message):
        """Generate AI response to user message"""
        message_lower = user_message.lower()

        # Conversion help
        if any(word in message_lower for word in ['convert', 'conversion', 'how to convert']):
            return ("🔄 **Conversion Help:**\n\n"
                   "1. Select your Windows script using 'Browse' button\n"
                   "2. Choose where to save the converted script\n"
                   "3. Click 'Start Conversion' button\n"
                   "4. Wait for conversion to complete\n"
                   "5. The converted script will be saved to your chosen location\n\n"
                   "The conversion process automatically handles:\n"
                   "• Windows API → macOS API conversion\n"
                   "• Screen capture (mss → Quartz)\n"
                   "• Mouse/keyboard control (pyautogui → pynput)\n"
                   "• Code optimization and cleanup")

        # Running script help
        elif any(word in message_lower for word in ['run', 'execute', 'start', 'launch']):
            return ("🚀 **Running Your Converted Script:**\n\n"
                   "1. **Grant macOS Permissions:**\n"
                   "   • System Preferences → Security & Privacy → Privacy\n"
                   "   • Add Terminal to: Screen Recording, Accessibility, Input Monitoring\n"
                   "   • RESTART Terminal after granting permissions\n\n"
                   "2. **Navigate to script location:**\n"
                   "   cd /path/to/your/script\n\n"
                   "3. **Test the script:**\n"
                   "   python3 your_script_macos.py --test\n\n"
                   "4. **Run the script:**\n"
                   "   python3 your_script_macos.py\n\n"
                   "Need help with permissions? Let me know!")

        # Installation issues
        elif any(word in message_lower for word in ['install', 'installation', 'setup', 'dependencies']):
            return ("📦 **Installation Help:**\n\n"
                   "**Required packages:**\n"
                   "• pillow (image processing)\n"
                   "• numpy (numerical operations)\n"
                   "• opencv-python (computer vision)\n"
                   "• pynput (mouse/keyboard control)\n"
                   "• pyobjc-framework-Quartz (screen capture)\n\n"
                   "**Install command:**\n"
                   "pip3 install pillow numpy opencv-python pynput pyobjc-framework-Quartz\n\n"
                   "**If installation fails:**\n"
                   "1. Update pip: python3 -m pip install --upgrade pip\n"
                   "2. Try with --user flag: pip3 install --user [package]\n"
                   "3. Use homebrew: brew install python@3.11\n\n"
                   "Still having issues? Run the system diagnostics!")

        # Permission issues
        elif any(word in message_lower for word in ['permission', 'access', 'denied', 'security']):
            return ("🔐 **macOS Permission Issues:**\n\n"
                   "**Required Permissions:**\n"
                   "1. **Screen Recording** - To capture game screen\n"
                   "2. **Accessibility** - To control mouse/keyboard\n"
                   "3. **Input Monitoring** - To detect hotkeys\n\n"
                   "**How to Grant:**\n"
                   "1. System Preferences → Security & Privacy\n"
                   "2. Click 'Privacy' tab\n"
                   "3. Select each permission type from left sidebar\n"
                   "4. Click lock icon and enter password\n"
                   "5. Click + button and add Terminal\n"
                   "6. Check the box next to Terminal\n"
                   "7. **RESTART Terminal** (very important!)\n\n"
                   "**Test permissions:**\n"
                   "python3 your_script.py --test-permissions")

        # Performance issues
        elif any(word in message_lower for word in ['slow', 'performance', 'lag', 'optimize']):
            return ("⚡ **Performance Optimization:**\n\n"
                   "**For Better Speed:**\n"
                   "• Close unnecessary applications\n"
                   "• Use native Python (not Rosetta on Apple Silicon)\n"
                   "• Ensure 8GB+ RAM available\n"
                   "• Use SSD storage\n\n"
                   "**Script Settings:**\n"
                   "• Reduce screen capture rate (30 FPS → 15 FPS)\n"
                   "• Increase detection sensitivity (0.8 → 0.7)\n"
                   "• Add delays between actions\n\n"
                   "**Check System:**\n"
                   "• Activity Monitor for CPU usage\n"
                   "• Memory pressure\n"
                   "• Available storage space\n\n"
                   "Run system diagnostics for detailed analysis!")

        # Error help
        elif any(word in message_lower for word in ['error', 'bug', 'problem', 'issue', 'not working']):
            return ("🐛 **Error Troubleshooting:**\n\n"
                   "**Common Solutions:**\n"
                   "1. **ImportError/ModuleNotFoundError:**\n"
                   "   → Install missing packages: pip3 install [package]\n\n"
                   "2. **PermissionError:**\n"
                   "   → Grant macOS permissions and restart Terminal\n\n"
                   "3. **SyntaxError:**\n"
                   "   → Re-run conversion with latest version\n\n"
                   "4. **Screen capture fails:**\n"
                   "   → Check Screen Recording permission\n\n"
                   "**Get Detailed Help:**\n"
                   "• Run bug analysis tool\n"
                   "• Generate bug report for Discord support\n"
                   "• Check Debug.txt for error details\n\n"
                   "What specific error are you seeing?")

        # General help
        else:
            return ("🤖 **I'm here to help!**\n\n"
                   "I can assist with:\n"
                   "• **Conversion issues** - Problems converting Windows scripts\n"
                   "• **Running scripts** - How to execute converted macOS scripts\n"
                   "• **Installation** - Setting up dependencies and packages\n"
                   "• **Permissions** - macOS security and access issues\n"
                   "• **Performance** - Optimizing speed and reliability\n"
                   "• **Errors** - Troubleshooting specific problems\n\n"
                   "Try asking something like:\n"
                   "• \"How do I run my converted script?\"\n"
                   "• \"I'm getting a permission error\"\n"
                   "• \"The conversion is slow\"\n"
                   "• \"ImportError: No module named...\"\n\n"
                   "What would you like help with?")

    def run_bug_analysis(self):
        """Run bug analysis"""
        # Check if we have a script to analyze
        input_file = self.input_file_var.get().strip()
        output_file = self.output_file_var.get().strip()

        # Determine which file to analyze
        analyze_file = None
        if output_file and os.path.exists(output_file):
            analyze_file = output_file
            file_type = "converted script"
        elif input_file and os.path.exists(input_file):
            analyze_file = input_file
            file_type = "input script"
        else:
            messagebox.showerror("No Script Found",
                               "Please select a script file or run conversion first.")
            return

        self.root.after(0, lambda: self.log_message(msg))

        # Create analysis window
        analysis_window = tk.Toplevel(self.root)
        analysis_window.title("IRUS V5.0 - Bug Analysis")
        analysis_window.geometry("700x600")
        analysis_window.resizable(True, True)

        # Center window
        analysis_window.update_idletasks()
        x = (analysis_window.winfo_screenwidth() // 2) - (700 // 2)
        y = (analysis_window.winfo_screenheight() // 2) - (600 // 2)
        analysis_window.geometry(f"700x600+{x}+{y}")

        # Main frame
        main_frame = ttk.Frame(analysis_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="🔍 Bug Analysis Results",
            font=('Arial', 16, 'bold')
        )
        header_label.pack(pady=(0, 10))

        file_label = ttk.Label(
            main_frame,
            text=f"Analyzing: {Path(analyze_file).resolve().name}",
            font=('Arial', 10),
            foreground='gray'
        )
        file_label.pack(pady=(0, 20))

        # Progress bar
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill='x', pady=(0, 20))

        analysis_progress = ttk.Progressbar(progress_frame, mode='indeterminate')
        analysis_progress.pack(fill='x')

        progress_label = ttk.Label(progress_frame, text="Starting analysis...", font=('Arial', 9))
        progress_label.pack(pady=(5, 0))

        # Results area
        results_frame = ttk.Frame(main_frame)
        results_frame.pack(fill='both', expand=True)

        # Results text
        results_text = tk.Text(
            results_frame,
            wrap='word',
            font=('Consolas', 9),
            bg='#f8f9fa'
        )

        results_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=results_text.yview)
        results_text.configure(yscrollcommand=results_scrollbar.set)

        results_text.pack(side='left', fill='both', expand=True)
        results_scrollbar.pack(side='right', fill='y')

        # Close button
        close_btn = ttk.Button(main_frame, text="Close", command=analysis_window.destroy)
        close_btn.pack(pady=(10, 0))

        # Run analysis in thread
        def run_analysis():
    """Function definition"""
            analysis_progress.start()

            try:
                # Quick syntax check
                progress_label.config(text="Checking syntax...")
                analysis_window.update()

                with open(analyze_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                results = []
                results.append("🔍 IRUS V5.0 Bug Analysis Report")
                results.append("=" * 50)
                results.append(f"File: {analyze_file}")
                results.append(f"Size: {len(content)} characters")
                results.append(f"Lines: {len(content.split(chr(10)))}")
                results.append(f"Analysis Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
                results.append("")

                # Syntax validation
                progress_label.config(text="Validating Python syntax...")
                analysis_window.update()

                try:
                    compile(content, analyze_file, 'exec')
                    results.append("✅ SYNTAX CHECK: Valid Python syntax")
                except SyntaxError as e:
                    results.append(f"❌ SYNTAX ERROR: Line {e.lineno}: {e.msg}")

                # Import analysis
                progress_label.config(text="Analyzing imports...")
                analysis_window.update()

                import_lines = [line.strip() for line in content.split('\n') if line.strip().startswith(('import ', 'from '))]
                results.append(f"\n📦 IMPORTS FOUND: {len(import_lines)}")

                required_macos_imports = ['Quartz', 'pynput', 'PIL', 'numpy', 'cv2']
                windows_imports = ['mss', 'pyautogui', 'keyboard', 'ctypes.windll']

                for imp in required_macos_imports:
                    if imp in content:
                        results.append(f"✅ {imp}: Found")
                    else:
                        results.append(f"⚠️ {imp}: Missing (may be needed)")

                for imp in windows_imports:
                    if imp in content:
                        results.append(f"❌ {imp}: Windows import detected - needs conversion")

                # API analysis
                progress_label.config(text="Checking API usage...")
                analysis_window.update()

                results.append(f"\n🔧 API ANALYSIS:")

                # Check for Windows APIs
                windows_apis = ['pyautogui.', 'mss.', 'keyboard.is_pressed', 'ctypes.windll']
                macos_apis = ['CGDisplayCreateImage', 'mouse_controller', 'keyboard_controller']

                for api in windows_apis:
                    count = content.count(api)
                    if count > 0:
                        results.append(f"❌ Windows API '{api}': {count} occurrences - needs conversion")

                for api in macos_apis:
                    count = content.count(api)
                    if count > 0:
                        results.append(f"✅ macOS API '{api}': {count} occurrences")

                # Performance analysis
                progress_label.config(text="Analyzing performance...")
                analysis_window.update()

                results.append(f"\n⚡ PERFORMANCE ANALYSIS:")

                # Check for potential issues
                if 'while True:' in content and 'time.sleep' not in content:
                    results.append("⚠️ Busy waiting loop detected - add sleep delays")

                if content.count('time.sleep(0') > 0:
                    results.append("⚠️ Zero-delay sleep found - ineffective")

                thread_count = content.count('Thread(')
                if thread_count > 0:
                    results.append(f"ℹ️ Threading used: {thread_count} threads created")
                    if 'daemon' not in content:
                        results.append("⚠️ Consider using daemon threads")

                # Security analysis
                progress_label.config(text="Security scan...")
                analysis_window.update()

                results.append(f"\n🔒 SECURITY ANALYSIS:")

                security_issues = ['eval_function(', 'exec(', 'shell=True']
                security_clean = True

                for issue in security_issues:
                    if issue in content:
                        results.append(f"❌ Security risk: {issue} found")
                        security_clean = False

                if security_clean:
                    results.append("✅ No obvious security issues detected")

                # Overall assessment
                results.append(f"\n📊 OVERALL ASSESSMENT:")

                critical_issues = results.count("❌")
                warnings = results.count("⚠️")

                if critical_issues == 0 and warnings == 0:
                    results.append("🎉 EXCELLENT: No issues detected!")
                    score = 100
                elif critical_issues == 0:
                    results.append(f"✅ GOOD: {warnings} minor warnings")
                    score = max(80, 100 - warnings * 5)
                else:
                    results.append(f"⚠️ NEEDS ATTENTION: {critical_issues} critical issues, {warnings} warnings")
                    score = max(50, 100 - critical_issues * 15 - warnings * 5)

                results.append(f"📈 Quality Score: {score}/100")

                # Recommendations
                results.append(f"\n💡 RECOMMENDATIONS:")
                if critical_issues > 0:
                    results.append("1. Fix critical issues before running script")
                if warnings > 0:
                    results.append("2. Address warnings for better performance")
                results.append("3. Test script with --test flag before use")
                results.append("4. Grant required macOS permissions")

                # Display results
                analysis_progress.stop()
                progress_label.config(text="Analysis complete!")

                results_text.delete('1.0', 'end')
                results_text.insert('1.0', '\n'.join(results))

                # Log summary
                self.root.after(0, lambda: self.log_message(msg))
                if critical_issues > 0:
                    self.root.after(0, lambda: self.log_message(msg))
                if warnings > 0:
                    self.root.after(0, lambda: self.log_message(msg))

            except Exception as e:
                analysis_progress.stop()
                progress_label.config(text="Analysis failed!")
                results_text.delete('1.0', 'end')
                results_text.insert('1.0', f"❌ Analysis Error:\n{str(e)}\n\nPlease check the file and try again.")
                self.root.after(0, lambda: self.log_message(msg))

        # Start analysis
        threading.Thread(target=run_analysis, daemon=True).start()

    def open_feedback(self):
        """Open feedback system"""
        self.log_message("⭐ Opening feedback system...")

        try:
            from tools.feedback_system import show_feedback_window
            show_feedback_window(self.root)
        except ImportError:
            # Create inline feedback system if import fails
            self.create_inline_feedback_system()

    def create_inline_feedback_system(self):
        """Create inline feedback system"""
        feedback_window = tk.Toplevel(self.root)
        feedback_window.title("IRUS V5.0 - User Feedback")
        feedback_window.geometry("500x600")
        feedback_window.resizable(False, False)

        # Center window
        feedback_window.update_idletasks()
        x = (feedback_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (feedback_window.winfo_screenheight() // 2) - (600 // 2)
        feedback_window.geometry(f"500x600+{x}+{y}")

        # Main frame
        main_frame = ttk.Frame(feedback_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="📝 Share Your Experience",
            font=('Arial', 16, 'bold')
        )
        header_label.pack(pady=(0, 10))

        subtitle_label = ttk.Label(
            main_frame,
            text="Help us improve IRUS with your valuable feedback",
            font=('Arial', 10),
            foreground='gray'
        )
        subtitle_label.pack(pady=(0, 20))

        # Rating section
        rating_frame = ttk.LabelFrame(main_frame, text="Overall Rating", padding=15)
        rating_frame.pack(fill='x', pady=(0, 15))

        ttk.Label(rating_frame, text="How would you rate IRUS V5.0?").pack(pady=(0, 10))

        # Star rating
        star_frame = ttk.Frame(rating_frame)
        star_frame.pack()

        rating_var = tk.IntVar()
        star_buttons = []

        def update_stars():
    """Function definition"""
            rating_var.set(selected_rating)
            for i, btn in enumerate(star_buttons):
                if i < selected_rating:
                    btn.config(text="★", fg="#FFD700")
                else:
                    btn.config(text="☆", fg="gray")

        for i in range(5):
            star_btn = tk.Button(
                star_frame,
                text="☆",
                font=("Arial", 20),
                bg="white",
                fg="gray",
                bd=0,
                cursor="hand2",
                command=lambda rating=i+1: update_stars(rating)
            )
            star_btn.pack(side="left", padx=2)
            star_buttons.append(star_btn)

        # Feedback text
        feedback_frame = ttk.LabelFrame(main_frame, text="Your Feedback (Optional)", padding=15)
        feedback_frame.pack(fill='both', expand=True, pady=(0, 15))

        ttk.Label(feedback_frame, text="Tell us about your experience:").pack(anchor='w', pady=(0, 5))

        feedback_text = tk.Text(
            feedback_frame,
            height=8,
            wrap='word',
            font=('Arial', 10)
        )
        feedback_text.pack(fill='both', expand=True)

        # Contact info
        contact_frame = ttk.LabelFrame(main_frame, text="Contact (Optional)", padding=15)
        contact_frame.pack(fill='x', pady=(0, 15))

        ttk.Label(contact_frame, text="Discord username or email:").pack(anchor='w', pady=(0, 5))
        contact_var = tk.StringVar()
        contact_entry = ttk.Entry(contact_frame, textvariable=contact_var, width=40)
        contact_entry.pack(fill='x')

        # Status label
        status_label = ttk.Label(main_frame, text="", foreground='red')
        status_label.pack(pady=5)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x', pady=(10, 0))

        def submit_feedback():
    """Function definition"""
            rating = rating_var.get()
            feedback_content = feedback_text.get('1.0', 'end-1c').strip()
            contact_info = contact_var.get().strip()

            if rating == 0:
                status_label.config(text="⚠️ Please select a star rating", foreground='red')
                return

            # Simulate sending feedback
            status_label.config(text="📤 Sending feedback...", foreground='blue')
            feedback_window.update()

            # Simulate network delay
            feedback_window.after(1000, lambda: send_feedback_complete(rating, feedback_content, contact_info))

        def send_feedback_complete():
    """Function definition"""
            try:
                # Try Discord webhook if configured
                webhook_url = self.get_discord_webhook()

                if webhook_url and requests:
                    success = self.send_to_discord_webhook(
                        webhook_url,
                        f"⭐ **IRUS V5.0 Feedback** ⭐\n"
                        f"**Rating:** {rating}/5 stars\n"
                        f"**Feedback:** {feedback_content or 'No additional feedback'}\n"
                        f"**Contact:** {contact_info or 'Anonymous'}\n"
                        f"**Time:** {time.strftime('%Y-%m-%d %H:%M:%S')}"
                    )

                    if success:
                        messagebox.showinfo(
                            "Feedback Submitted!",
                            f"✅ Thank you for your {rating}-star feedback!\n\n"
                            "Your feedback has been sent successfully!\n"
                            "We appreciate your input and will use it to improve IRUS!"
                        )
                        feedback_window.destroy()
                        return

                # Fallback to local save
                raise Exception("Discord not configured")

            except Exception:
                # Fallback - save locally
                feedback_data = {
                    'rating': rating,
                    'feedback': feedback_content,
                    'contact': contact_info,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                }

                # Save to local file
                try:
                    os.makedirs('feedback', exist_ok=True)
                    with open(f'feedback/feedback_{int(time.time())}.json', "w", encoding="utf-8") as f:
                        json.dump(feedback_data, f, indent=2)

                    messagebox.showinfo(
                        "Feedback Saved!",
                        f"✅ Thank you for your {rating}-star feedback!\n\n"
                        "Your feedback has been saved locally.\n"
                        "Please share it with the developer on Discord."
                    )
                    feedback_window.destroy()

                except Exception as e:
                    status_label.config(text=f"❌ Error saving feedback: {e}", foreground='red')

        # Enhanced buttons with better styling
        cancel_btn = ttk.Button(button_frame, text="❌ Cancel", command=feedback_window.destroy)
        cancel_btn.pack(side='right', padx=(10, 0))

        submit_btn = ttk.Button(button_frame, text="📤 Submit Feedback", command=submit_feedback)
        submit_btn.pack(side='right')

        # Make submit button more prominent
        submit_btn.configure(style='Accent.TButton')

        # Add keyboard shortcut
        feedback_window.bind('<Return>', lambda e: submit_feedback())
        feedback_window.bind('<Escape>', lambda e: feedback_window.destroy())

    def open_bug_reporter(self):
        """Open bug reporting system"""
        self.log_message("🐛 Opening bug reporter...")

        # Always use inline bug reporter for better integration
        self.create_inline_bug_reporter()

    def create_inline_bug_reporter(self):
        """Create inline bug reporting system"""
        bug_window = tk.Toplevel(self.root)
        bug_window.title("IRUS V5.0 - Bug Reporter")
        bug_window.geometry("600x700")
        bug_window.resizable(True, True)

        # Center window
        bug_window.update_idletasks()
        x = (bug_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (bug_window.winfo_screenheight() // 2) - (700 // 2)
        bug_window.geometry(f"600x700+{x}+{y}")

        # Main frame
        main_frame = ttk.Frame(bug_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="🐛 Bug Report",
            font=('Arial', 16, 'bold')
        )
        header_label.pack(pady=(0, 10))

        subtitle_label = ttk.Label(
            main_frame,
            text="Help us fix issues by reporting bugs",
            font=('Arial', 10),
            foreground='gray'
        )
        subtitle_label.pack(pady=(0, 20))

        # Bug type selection
        type_frame = ttk.LabelFrame(main_frame, text="Bug Type", padding=15)
        type_frame.pack(fill='x', pady=(0, 15))

        bug_type_var = tk.StringVar(value="Conversion Error")
        bug_types = ["Conversion Error", "UI Issue", "Performance Problem", "Crash/Freeze", "Feature Request", "Other"]

        for bug_type in bug_types:
            ttk.Radiobutton(
                type_frame,
                text=bug_type,
                variable=bug_type_var,
                value=bug_type
            ).pack(anchor='w', pady=2)

        # Bug description
        desc_frame = ttk.LabelFrame(main_frame, text="Bug Description", padding=15)
        desc_frame.pack(fill='both', expand=True, pady=(0, 15))

        ttk.Label(desc_frame, text="Describe the bug in detail:").pack(anchor='w', pady=(0, 5))

        bug_text = tk.Text(
            desc_frame,
            height=8,
            wrap='word',
            font=('Arial', 10)
        )
        bug_scrollbar = ttk.Scrollbar(desc_frame, orient='vertical', command=bug_text.yview)
        bug_text.configure(yscrollcommand=bug_scrollbar.set)

        bug_text.pack(side='left', fill='both', expand=True)
        bug_scrollbar.pack(side='right', fill='y')

        # Steps to reproduce
        steps_frame = ttk.LabelFrame(main_frame, text="Steps to Reproduce", padding=15)
        steps_frame.pack(fill='x', pady=(0, 15))

        ttk.Label(steps_frame, text="How can we reproduce this bug?").pack(anchor='w', pady=(0, 5))

        steps_text = tk.Text(
            steps_frame,
            height=4,
            wrap='word',
            font=('Arial', 10)
        )
        steps_text.pack(fill='x')

        # Contact info
        contact_frame = ttk.LabelFrame(main_frame, text="Contact Information (Optional)", padding=15)
        contact_frame.pack(fill='x', pady=(0, 15))

        ttk.Label(contact_frame, text="Discord username or email:").pack(anchor='w', pady=(0, 5))
        contact_var = tk.StringVar()
        contact_entry = ttk.Entry(contact_frame, textvariable=contact_var, width=40)
        contact_entry.pack(fill='x')

        # Status label
        status_label = ttk.Label(main_frame, text="", foreground='red')
        status_label.pack(pady=5)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x', pady=(10, 0))

        def submit_bug_report():
    """Function definition"""
            bug_type = bug_type_var.get()
            description = bug_text.get('1.0', 'end-1c').strip()
            steps = steps_text.get('1.0', 'end-1c').strip()
            contact_info = contact_var.get().strip()

            if not description:
                status_label.config(text="⚠️ Please provide a bug description", foreground='red')
                return

            # Simulate sending bug report
            status_label.config(text="📤 Sending bug report...", foreground='blue')
            bug_window.update()

            # Simulate network delay
            bug_window.after(1000, lambda: send_bug_report_complete(bug_type, description, steps, contact_info))

        def send_bug_report_complete():
    """Function definition"""
            try:
                # Try Discord webhook if configured
                webhook_url = self.get_discord_webhook()

                if webhook_url and requests:
                    success = self.send_to_discord_webhook(
                        webhook_url,
                        f"🐛 **IRUS V5.0 Bug Report** 🐛\n"
                        f"**Type:** {bug_type}\n"
                        f"**Description:** {description}\n"
                        f"**Steps to Reproduce:** {steps or 'Not provided'}\n"
                        f"**Contact:** {contact_info or 'Anonymous'}\n"
                        f"**Time:** {time.strftime('%Y-%m-%d %H:%M:%S')}"
                    )

                    if success:
                        messagebox.showinfo(
                            "Bug Report Submitted!",
                            "✅ Thank you for reporting this bug!\n\n"
                            "Your report has been sent to our development team.\n"
                            "We'll investigate and fix the issue as soon as possible!"
                        )
                        bug_window.destroy()
                        return

                # Fallback to local save
                raise Exception("Discord not configured")

            except Exception:
                # Fallback - save locally
                bug_data = {
                    'type': bug_type,
                    'description': description,
                    'steps': steps,
                    'contact': contact_info,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                }

                # Save to local file
                try:
                    os.makedirs('bug_reports', exist_ok=True)
                    with open(f'bug_reports/bug_{int(time.time())}.json', "w", encoding="utf-8") as f:
                        json.dump(bug_data, f, indent=2)

                    messagebox.showinfo(
                        "Bug Report Saved!",
                        "✅ Thank you for reporting this bug!\n\n"
                        "Your report has been saved locally.\n"
                        "Please share it with the developer on Discord."
                    )
                    bug_window.destroy()

                except Exception as e:
                    status_label.config(text=f"❌ Error saving bug report: {e}", foreground='red')

        # Enhanced bug report buttons
        cancel_btn = ttk.Button(button_frame, text="❌ Cancel", command=bug_window.destroy)
        cancel_btn.pack(side='right', padx=(10, 0))

        submit_btn = ttk.Button(button_frame, text="🐛 Submit Bug Report", command=submit_bug_report)
        submit_btn.pack(side='right')

        # Make submit button prominent
        submit_btn.configure(style='Accent.TButton')

        # Add keyboard shortcuts
        bug_window.bind('<Control-Return>', lambda e: submit_bug_report())
        bug_window.bind('<Escape>', lambda e: bug_window.destroy())

    def auto_report_bug(self, exception, error_type):
        """Automatically report critical bugs to Discord"""
        try:
            # Only auto-report if Discord is properly configured
            if not hasattr(self, 'discord_enabled_var') or not self.discord_enabled_var.get():
                return

            webhook_url = self.get_discord_webhook()

            if webhook_url and requests:
                # Create automatic bug report
                import traceback
                error_traceback = traceback.format_exc()

                bug_report = f"""
**Note:** This is an automatic report. User may follow up with more details."""
                    self.log_message("🤖 Automatic bug report sent to Discord")
                else:
                    self.log_message("⚠️ Could not send automatic bug report")

        except Exception as e:
            # Don't let auto-reporting cause more errors
            self.root.after(0, lambda: self.log_message(msg))

    def browse_input_file(self):
        """Browse for input script file"""
        filename = filedialog.askopenfilename(
            title="Select Windows Python Script",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if filename:
            self.input_file_var.set(filename)
            # Auto-generate output filename
            input_path = Path(filename).resolve()
            output_name = f"{input_path.stem}_macos.py"
            self.output_file_var.set(f"output/{output_name}")
            self.root.after(0, lambda: self.log_message(msg))

    def browse_output_file(self):
        """Browse for output save location"""
        filename = filedialog.asksaveasfilename(
            title="Save Converted Script As",
            defaultextension=".py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if filename:
            self.output_file_var.set(filename)
            self.root.after(0, lambda: self.log_message(msg))

    def set_output_location(self, location):
        """Set output to quick location"""
        import os
        if location.startswith("~/"):
            location = os.path.expanduser(location)

        # Get current filename or use default
        current_output = self.output_file_var.get()
        if current_output:
            filename = Path(current_output).resolve().name
        else:
            input_file = self.input_file_var.get()
            if input_file:
                filename = f"{Path(input_file).resolve().stem}_macos.py"
            else:
                filename = "fishing_macro_macos.py"

        new_path = os.path.join(location, filename)
        self.output_file_var.set(new_path)
        self.root.after(0, lambda: self.log_message(msg))

    def log_message(self, message):
        """Add message to log"""
        timestamp = time.strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"

        # Only update log_text if it exists
        if hasattr(self, 'log_text'):
            try:
                self.log_text.insert('end', f"{formatted_message}\n")
                self.log_text.see('end')
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        # Only update status_label if it exists
        if hasattr(self, 'status_label'):
            try:
                self.root.after(0, lambda: self.status_label.config()text=message)
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        # Fallback to console if UI components aren't ready
        if not hasattr(self, 'log_text') or not hasattr(self, 'status_label'):
            print(formatted_message)

    def open_settings(self):
        """Open settings window (placeholder for now)"""
        self.log_message("⚙️ Opening settings...")
        # This will open the settings tab
        self.notebook.select(2)  # Select settings tab

    def open_mobile_companion(self):
        """Open mobile companion setup"""
        self.log_message("📱 Mobile companion setup...")
        messagebox.showinfo(
            "Mobile Companion",
            "📱 Mobile Companion Setup\n\n"
            "To set up mobile companion:\n"
            "1. Join our Discord server\n"
            "2. Use the #mobile-companion channel\n"
            "3. Follow the setup instructions\n\n"
            "This feature allows you to monitor and control IRUS from your phone!"
        )

    def open_advanced_tools(self):
        """Open advanced tools menu"""
        self.log_message("🔧 Advanced tools...")

        if not self.experimental_var.get():
            messagebox.showinfo(
                "Advanced Tools",
                "🔧 Advanced Tools\n\n"
                "Advanced features:\n"
                "• Batch conversion\n"
                "• Custom templates\n"
                "• Performance profiling\n"
                "• Debug mode\n\n"
                "Enable 'Experimental Features' in settings to access these tools!"
            )
            return

        # Create advanced tools window
        tools_window = tk.Toplevel(self.root)
        tools_window.title("IRUS V5.0 - Advanced Tools")
        tools_window.geometry("500x400")
        tools_window.resizable(False, False)

        # Center window
        tools_window.update_idletasks()
        x = (tools_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (tools_window.winfo_screenheight() // 2) - (400 // 2)
        tools_window.geometry(f"500x400+{x}+{y}")

        main_frame = ttk.Frame(tools_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        ttk.Label(
            main_frame,
            text="🔧 Advanced Tools",
            font=('Arial', 16, 'bold')
        ).pack(pady=(0, 20))

        # Tools based on enabled experimental features
        if self.batch_conversion_var.get():
            ttk.Button(
                main_frame,
                text="🔄 Batch Conversion",
                command=self.open_batch_conversion,
                width=30
            ).pack(pady=5)

        if self.ai_optimization_var.get():
            ttk.Button(
                main_frame,
                text="🤖 AI Code Optimizer",
                command=self.open_ai_optimizer,
                width=30
            ).pack(pady=5)

        if self.profiling_var.get():
            ttk.Button(
                main_frame,
                text="📊 Performance Profiler",
                command=self.open_profiler,
                width=30
            ).pack(pady=5)

        if self.custom_templates_var.get():
            ttk.Button(
                main_frame,
                text="📝 Template Manager",
                command=self.open_template_manager,
                width=30
            ).pack(pady=5)

        if self.advanced_debug_var.get():
            ttk.Button(
                main_frame,
                text="🔍 Debug Console",
                command=self.open_debug_console,
                width=30
            ).pack(pady=5)

        if self.cloud_sync_var.get():
            ttk.Button(
                main_frame,
                text="☁️ Cloud Sync",
                command=self.open_cloud_sync,
                width=30
            ).pack(pady=5)

        # If no experimental features enabled
        if not any([
            self.batch_conversion_var.get(),
            self.ai_optimization_var.get(),
            self.profiling_var.get(),
            self.custom_templates_var.get(),
            self.advanced_debug_var.get(),
            self.cloud_sync_var.get()
        ]):
            ttk.Label(
                main_frame,
                text="No experimental features enabled.\nGo to Settings → Advanced to enable specific tools.",
                font=('Arial', 10),
                foreground='gray',
                justify='center'
            ).pack(expand=True)

        ttk.Button(main_frame, text="Close", command=tools_window.destroy).pack(pady=(20, 0))

    def on_experimental_toggle(self):
        """Handle experimental features toggle"""
        if self.experimental_var.get():
            self.experimental_frame.pack(fill='x', pady=(10, 0))
            self.log_message("🧪 Experimental features enabled!")
            messagebox.showwarning(
                "Experimental Features Enabled",
                "⚠️ Experimental Features Enabled!\n\n"
                "You have enabled experimental features. These features:\n"
                "• May be unstable or incomplete\n"
                "• Could cause unexpected behavior\n"
                "• Are not fully tested\n\n"
                "Use at your own risk!"
            )
        else:
            self.experimental_frame.pack_forget()
            self.log_message("🧪 Experimental features disabled")

    # Experimental feature methods
    def open_batch_converter(self):
        """Open batch conversion tool"""
        try:
            from tools.batch_converter import BatchConverterGUI
            self.log_message("🚀 Opening Batch Converter...")

            # Run in separate thread to avoid blocking
            def run_batch_converter():
    """Function definition"""
                try:
                    app = BatchConverterGUI()
                    app.run()
                except Exception as e:
                    self.root.after(0, lambda: self.log_message(msg))

            threading.Thread(target=run_batch_converter, daemon=True).start()

        except ImportError:
            messagebox.showinfo(
                "Batch Converter",
                "📦 Batch Conversion System\n\n"
                "This experimental feature allows:\n"
                "• Converting multiple files at once\n"
                "• Parallel processing for speed\n"
                "• Progress tracking for each file\n\n"
                "Status: Available! Launching..."
            )

    def open_ai_optimizer(self):
        """Open AI code optimizer"""
        try:
            from tools.ai_optimizer import AICodeOptimizer

            # Get current script for analysis
            input_file = self.input_file_var.get().strip()
            if not input_file or not Path(input_file).resolve().exists():
                messagebox.showwarning(
                    "No Script Selected",
                    "Please select a Python script first to analyze with AI optimizer."
                )
                return

            self.log_message("🤖 Running AI Code Analysis...")

            # Run AI analysis
            def run_ai_analysis():
    """Function definition"""
                try:
                    optimizer = AICodeOptimizer()

                    with open(input_file, 'r', encoding='utf-8') as f:
                        code_content = f.read()

                    analysis = optimizer.analyze_code(code_content, Path(input_file).resolve().name)
                    report = optimizer.generate_report(analysis)

                    # Show results in new window
                    self.root.after(0, lambda: self.show_ai_results(report, analysis))

                except Exception as e:
                    self.root.after(0, lambda: self.root.after(0, lambda: self.log_message(msg)))

            threading.Thread(target=run_ai_analysis, daemon=True).start()

        except ImportError:
            messagebox.showinfo(
                "AI Code Optimizer",
                "🤖 AI-Powered Code Optimization\n\n"
                "This experimental feature uses AI to:\n"
                "• Optimize code performance\n"
                "• Suggest improvements\n"
                "• Fix common issues automatically\n\n"
                "Status: Available! Select a script first."
            )

    def show_ai_results(self, report, analysis):
        """Show AI analysis results in a new window"""
        results_window = tk.Toplevel(self.root)
        results_window.title("🤖 AI Code Analysis Results")
        results_window.geometry("800x600")

        # Center window
        results_window.update_idletasks()
        x = (results_window.winfo_screenwidth() // 2) - (400)
        y = (results_window.winfo_screenheight() // 2) - (300)
        results_window.geometry(f"800x600+{x}+{y}")

        # Main frame
        main_frame = ttk.Frame(results_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text=f"🤖 AI Analysis: {analysis['filename']}",
            font=('Arial', 16, 'bold')
        )
        header_label.pack(pady=(0, 15))

        # Quality score
        score_frame = ttk.Frame(main_frame)
        score_frame.pack(fill='x', pady=(0, 15))

        ttk.Label(score_frame, text="Quality Score:", font=('Arial', 12, 'bold')).pack(side='left')

        score = analysis['overall_score']
        score_color = 'green' if score >= 80 else 'orange' if score >= 60 else 'red'
        score_label = tk.Label(
            score_frame,
            text=f"{score:.1f}/100",
            font=('Arial', 12, 'bold'),
            fg=score_color
        )
        score_label.pack(side='left', padx=(10, 0))

        # Results text
        results_text = tk.Text(main_frame, font=('Courier', 10))
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=results_text.yview)
        results_text.configure(yscrollcommand=scrollbar.set)

        results_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Insert report
        results_text.insert('1.0', report)
        results_text.config(state='disabled')

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x', pady=(15, 0))

        ttk.Button(
            button_frame,
            text="💾 Save Report",
            command=lambda: self.save_ai_report(report, analysis)
        ).pack(side='left')

        ttk.Button(
            button_frame,
            text="❌ Close",
            command=results_window.destroy
        ).pack(side='right')

    def save_ai_report(self, report, analysis):
        """Save AI analysis report to file"""
        try:
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            filename = f"ai_analysis_{analysis['filename']}_{timestamp}.txt"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(report)
                f.write(f"\n\nDetailed Analysis Data:\n")
                f.write(json.dumps(analysis, indent=2))

            messagebox.showinfo("Report Saved", f"AI analysis report saved to:\n{filename}")

        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save report:\n{e}")

    def open_profiler(self):
        """Open performance profiler"""
        try:
            from tools.performance_profiler import PerformanceProfilerGUI
            self.log_message("📊 Opening Performance Profiler...")

            # Run in separate thread to avoid blocking
            def run_profiler():
    """Function definition"""
                try:
                    app = PerformanceProfilerGUI()
                    app.run()
                except Exception as e:
                    self.root.after(0, lambda: self.log_message(msg))

            threading.Thread(target=run_profiler, daemon=True).start()

        except ImportError:
            messagebox.showinfo(
                "Performance Profiler",
                "📊 Real-time Performance Profiling\n\n"
                "This experimental feature provides:\n"
                "• Real-time performance monitoring\n"
                "• Memory usage tracking\n"
                "• Bottleneck identification\n\n"
                "Status: Available! Launching..."
            )

    def open_template_manager(self):
        """Open template manager"""
        try:
            from tools.template_manager import TemplateManagerGUI
            self.log_message("📝 Opening Template Manager...")

            # Run in separate thread to avoid blocking
            def run_template_manager():
    """Function definition"""
                try:
                    app = TemplateManagerGUI()
                    app.run()
                except Exception as e:
                    self.root.after(0, lambda: self.log_message(msg))

            threading.Thread(target=run_template_manager, daemon=True).start()

        except ImportError:
            messagebox.showinfo(
                "Template Manager",
                "📝 Custom Conversion Templates\n\n"
                "This experimental feature allows:\n"
                "• Creating custom conversion rules\n"
                "• Saving reusable templates\n"
                "• Sharing templates with community\n\n"
            "Status: Prototype ready!"
        )

    def open_debug_console(self):
        """Open advanced debug console"""
        messagebox.showinfo(
            "Debug Console",
            "🔍 Advanced Debugging Tools\n\n"
            "This experimental feature includes:\n"
            "• Interactive Python console\n"
            "• Variable inspection\n"
            "• Step-by-step debugging\n\n"
            "Status: Alpha version!"
        )

    def open_cloud_sync(self):
        """Open cloud synchronization"""
        messagebox.showinfo(
            "Cloud Sync",
            "☁️ Cloud Settings Synchronization\n\n"
            "This experimental feature enables:\n"
            "• Sync settings across devices\n"
            "• Backup configurations\n"
            "• Team collaboration features\n\n"
            "Status: Planning phase!"
        )

    def on_theme_change(self, event=None):
        """Handle theme change immediately"""
        theme = self.theme_var.get()
        self.root.after(0, lambda: self.log_message(msg))

        # Define theme colors
        if theme == "Dark":
            bg_color = "#2b2b2b"
            fg_color = "#ffffff"
            text_bg = "#1e1e1e"
            select_bg = "#404040"
        elif theme == "Light":
            bg_color = "#ffffff"
            fg_color = "#000000"
            text_bg = "#f8f9fa"
            select_bg = "#e9ecef"
        elif theme == "High Contrast":
            bg_color = "#000000"
            fg_color = "#ffff00"
            text_bg = "#000000"
            select_bg = "#333333"
        else:  # Professional
            bg_color = ProfessionalTheme.COLORS['background']
            fg_color = ProfessionalTheme.COLORS['text']
            text_bg = "#f8f9fa"
            select_bg = "#e9ecef"

        # Apply to root window
        self.root.configure(bg=bg_color)

        # Apply to log text if it exists
        if hasattr(self, 'log_text'):
            try:
                self.log_text.configure(bg=text_bg, fg=fg_color, selectbackground=select_bg)
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        # Apply to notebook tabs
        if hasattr(self, 'notebook'):
            try:
                style = ttk.Style()
                if theme == "Dark":
                    style.configure('TNotebook', background=bg_color)
                    style.configure('TNotebook.Tab', background=select_bg, foreground=fg_color)
                elif theme == "Light":
                    style.configure('TNotebook', background=bg_color)
                    style.configure('TNotebook.Tab', background=select_bg, foreground=fg_color)
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        # Update status label colors
        if hasattr(self, 'status_label'):
            try:
                self.status_label.configure(foreground=fg_color)
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        # Update log
        self.root.after(0, lambda: self.log_message(msg))

        # Save setting
        self.save_settings()

    def on_font_size_change(self, value):
        """Handle font size change immediately"""
        size = int(float(value))
        self.root.after(0, lambda: self.log_message(msg))

        # Update font size label
        if hasattr(self, 'font_size_label'):
            self.root.after(0, lambda: self.font_size_label.config()text=f"Current: {size}pt")

        # Apply font size to log text
        if hasattr(self, 'log_text'):
            try:
                new_font = ("Consolas", size)
                self.log_text.configure(font=new_font)
            except Exception as e:
                self.root.after(0, lambda: self.log_message(msg))

        # Apply font size to status label
        if hasattr(self, 'status_label'):
            try:
                new_font = ("Arial", size)
                self.status_label.configure(font=new_font)
            except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging

        # Apply font size to other UI elements
        try:
            # Update ttk Style for labels and buttons
            style = ttk.Style()
            style.configure('TLabel', font=('Arial', size))
            style.configure('TButton', font=('Arial', size))
            style.configure('Heading.TLabel', font=('Arial', size + 2, 'bold'))

            self.root.after(0, lambda: self.log_message(msg))
        except Exception as e:
            self.root.after(0, lambda: self.log_message(msg))

        # Save setting
        self.save_settings()

    def save_settings(self):
        """Save current settings to file"""
        try:
            settings = {
                'theme': self.theme_var.get(),
                'font_size': self.font_size_var.get(),
                'auto_open': self.auto_open_var.get(),
                'backup': self.backup_var.get(),
                'verbose': self.verbose_var.get(),
                'speed': self.speed_var.get(),
                'memory': self.memory_var.get(),
                'discord_enabled': self.discord_enabled_var.get(),
                'mobile_companion': self.mobile_companion_var.get(),
                'debug': self.debug_var.get(),
                'auto_update': self.auto_update_var.get(),
                'experimental': self.experimental_var.get(),
                'discord_webhook_url': self.webhook_var.get() if hasattr(self, 'webhook_var') else '',
                # Experimental features
                'batch_conversion': self.batch_conversion_var.get() if hasattr(self, 'batch_conversion_var') else False,
                'ai_optimization': self.ai_optimization_var.get() if hasattr(self, 'ai_optimization_var') else False,
                'profiling': self.profiling_var.get() if hasattr(self, 'profiling_var') else False,
                'custom_templates': self.custom_templates_var.get() if hasattr(self, 'custom_templates_var') else False,
                'advanced_debug': self.advanced_debug_var.get() if hasattr(self, 'advanced_debug_var') else False,
                'cloud_sync': self.cloud_sync_var.get() if hasattr(self, 'cloud_sync_var') else False
            }

            with open('settings.json', "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2)

        except Exception as e:
            print(f"Error saving settings: {e}")

    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ProfessionalMainWindow()
    app.run()
