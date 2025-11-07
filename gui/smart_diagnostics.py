#!/usr/bin/env python3
"""
IRUS V4 - Smart Diagnostics System
Advanced system analysis and predictive issue detection
"""

import sys
import os
import platform
import subprocess
import psutil
import time
import json
from pathlib import Path

class SmartDiagnostics:
    def __init__(self):
        self.system_info = {}
        self.issues_found = []
        self.recommendations = []
        self.compatibility_score = 0
        
    def run_comprehensive_analysis(self):
        """Run complete system analysis"""
        print("🔍 Running comprehensive system analysis...")
        
        # Basic system info
        self.analyze_system_specs()
        
        # Performance analysis
        self.analyze_performance()
        
        # Network analysis
        self.analyze_network()
        
        # Python environment analysis
        self.analyze_python_environment()
        
        # macOS specific analysis
        self.analyze_macos_features()
        
        # Predictive issue detection
        self.predict_potential_issues()
        
        # Calculate compatibility score
        self.calculate_compatibility_score()
        
        return self.generate_report()
    
    def analyze_system_specs(self):
        """Analyze hardware specifications"""
        try:
            # CPU info
            cpu_count = psutil.cpu_count(logical=True)
            cpu_freq = psutil.cpu_freq()
            
            # Memory info
            memory = psutil.virtual_memory()
            
            # Disk info
            disk = psutil.disk_usage('/')
            
            # macOS version
            mac_version = platform.mac_ver()[0]
            
            self.system_info.update({
                'cpu_cores': cpu_count,
                'cpu_frequency': cpu_freq.current if cpu_freq else 0,
                'total_memory_gb': round(memory.total / (1024**3), 2),
                'available_memory_gb': round(memory.available / (1024**3), 2),
                'memory_percent_used': memory.percent,
                'disk_total_gb': round(disk.total / (1024**3), 2),
                'disk_free_gb': round(disk.free / (1024**3), 2),
                'disk_percent_used': round((disk.used / disk.total) * 100, 1),
                'macos_version': mac_version,
                'architecture': platform.machine()
            })
            
            # Check for potential issues
            if memory.percent > 80:
                self.issues_found.append({
                    'type': 'warning',
                    'title': 'High Memory Usage',
                    'description': f'Memory usage is {memory.percent}% - may cause installation issues',
                    'solution': 'Close unnecessary applications before running the wizard'
                })
            
            if disk.free < 2 * (1024**3):  # Less than 2GB free
                self.issues_found.append({
                    'type': 'error',
                    'title': 'Low Disk Space',
                    'description': f'Only {round(disk.free / (1024**3), 1)}GB free space available',
                    'solution': 'Free up at least 2GB of disk space before proceeding'
                })
                
        except Exception as e:
            self.issues_found.append({
                'type': 'warning',
                'title': 'System Analysis Failed',
                'description': f'Could not analyze system specs: {e}',
                'solution': 'Manual verification may be needed'
            })
    
    def analyze_performance(self):
        """Analyze system performance"""
        try:
            # CPU usage over 5 seconds
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Load average (Unix only)
            if hasattr(os, 'getloadavg'):
                load_avg = os.getloadavg()[0]
            else:
                load_avg = 0
            
            self.system_info.update({
                'cpu_usage_percent': cpu_percent,
                'load_average': load_avg
            })
            
            # Performance warnings
            if cpu_percent > 80:
                self.issues_found.append({
                    'type': 'warning',
                    'title': 'High CPU Usage',
                    'description': f'CPU usage is {cpu_percent}% - installation may be slow',
                    'solution': 'Wait for CPU usage to decrease or close resource-intensive apps'
                })
                
        except Exception as e:
            print(f"Performance analysis failed: {e}")
    
    def analyze_network(self):
        """Analyze network connectivity"""
        try:
            # Test internet connectivity
            start_time = time.time()
            result = subprocess.run(['ping', '-c', '1', 'google.com'], 
                                  capture_output=True, timeout=10)
            ping_time = (time.time() - start_time) * 1000
            
            network_ok = result.returncode == 0
            
            self.system_info.update({
                'network_available': network_ok,
                'ping_time_ms': round(ping_time, 1) if network_ok else None
            })
            
            if not network_ok:
                self.issues_found.append({
                    'type': 'error',
                    'title': 'No Internet Connection',
                    'description': 'Cannot reach the internet - package installation will fail',
                    'solution': 'Connect to the internet and try again'
                })
            elif ping_time > 5000:  # 5 seconds
                self.issues_found.append({
                    'type': 'warning',
                    'title': 'Slow Internet Connection',
                    'description': f'Ping time is {round(ping_time/1000, 1)} seconds',
                    'solution': 'Package installation may take longer than usual'
                })
                
        except Exception as e:
            self.issues_found.append({
                'type': 'warning',
                'title': 'Network Test Failed',
                'description': f'Could not test network: {e}',
                'solution': 'Verify internet connection manually'
            })
    
    def analyze_python_environment(self):
        """Analyze Python environment"""
        try:
            # Python version
            python_version = sys.version_info
            
            # pip version
            pip_result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                                      capture_output=True, text=True)
            pip_version = pip_result.stdout.strip() if pip_result.returncode == 0 else 'Unknown'
            
            # Check for virtual environment
            in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
            
            # Check installed packages
            installed_packages = self.get_installed_packages()
            
            self.system_info.update({
                'python_version': f"{python_version.major}.{python_version.minor}.{python_version.micro}",
                'pip_version': pip_version,
                'in_virtual_env': in_venv,
                'python_executable': sys.executable,
                'installed_packages': installed_packages
            })
            
            # Check for issues
            if python_version < (3, 8):
                self.issues_found.append({
                    'type': 'error',
                    'title': 'Python Version Too Old',
                    'description': f'Python {python_version.major}.{python_version.minor} detected, need 3.8+',
                    'solution': 'Install Python 3.11: brew install python@3.11'
                })
            
            if 'pip' not in pip_version.lower():
                self.issues_found.append({
                    'type': 'error',
                    'title': 'pip Not Available',
                    'description': 'pip package manager not found',
                    'solution': 'Install pip: python3 -m ensurepip --upgrade'
                })
                
        except Exception as e:
            self.issues_found.append({
                'type': 'warning',
                'title': 'Python Analysis Failed',
                'description': f'Could not analyze Python environment: {e}',
                'solution': 'Manual Python verification needed'
            })
    
    def analyze_macos_features(self):
        """Analyze macOS specific features"""
        try:
            # macOS version compatibility
            mac_version = platform.mac_ver()[0]
            version_parts = [int(x) for x in mac_version.split('.')]
            
            # Check for Apple Silicon
            is_apple_silicon = platform.machine() == 'arm64'
            
            # Check for Rosetta (if Apple Silicon)
            rosetta_available = False
            if is_apple_silicon:
                rosetta_result = subprocess.run(['arch', '-x86_64', 'uname', '-m'], 
                                              capture_output=True)
                rosetta_available = rosetta_result.returncode == 0
            
            # Check Xcode Command Line Tools
            xcode_result = subprocess.run(['xcode-select', '-p'], capture_output=True)
            xcode_installed = xcode_result.returncode == 0
            
            self.system_info.update({
                'macos_version_parts': version_parts,
                'is_apple_silicon': is_apple_silicon,
                'rosetta_available': rosetta_available,
                'xcode_tools_installed': xcode_installed
            })
            
            # Version compatibility
            if version_parts[0] < 10 or (version_parts[0] == 10 and version_parts[1] < 15):
                self.issues_found.append({
                    'type': 'error',
                    'title': 'macOS Version Too Old',
                    'description': f'macOS {mac_version} detected, need 10.15+',
                    'solution': 'Upgrade macOS or use an older Python version'
                })
            
            # Xcode tools check
            if not xcode_installed:
                self.recommendations.append({
                    'type': 'suggestion',
                    'title': 'Install Xcode Command Line Tools',
                    'description': 'Recommended for PyObjC installation',
                    'command': 'xcode-select --install'
                })
                
        except Exception as e:
            print(f"macOS analysis failed: {e}")
    
    def predict_potential_issues(self):
        """Predict potential issues based on system analysis"""
        
        # Memory-based predictions
        if self.system_info.get('total_memory_gb', 0) < 4:
            self.recommendations.append({
                'type': 'warning',
                'title': 'Low Memory System',
                'description': 'System has less than 4GB RAM - installation may be slow',
                'suggestion': 'Close all unnecessary applications during installation'
            })
        
        # Disk space predictions
        if self.system_info.get('disk_free_gb', 0) < 5:
            self.recommendations.append({
                'type': 'warning',
                'title': 'Limited Disk Space',
                'description': 'Less than 5GB free space available',
                'suggestion': 'Free up more space to avoid installation issues'
            })
        
        # Network predictions
        if self.system_info.get('ping_time_ms', 0) > 1000:
            self.recommendations.append({
                'type': 'info',
                'title': 'Slow Network Detected',
                'description': 'Package downloads may take longer than usual',
                'suggestion': 'Be patient during package installation phase'
            })
        
        # Apple Silicon specific
        if self.system_info.get('is_apple_silicon', False):
            self.recommendations.append({
                'type': 'info',
                'title': 'Apple Silicon Detected',
                'description': 'Using native ARM64 Python is recommended',
                'suggestion': 'Ensure you\'re using native Python, not Rosetta'
            })
    
    def get_installed_packages(self):
        """Get list of installed Python packages"""
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')[2:]  # Skip header
                packages = {}
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        if len(parts) >= 2:
                            packages[parts[0]] = parts[1]
                return packages
        except:
            pass
        return {}
    
    def calculate_compatibility_score(self):
        """Calculate overall compatibility score (0-100)"""
        score = 100
        
        # Deduct points for errors
        for issue in self.issues_found:
            if issue['type'] == 'error':
                score -= 25
            elif issue['type'] == 'warning':
                score -= 10
        
        # Bonus points for good conditions
        if self.system_info.get('total_memory_gb', 0) >= 8:
            score += 5
        
        if self.system_info.get('disk_free_gb', 0) >= 10:
            score += 5
        
        if self.system_info.get('xcode_tools_installed', False):
            score += 10
        
        self.compatibility_score = max(0, min(100, score))
    
    def generate_report(self):
        """Generate comprehensive diagnostic report"""
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'compatibility_score': self.compatibility_score,
            'system_info': self.system_info,
            'issues_found': self.issues_found,
            'recommendations': self.recommendations,
            'summary': self.generate_summary()
        }
        
        return report
    
    def generate_summary(self):
        """Generate human-readable summary"""
        if self.compatibility_score >= 90:
            status = "Excellent"
            message = "Your system is perfectly configured for the macro conversion!"
        elif self.compatibility_score >= 75:
            status = "Good"
            message = "Your system should work well with minor optimizations."
        elif self.compatibility_score >= 50:
            status = "Fair"
            message = "Your system will work but may need some fixes first."
        else:
            status = "Poor"
            message = "Several issues need to be resolved before proceeding."
        
        return {
            'status': status,
            'message': message,
            'error_count': len([i for i in self.issues_found if i['type'] == 'error']),
            'warning_count': len([i for i in self.issues_found if i['type'] == 'warning']),
            'recommendation_count': len(self.recommendations)
        }

def run_smart_diagnostics():
    """Run smart diagnostics and return report"""
    diagnostics = SmartDiagnostics()
    return diagnostics.run_comprehensive_analysis()

if __name__ == "__main__":
    report = run_smart_diagnostics()
    print(json.dumps(report, indent=2))
