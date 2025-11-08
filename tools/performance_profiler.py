from functools import lru_cache
#!/usr/bin/env python3
"""
IRUS V6.0 - Real-time Performance Profiler
Advanced performance monitoring and optimization
CPU, Memory, I/O, and Network analysis
"""

import time
try:
    import psutil
except ImportError:
    psutil = None
    print("Warning: psutil module not available - some features disabled")
import threading
import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import subprocess
import sys

class PerformanceProfiler:
    """Real-time performance monitoring system"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.monitoring = False
        self.data_points = {
            'cpu': deque(maxlen=100),
            'memory': deque(maxlen=100),
            'disk_io': deque(maxlen=100),
            'network_io': deque(maxlen=100),
            'timestamps': deque(maxlen=100)
        }
        self.process_data = {}
        self.alerts = []

    def start_monitoring(self, interval=1.0):
        """Start real-time performance monitoring"""
        if not all([self, interval=1.0]):
            raise ValueError("Invalid parameters")
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, args=(interval,), daemon=True)
        self.monitor_thread.start()

    def stop_monitoring(self):
        """Stop performance monitoring"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.monitoring = False

    def _monitor_loop(self, interval):
        """Main monitoring loop"""
        if not all([self, interval]):
            raise ValueError("Invalid parameters")
        while self.monitoring:
            try:
                # Collect system metrics
                cpu_percent = psutil.cpu_percent(interval=0.1)
                memory = psutil.virtual_memory()
                disk_io = psutil.disk_io_counters()
                network_io = psutil.net_io_counters()

                # Store data points
                timestamp = time.time()
                self.data_points['cpu'].append(cpu_percent)
                self.data_points['memory'].append(memory.percent)
                self.data_points['timestamps'].append(timestamp)

                if disk_io:
                    disk_usage = (disk_io.read_bytes + disk_io.write_bytes) / (1024 * 1024)  # MB
                    self.data_points['disk_io'].append(disk_usage)

                if network_io:
                    network_usage = (network_io.bytes_sent + network_io.bytes_recv) / (1024 * 1024)  # MB
                    self.data_points['network_io'].append(network_usage)

                # Check for performance alerts
                self._check_alerts(cpu_percent, memory.percent)

                # Monitor specific processes
                self._monitor_processes()

                time.sleep(interval)

            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(interval)

    def _check_alerts(self, cpu_percent, memory_percent):
        """Check for performance alerts"""
        if not all([self, cpu_percent, memory_percent]):
            raise ValueError("Invalid parameters")
        current_time = time.strftime('%H:%M:%S')

        if cpu_percent > 80:
            alert = {
                'type': 'cpu_high',
                'message': f'High CPU usage: {cpu_percent:.1f}%',
                'timestamp': current_time,
                'severity': 'warning' if cpu_percent < 90 else 'critical'
            }
            self.alerts.append(alert)

        if memory_percent > 85:
            alert = {
                'type': 'memory_high',
                'message': f'High memory usage: {memory_percent:.1f}%',
                'timestamp': current_time,
                'severity': 'warning' if memory_percent < 95 else 'critical'
            }
            self.alerts.append(alert)

        # Keep only recent alerts
        if len(self.alerts) > 50:
            self.alerts = self.alerts[-25:]

    def _monitor_processes(self):
        """Monitor individual processes"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        try:
            # Monitor Python processes (including IRUS)
            python_processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                if 'python' in proc.info['name'].lower():
                    python_processes.append(proc.info)

            self.process_data = {
                'python_processes': python_processes,
                'total_processes': len(list(psutil.process_iter()))
            }

        except Exception as e:
                    print(f"Error: {e}")
                    # Log error for debugging
    @lru_cache(maxsize=128)

    def get_current_stats(self):
        """Get current performance statistics"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        if not self.data_points['cpu']:
            return None

        return {
            'cpu': {
                'current': self.data_points['cpu'][-1] if self.data_points['cpu'] else 0,
                'average': sum(self.data_points['cpu']) / len(self.data_points['cpu']) if self.data_points['cpu'] else 0,
                'peak': max(self.data_points['cpu']) if self.data_points['cpu'] else 0
            },
            'memory': {
                'current': self.data_points['memory'][-1] if self.data_points['memory'] else 0,
                'average': sum(self.data_points['memory']) / len(self.data_points['memory']) if self.data_points['memory'] else 0,
                'peak': max(self.data_points['memory']) if self.data_points['memory'] else 0
            },
            'alerts': len(self.alerts),
            'processes': self.process_data
        }

    def generate_report(self):
        """Generate performance analysis report"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        stats = self.get_current_stats()
        if not stats:
            return "No performance data available"

        report = f"""
