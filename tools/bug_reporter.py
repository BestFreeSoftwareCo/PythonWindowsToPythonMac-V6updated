#!/usr/bin/env python3
"""
IRUS V4.5 - Bug Reporter System
Automated bug reporting to Discord server with system diagnostics
"""

import sys
import os
import platform
import json
import subprocess
import time
from pathlib import Path
import traceback

class BugReporter:
    def __init__(self):
        self.system_info = {}
        self.error_details = {}
        self.log_files = []
        self.discord_webhook = None  # Will be set by user
        
    def collect_system_info(self):
        """Collect comprehensive system information"""
        
        try:
            # Basic system info
            self.system_info = {
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'os': platform.system(),
                'os_version': platform.platform(),
                'architecture': platform.machine(),
                'python_version': sys.version,
                'python_executable': sys.executable,
            }
            
            # macOS specific info
            if platform.system() == 'Darwin':
                try:
                    # macOS version
                    result = subprocess.run(['sw_vers'], capture_output=True, text=True)
                    self.system_info['macos_details'] = result.stdout.strip()
                    
                    # Xcode tools
                    result = subprocess.run(['xcode-select', '-p'], capture_output=True)
                    self.system_info['xcode_tools'] = result.returncode == 0
                    
                    # Homebrew
                    result = subprocess.run(['brew', '--version'], capture_output=True)
                    self.system_info['homebrew_available'] = result.returncode == 0
                    
                except Exception as e:
                    pass
            
            # Python packages
            try:
                result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    self.system_info['installed_packages'] = result.stdout
            except Exception as e:
                pass
            
            # Memory and disk info
            try:
                import psutil
                memory = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                
                self.system_info.update({
                    'memory_total_gb': round(memory.total / (1024**3), 2),
                    'memory_available_gb': round(memory.available / (1024**3), 2),
                    'memory_percent_used': memory.percent,
                    'disk_total_gb': round(disk.total / (1024**3), 2),
                    'disk_free_gb': round(disk.free / (1024**3), 2),
                    'cpu_count': psutil.cpu_count()
                })
            except ImportError:
                pass
                
        except Exception as e:
            self.system_info['collection_error'] = str(e)
    
    def collect_error_details(self, error_type, error_message, error_traceback=None):
        """Collect specific error information"""
        
        self.error_details = {
            'error_type': error_type,
            'error_message': error_message,
            'error_traceback': error_traceback or traceback.format_exc(),
            'error_timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def collect_log_files(self):
        """Collect relevant log files"""
        
        log_locations = [
            'Debug.txt',
            'output/Debug.txt',
            'conversion_report.txt',
            'output/conversion_report.txt'
        ]
        
        for log_path in log_locations:
            if os.path.exists(log_path):
                try:
                    with open(log_path, 'r', encoding='utf-8') as f:
                        # Get last 50 lines to avoid huge reports
                        lines = f.readlines()
                        recent_lines = lines[-50:] if len(lines) > 50 else lines
                        
                        self.log_files.append({
                            'filename': log_path,
                            'content': ''.join(recent_lines),
                            'total_lines': len(lines)
                        })
                except Exception as e:
                    self.log_files.append({
                        'filename': log_path,
                        'error': f'Could not read file: {e}'
                    })
    
    def generate_bug_report(self, user_description="", contact_info=""):
        """Generate comprehensive bug report"""
        
        self.collect_system_info()
        self.collect_log_files()
        
        report = {
            'report_id': f"IRUS-{int(time.time())}",
            'version': 'V4.5',
            'user_description': user_description,
            'contact_info': contact_info,
            'system_info': self.system_info,
            'error_details': self.error_details,
            'log_files': self.log_files,
            'generated_at': time.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        
        return report
    
    def format_discord_message(self, report):
        """Format bug report for Discord"""
        
        # Create a concise Discord message
        message = f"""🐛 **IRUS V4.5 Bug Report**
        
**Report ID:** `{report['report_id']}`
**Timestamp:** {report['generated_at']}

**System Info:**
• OS: {report['system_info'].get('os', 'Unknown')} {report['system_info'].get('architecture', '')}
• Python: {report['system_info'].get('python_version', 'Unknown').split()[0]}
• Memory: {report['system_info'].get('memory_available_gb', 'Unknown')}GB available

**Error Details:**
• Type: `{report['error_details'].get('error_type', 'General Issue')}`
• Message: `{report['error_details'].get('error_message', 'No specific error')}`

**User Description:**
{report['user_description'] or 'No description provided'}

**Contact:** {report['contact_info'] or 'No contact info provided'}
"""
        
        # Add log file info if available
        if report['log_files']:
            message += f"\n**Log Files:** {len(report['log_files'])} files collected"
        
        return message
    
    def save_report_locally(self, report):
        """Save bug report to local file"""
        
        reports_dir = Path('bug_reports')
        reports_dir.mkdir(exist_ok=True)
        
        report_file = reports_dir / f"{report['report_id']}.json"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, default=str)
            
            print(f"📄 Bug report saved: {report_file}")
            return str(report_file)
            
        except Exception as e:
            print(f"❌ Could not save report: {e}")
            return None
    
    def submit_to_discord(self, report, webhook_url=None):
        """Submit bug report to Discord (placeholder for webhook)"""
        
        if not webhook_url:
            print("⚠️ Discord webhook URL not configured")
            print("📋 Please manually share the bug report with the developer")
            return False
        
        try:
            import requests
            
            discord_message = self.format_discord_message(report)
            
            payload = {
                'content': discord_message,
                'username': 'IRUS Bug Reporter'
            }
            
            response = requests.post(webhook_url, json=payload)
            
            if response.status_code == 204:
                print("✅ Bug report submitted to Discord successfully!")
                return True
            else:
                print(f"❌ Discord submission failed: {response.status_code}")
                return False
                
        except ImportError:
            print("⚠️ 'requests' library not available for Discord submission")
            return False
        except Exception as e:
            print(f"❌ Error generating report: {e}")
            return None
    
    def create_interactive_report(self):
        """Create interactive bug report (GUI integration)"""
        try:
            # Collect system info
            self.collect_system_info()
            
            # For GUI integration, return the reporter instance
            # The GUI will handle the actual report creation
            return self
            
        except Exception as e:
            print(f"❌ Error creating interactive report: {e}")
            return None

def report_bug_interactive():
    """Interactive bug reporting"""
    
    print("🐛 IRUS V4.5 Bug Reporter")
    print("=" * 40)
    print()
    
    # Get user input
    print("Please describe the issue you encountered:")
    user_description = input("> ")
    print()
    
    print("Your contact info (optional - Discord username, email, etc.):")
    contact_info = input("> ")
    print()
    
    # Ask about error details
    print("Did you encounter a specific error? (y/n)")
    has_error = input("> ").lower().startswith('y')
    
    error_type = ""
    error_message = ""
    
    if has_error:
        print("What type of error? (e.g., ImportError, PermissionError, etc.)")
        error_type = input("> ")
        
        print("Error message (copy/paste if available):")
        error_message = input("> ")
    
    print("\n🔍 Collecting system information...")
    
    # Generate report
    reporter = BugReporter()
    
    if has_error:
        reporter.collect_error_details(error_type, error_message)
    
    report = reporter.generate_bug_report(user_description, contact_info)
    
    # Save locally
    report_file = reporter.save_report_locally(report)
    
    print(f"\n📊 Bug Report Generated:")
    print(f"• Report ID: {report['report_id']}")
    print(f"• System: {report['system_info'].get('os', 'Unknown')}")
    print(f"• Python: {report['system_info'].get('python_version', 'Unknown').split()[0]}")
    print(f"• Log files: {len(report['log_files'])} collected")
    
    # Instructions for manual submission
    print(f"\n📋 Next Steps:")
    print(f"1. Join the Discord server: [DISCORD_LINK_PLACEHOLDER]")
    print(f"2. Go to the #bug-reports channel")
    print(f"3. Share your Report ID: {report['report_id']}")
    print(f"4. Attach the report file: {report_file}")
    print(f"5. Describe your issue briefly")
    
    print(f"\n💡 The developer will help you resolve the issue quickly!")
    
    return report

def report_bug_automatic(error_type, error_message, user_description="Automatic error report"):
    """Automatic bug reporting for caught exceptions"""
    
    reporter = BugReporter()
    reporter.collect_error_details(error_type, error_message)
    
    report = reporter.generate_bug_report(user_description)
    report_file = reporter.save_report_locally(report)
    
    print(f"\n🐛 Automatic bug report generated: {report['report_id']}")
    print(f"📄 Report saved: {report_file}")
    print(f"📋 Please share this with the developer on Discord: [DISCORD_LINK_PLACEHOLDER]")
    
    return report

def setup_automatic_reporting():
    """Set up automatic exception handling"""
    
    def exception_handler(exc_type, exc_value, exc_traceback):
        """Handle uncaught exceptions"""
        
        if issubclass(exc_type, KeyboardInterrupt):
            # Don't report Ctrl+C
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        
        print(f"\n❌ Unexpected error occurred: {exc_type.__name__}")
        print(f"📝 Error: {exc_value}")
        
        # Generate automatic bug report
        report_bug_automatic(
            exc_type.__name__,
            str(exc_value),
            "Automatic report for uncaught exception"
        )
        
        # Still show the original traceback
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
    
    # Install the exception handler
    sys.excepthook = exception_handler
    print("🛡️ Automatic bug reporting enabled")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--setup":
        setup_automatic_reporting()
        print("✅ Automatic bug reporting is now active")
    else:
        report_bug_interactive()