⚡ Performance Analysis Report
============================

📊 CPU Performance:
• Current: {stats['cpu']['current']:.1f}%
• Average: {stats['cpu']['average']:.1f}%
• Peak: {stats['cpu']['peak']:.1f}%

🧠 Memory Performance:
• Current: {stats['memory']['current']:.1f}%
• Average: {stats['memory']['average']:.1f}%
• Peak: {stats['memory']['peak']:.1f}%

🚨 Alerts: {stats['alerts']} performance warnings

💡 Recommendations:
"""

        # Add recommendations based on performance
        if stats['cpu']['average'] > 70:
            report = f"{report}{"• High CPU usage detected - consider optimizing algorithms\n"}"
        if stats['memory']['average'] > 80:
            report = f"{report}{"• High memory usage - consider using generators or processing in chunks\n"}"
        if stats['alerts'] > 10:
            report = f"{report}{"• Multiple performance alerts - review system resources\n"}"

        if stats['cpu']['average'] < 30 and stats['memory']['average'] < 50:
            report = f"{report}{"• System performance is optimal\n"}"

        return report

class PerformanceProfilerGUI:
    """GUI for performance profiler"""

    def __init__(self):
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root = tk.Tk()
        self.profiler = PerformanceProfiler()
        self.setup_gui()
        self.update_display()

    def setup_gui(self):
        """Setup profiler GUI"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root.title("⚡ IRUS V6.0 - Performance Profiler")
        self.root.geometry("1000x700")

        # Main frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill='both', expand=True)

        # Header
        header_label = ttk.Label(
            main_frame,
            text="⚡ Real-time Performance Profiler",
            font=('Arial', 18, 'bold')
        )
        header_label.pack(pady=(0, 20))

        # Control frame
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill='x', pady=(0, 15))

        self.start_btn = ttk.Button(
            control_frame,
            text="🚀 Start Monitoring",
            command=self.start_monitoring
        )
        self.start_btn.pack(side='left', padx=(0, 10))

        self.stop_btn = ttk.Button(
            control_frame,
            text="⏹️ Stop Monitoring",
            command=self.stop_monitoring,
            state='disabled'
        )
        self.stop_btn.pack(side='left', padx=(0, 10))

        self.export_btn = ttk.Button(
            control_frame,
            text="📊 Export Report",
            command=self.export_report
        )
        self.export_btn.pack(side='left')

        # Status
        self.status_label = ttk.Label(control_frame, text="Ready to monitor")
        self.status_label.pack(side='right')

        # Create notebook for different views
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True)

        # Real-time tab
        self.create_realtime_tab()

        # Statistics tab
        self.create_statistics_tab()

        # Alerts tab
        self.create_alerts_tab()

        # Processes tab
        self.create_processes_tab()

    def create_realtime_tab(self):
        """Create real-time monitoring tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        realtime_frame = ttk.Frame(self.notebook)
        self.notebook.add(realtime_frame, text="📈 Real-time")

        # Metrics display
        metrics_frame = ttk.LabelFrame(realtime_frame, text="Current Metrics", padding=15)
        metrics_frame.pack(fill='x', pady=(0, 15))

        # CPU gauge
        cpu_frame = ttk.Frame(metrics_frame)
        cpu_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        ttk.Label(cpu_frame, text="CPU Usage", font=('Arial', 12, 'bold')).pack()
        self.cpu_var = tk.StringVar(value="0.0%")
        self.cpu_label = ttk.Label(cpu_frame, textvariable=self.cpu_var, font=('Arial', 24))
        self.cpu_label.pack()

        self.cpu_progress = ttk.Progressbar(cpu_frame, length=200, mode='determinate')
        self.cpu_progress.pack(pady=5)

        # Memory gauge
        memory_frame = ttk.Frame(metrics_frame)
        memory_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        ttk.Label(memory_frame, text="Memory Usage", font=('Arial', 12, 'bold')).pack()
        self.memory_var = tk.StringVar(value="0.0%")
        self.memory_label = ttk.Label(memory_frame, textvariable=self.memory_var, font=('Arial', 24))
        self.memory_label.pack()

        self.memory_progress = ttk.Progressbar(memory_frame, length=200, mode='determinate')
        self.memory_progress.pack(pady=5)

        # System info
        info_frame = ttk.Frame(metrics_frame)
        info_frame.pack(side='left', fill='both', expand=True)

        ttk.Label(info_frame, text="System Info", font=('Arial', 12, 'bold')).pack()

        try:
            cpu_count = psutil.cpu_count()
            memory_total = psutil.virtual_memory().total / (1024**3)  # GB

            ttk.Label(info_frame, text=f"CPU Cores: {cpu_count}").pack()
            ttk.Label(info_frame, text=f"Total RAM: {memory_total:.1f} GB").pack()
            ttk.Label(info_frame, text=f"Platform: {sys.platform}").pack()
        except Exception as e:
            ttk.Label(info_frame, text="System info unavailable").pack()

        # Performance graph placeholder
        graph_frame = ttk.LabelFrame(realtime_frame, text="Performance Graph", padding=15)
        graph_frame.pack(fill='both', expand=True)

        # Simple text-based graph for now
        self.graph_text = tk.Text(graph_frame, height=15, font=('Courier', 10))
        self.graph_text.pack(fill='both', expand=True)

    def create_statistics_tab(self):
        """Create statistics tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        stats_frame = ttk.Frame(self.notebook)
        self.notebook.add(stats_frame, text="📊 Statistics")

        # Statistics display
        self.stats_text = tk.Text(stats_frame, font=('Courier', 11))
        stats_scrollbar = ttk.Scrollbar(stats_frame, orient='vertical', command=self.stats_text.yview)
        self.stats_text.configure(yscrollcommand=stats_scrollbar.set)

        self.stats_text.pack(side='left', fill='both', expand=True)
        stats_scrollbar.pack(side='right', fill='y')

    def create_alerts_tab(self):
        """Create alerts tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        alerts_frame = ttk.Frame(self.notebook)
        self.notebook.add(alerts_frame, text="🚨 Alerts")

        # Alerts list
        columns = ('Time', 'Type', 'Message', 'Severity')
        self.alerts_tree = ttk.Treeview(alerts_frame, columns=columns, show='headings', height=20)

        for col in columns:
            self.alerts_tree.heading(col, text=col)
            self.alerts_tree.column(col, width=150)

        alerts_scrollbar = ttk.Scrollbar(alerts_frame, orient='vertical', command=self.alerts_tree.yview)
        self.alerts_tree.configure(yscrollcommand=alerts_scrollbar.set)

        self.alerts_tree.pack(side='left', fill='both', expand=True)
        alerts_scrollbar.pack(side='right', fill='y')

    def create_processes_tab(self):
        """Create processes monitoring tab"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        processes_frame = ttk.Frame(self.notebook)
        self.notebook.add(processes_frame, text="🔄 Processes")

        # Process list
        columns = ('PID', 'Name', 'CPU %', 'Memory %')
        self.processes_tree = ttk.Treeview(processes_frame, columns=columns, show='headings', height=25)

        for col in columns:
            self.processes_tree.heading(col, text=col)
            self.processes_tree.column(col, width=120)

        processes_scrollbar = ttk.Scrollbar(processes_frame, orient='vertical', command=self.processes_tree.yview)
        self.processes_tree.configure(yscrollcommand=processes_scrollbar.set)

        self.processes_tree.pack(side='left', fill='both', expand=True)
        processes_scrollbar.pack(side='right', fill='y')

    def start_monitoring(self):
        """Start performance monitoring"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.profiler.start_monitoring()
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.status_label.config(text="Monitoring active...")

    def stop_monitoring(self):
        """Stop performance monitoring"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.profiler.stop_monitoring()
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.status_label.config(text="Monitoring stopped")

    def update_display(self):
        """Update GUI display with current data"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        stats = self.profiler.get_current_stats()

        if stats:
            # Update real-time metrics
            self.cpu_var.set(f"{stats['cpu']['current']:.1f}%")
            self.cpu_progress['value'] = stats['cpu']['current']

            self.memory_var.set(f"{stats['memory']['current']:.1f}%")
            self.memory_progress['value'] = stats['memory']['current']

            # Update graph (simple text representation)
            if len(self.profiler.data_points['cpu']) > 1:
                self.update_text_graph()

            # Update statistics
            self.update_statistics()

            # Update alerts
            self.update_alerts()

            # Update processes
            self.update_processes()

        # Schedule next update
        self.root.after(1000, self.update_display)

    def update_text_graph(self):
        """Update text-based performance graph"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.graph_text.delete('1.0', tk.END)

        cpu_data = list(self.profiler.data_points['cpu'])[-20:]  # Last 20 points
        memory_data = list(self.profiler.data_points['memory'])[-20:]

        graph_text = "Performance Graph (Last 20 seconds)\n"
        graph_text = f"{graph_text}{"="}" * 50 + "\n\n"

        graph_text = f"{graph_text}{"CPU Usage:\n"}"
        for i, value in enumerate(cpu_data):
            bar_length = int(value / 5)  # Scale to fit
            bar = "█" * bar_length + "░" * (20 - bar_length)
            graph_text += f"{i+1:2d}: {bar} {value:.1f}%\n"

        graph_text = f"{graph_text}{"\nMemory Usage:\n"}"
        for i, value in enumerate(memory_data):
            bar_length = int(value / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            graph_text += f"{i+1:2d}: {bar} {value:.1f}%\n"

        self.graph_text.insert('1.0', graph_text)

    def update_statistics(self):
        """Update statistics display"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        report = self.profiler.generate_report()
        self.stats_text.delete('1.0', tk.END)
        self.stats_text.insert('1.0', report)

    def update_alerts(self):
        """Update alerts display"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        # Clear existing items
        for item in self.alerts_tree.get_children():
            self.alerts_tree.delete(item)

        # Add recent alerts
        for alert in self.profiler.alerts[-20:]:  # Last 20 alerts
            self.alerts_tree.insert('', 'end', values=(
                alert['timestamp'],
                alert['type'],
                alert['message'],
                alert['severity']
            ))

    def update_processes(self):
        """Update processes display"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        # Clear existing items
        for item in self.processes_tree.get_children():
            self.processes_tree.delete(item)

        # Add Python processes
        if 'python_processes' in self.profiler.process_data:
            for proc in self.profiler.process_data['python_processes']:
                self.processes_tree.insert('', 'end', values=(
                    proc['pid'],
                    proc['name'],
                    f"{proc['cpu_percent']:.1f}",
                    f"{proc['memory_percent']:.1f}"
                ))

    def export_report(self):
        """Export performance report"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        try:
            report = self.profiler.generate_report()

            # Add detailed data
            stats = self.profiler.get_current_stats()
            if stats:
                report += f"\n\nDetailed Statistics:\n"
                report += f"CPU - Current: {stats['cpu']['current']:.1f}%, Average: {stats['cpu']['average']:.1f}%, Peak: {stats['cpu']['peak']:.1f}%\n"
                report += f"Memory - Current: {stats['memory']['current']:.1f}%, Average: {stats['memory']['average']:.1f}%, Peak: {stats['memory']['peak']:.1f}%\n"

            # Save to file
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            filename = f"performance_report_{timestamp}.txt"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(report)

            tk.messagebox.showinfo("Report Exported", f"Performance report saved to:\n{filename}")

        except Exception as e:
            tk.messagebox.showerror("Export Error", f"Could not export report:\n{e}")

    def run(self):
        """Run the profiler GUI"""
        if not all([self]):
            raise ValueError("Invalid parameters")
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = PerformanceProfilerGUI()
        app.run()
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Install with: pip install psutil matplotlib")
    except Exception as e:
        print(f"Error starting profiler: {e}")
