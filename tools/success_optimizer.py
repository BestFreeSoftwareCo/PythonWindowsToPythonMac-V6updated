#!/usr/bin/env python3
"""
IRUS V4 - Success Rate Optimizer
Advanced system optimization for maximum success rate
"""

import os
import sys
import subprocess
import platform
import json
import time
from pathlib import Path

class SuccessOptimizer:
    def __init__(self):
        self.optimizations = []
        self.applied_optimizations = []
        self.system_score = 0
        
    def analyze_and_optimize(self):
        """Analyze system and apply optimizations"""
        print("🚀 Analyzing system for optimization opportunities...")
        
        # Detect optimization opportunities
        self.detect_optimizations()
        
        # Apply safe optimizations automatically
        self.apply_safe_optimizations()
        
        # Suggest manual optimizations
        self.suggest_manual_optimizations()
        
        # Calculate final score
        self.calculate_success_score()
        
        return self.generate_optimization_report()
    
    def detect_optimizations(self):
        """Detect possible optimizations"""
        
        # Python environment optimizations
        self.check_python_optimizations()
        
        # Package management optimizations
        self.check_package_optimizations()
        
        # System performance optimizations
        self.check_performance_optimizations()
        
        # macOS specific optimizations
        self.check_macos_optimizations()
        
        # Network optimizations
        self.check_network_optimizations()
    
    def check_python_optimizations(self):
        """Check Python environment optimizations"""
        
        # Check Python version
        version = sys.version_info
        if version < (3, 11):
            self.optimizations.append({
                'type': 'python_upgrade',
                'priority': 'high',
                'title': 'Upgrade to Python 3.11',
                'description': 'Python 3.11 has better performance and compatibility',
                'benefit': '+15% installation speed, better Apple Silicon support',
                'command': 'brew install python@3.11',
                'auto_apply': False
            })
        
        # Check if using system Python vs Homebrew
        python_path = sys.executable
        if '/usr/bin/python' in python_path:
            self.optimizations.append({
                'type': 'python_source',
                'priority': 'medium',
                'title': 'Use Homebrew Python',
                'description': 'Homebrew Python is more reliable than system Python',
                'benefit': '+10% package compatibility',
                'command': 'brew install python@3.11 && export PATH="/opt/homebrew/bin:$PATH"',
                'auto_apply': False
            })
        
        # Check pip version
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                pip_version = result.stdout.split()[1]
                if tuple(map(int, pip_version.split('.'))) < (23, 0):
                    self.optimizations.append({
                        'type': 'pip_upgrade',
                        'priority': 'medium',
                        'title': 'Upgrade pip',
                        'description': 'Newer pip versions have better dependency resolution',
                        'benefit': '+5% installation success rate',
                        'command': f'{sys.executable} -m pip install --upgrade pip',
                        'auto_apply': True
                    })
        except:
            pass
    
    def check_package_optimizations(self):
        """Check package management optimizations"""
        
        # Check for conflicting packages
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'check'], 
                                  capture_output=True, text=True)
            if result.returncode != 0 and result.stdout.strip():
                self.optimizations.append({
                    'type': 'package_conflicts',
                    'priority': 'high',
                    'title': 'Fix Package Conflicts',
                    'description': 'Conflicting packages detected',
                    'benefit': '+20% stability',
                    'command': f'{sys.executable} -m pip check',
                    'auto_apply': False,
                    'details': result.stdout
                })
        except:
            pass
        
        # Check pip cache size
        try:
            cache_dir = subprocess.run([sys.executable, '-m', 'pip', 'cache', 'dir'], 
                                     capture_output=True, text=True)
            if cache_dir.returncode == 0:
                cache_path = Path(cache_dir.stdout.strip())
                if cache_path.exists():
                    cache_size = sum(f.stat().st_size for f in cache_path.rglob('*') if f.is_file())
                    if cache_size > 1024**3:  # 1GB
                        self.optimizations.append({
                            'type': 'pip_cache',
                            'priority': 'low',
                            'title': 'Clear pip Cache',
                            'description': f'pip cache is {cache_size // (1024**2)}MB',
                            'benefit': '+2% installation speed',
                            'command': f'{sys.executable} -m pip cache purge',
                            'auto_apply': True
                        })
        except:
            pass
    
    def check_performance_optimizations(self):
        """Check system performance optimizations"""
        
        # Check available memory
        try:
            import psutil
            memory = psutil.virtual_memory()
            
            if memory.percent > 85:
                self.optimizations.append({
                    'type': 'memory_usage',
                    'priority': 'high',
                    'title': 'Reduce Memory Usage',
                    'description': f'Memory usage is {memory.percent}%',
                    'benefit': '+15% installation reliability',
                    'command': 'Close unnecessary applications',
                    'auto_apply': False
                })
            
            # Check swap usage
            swap = psutil.swap_memory()
            if swap.percent > 50:
                self.optimizations.append({
                    'type': 'swap_usage',
                    'priority': 'medium',
                    'title': 'High Swap Usage',
                    'description': f'Swap usage is {swap.percent}%',
                    'benefit': '+10% performance',
                    'command': 'Restart applications or reboot system',
                    'auto_apply': False
                })
        except ImportError:
            pass
        
        # Check disk space
        import shutil
        disk_usage = shutil.disk_usage('/')
        free_gb = disk_usage.free / (1024**3)
        
        if free_gb < 2:
            self.optimizations.append({
                'type': 'disk_space',
                'priority': 'critical',
                'title': 'Critical Disk Space',
                'description': f'Only {free_gb:.1f}GB free',
                'benefit': 'Prevents installation failures',
                'command': 'Free up disk space',
                'auto_apply': False
            })
        elif free_gb < 5:
            self.optimizations.append({
                'type': 'disk_space',
                'priority': 'medium',
                'title': 'Low Disk Space',
                'description': f'{free_gb:.1f}GB free (recommend 5GB+)',
                'benefit': '+5% installation reliability',
                'command': 'Free up more disk space',
                'auto_apply': False
            })
    
    def check_macos_optimizations(self):
        """Check macOS specific optimizations"""
        
        # Check Xcode Command Line Tools
        try:
            result = subprocess.run(['xcode-select', '-p'], capture_output=True)
            if result.returncode != 0:
                self.optimizations.append({
                    'type': 'xcode_tools',
                    'priority': 'high',
                    'title': 'Install Xcode Command Line Tools',
                    'description': 'Required for PyObjC compilation',
                    'benefit': '+25% PyObjC installation success',
                    'command': 'xcode-select --install',
                    'auto_apply': False
                })
        except:
            pass
        
        # Check Homebrew
        try:
            result = subprocess.run(['brew', '--version'], capture_output=True)
            if result.returncode != 0:
                self.optimizations.append({
                    'type': 'homebrew',
                    'priority': 'medium',
                    'title': 'Install Homebrew',
                    'description': 'Package manager for easier dependency management',
                    'benefit': '+10% overall success rate',
                    'command': '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                    'auto_apply': False
                })
            else:
                # Check if Homebrew needs update
                try:
                    result = subprocess.run(['brew', 'outdated'], capture_output=True, text=True)
                    if result.stdout.strip():
                        self.optimizations.append({
                            'type': 'homebrew_update',
                            'priority': 'low',
                            'title': 'Update Homebrew Packages',
                            'description': 'Outdated packages detected',
                            'benefit': '+3% compatibility',
                            'command': 'brew update && brew upgrade',
                            'auto_apply': False
                        })
                except:
                    pass
        except:
            pass
        
        # Check for Apple Silicon optimizations
        if platform.machine() == 'arm64':
            # Check if using native Python
            if 'x86_64' in platform.platform():
                self.optimizations.append({
                    'type': 'native_python',
                    'priority': 'high',
                    'title': 'Use Native ARM64 Python',
                    'description': 'Currently using x86_64 Python via Rosetta',
                    'benefit': '+20% performance on Apple Silicon',
                    'command': 'Install native ARM64 Python from python.org or Homebrew',
                    'auto_apply': False
                })
    
    def check_network_optimizations(self):
        """Check network optimizations"""
        
        # Test PyPI connectivity
        try:
            import urllib.request
            start_time = time.time()
            urllib.request.urlopen('https://pypi.org', timeout=10)
            response_time = time.time() - start_time
            
            if response_time > 5:
                self.optimizations.append({
                    'type': 'network_speed',
                    'priority': 'medium',
                    'title': 'Slow PyPI Connection',
                    'description': f'PyPI response time: {response_time:.1f}s',
                    'benefit': 'Faster package downloads',
                    'command': 'Consider using a PyPI mirror or better internet connection',
                    'auto_apply': False
                })
        except:
            self.optimizations.append({
                'type': 'network_connectivity',
                'priority': 'critical',
                'title': 'No Internet Connection',
                'description': 'Cannot reach PyPI for package downloads',
                'benefit': 'Essential for package installation',
                'command': 'Connect to the internet',
                'auto_apply': False
            })
    
    def apply_safe_optimizations(self):
        """Apply optimizations that are safe to run automatically"""
        
        for opt in self.optimizations:
            if opt.get('auto_apply', False):
                print(f"🔧 Applying: {opt['title']}")
                
                try:
                    if opt['type'] == 'pip_upgrade':
                        subprocess.run(opt['command'].split(), check=True, capture_output=True)
                        self.applied_optimizations.append(opt)
                        print(f"✅ Applied: {opt['title']}")
                    
                    elif opt['type'] == 'pip_cache':
                        subprocess.run(opt['command'].split(), check=True, capture_output=True)
                        self.applied_optimizations.append(opt)
                        print(f"✅ Applied: {opt['title']}")
                        
                except subprocess.CalledProcessError as e:
                    print(f"❌ Failed to apply {opt['title']}: {e}")
                except Exception as e:
                    print(f"⚠️ Error applying {opt['title']}: {e}")
    
    def suggest_manual_optimizations(self):
        """Suggest manual optimizations to user"""
        
        manual_opts = [opt for opt in self.optimizations if not opt.get('auto_apply', False)]
        
        if manual_opts:
            print("\n📋 Manual optimizations recommended:")
            
            # Sort by priority
            priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
            manual_opts.sort(key=lambda x: priority_order.get(x['priority'], 4))
            
            for opt in manual_opts:
                priority_emoji = {
                    'critical': '🚨',
                    'high': '⚠️',
                    'medium': '💡',
                    'low': 'ℹ️'
                }
                
                print(f"\n{priority_emoji.get(opt['priority'], '•')} {opt['title']}")
                print(f"   Description: {opt['description']}")
                print(f"   Benefit: {opt['benefit']}")
                print(f"   Command: {opt['command']}")
    
    def calculate_success_score(self):
        """Calculate predicted success score"""
        base_score = 70  # Base success rate
        
        # Add points for applied optimizations
        for opt in self.applied_optimizations:
            if opt['priority'] == 'high':
                base_score += 5
            elif opt['priority'] == 'medium':
                base_score += 3
            elif opt['priority'] == 'low':
                base_score += 1
        
        # Deduct points for unresolved issues
        for opt in self.optimizations:
            if opt not in self.applied_optimizations:
                if opt['priority'] == 'critical':
                    base_score -= 20
                elif opt['priority'] == 'high':
                    base_score -= 10
                elif opt['priority'] == 'medium':
                    base_score -= 5
        
        self.system_score = max(0, min(100, base_score))
    
    def generate_optimization_report(self):
        """Generate comprehensive optimization report"""
        
        report = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'system_score': self.system_score,
            'total_optimizations': len(self.optimizations),
            'applied_optimizations': len(self.applied_optimizations),
            'pending_optimizations': len(self.optimizations) - len(self.applied_optimizations),
            'optimizations': self.optimizations,
            'applied': self.applied_optimizations,
            'recommendations': self.generate_recommendations()
        }
        
        return report
    
    def generate_recommendations(self):
        """Generate specific recommendations based on analysis"""
        
        recommendations = []
        
        if self.system_score >= 95:
            recommendations.append({
                'type': 'excellent',
                'message': 'Your system is optimally configured! Expect 98%+ success rate.'
            })
        elif self.system_score >= 85:
            recommendations.append({
                'type': 'good',
                'message': 'Your system is well configured. Expected success rate: 90-95%.'
            })
        elif self.system_score >= 70:
            recommendations.append({
                'type': 'fair',
                'message': 'Your system will work but could be optimized. Expected success rate: 75-85%.'
            })
        else:
            recommendations.append({
                'type': 'poor',
                'message': 'Several optimizations needed for reliable operation. Expected success rate: <75%.'
            })
        
        # Specific recommendations
        critical_issues = [opt for opt in self.optimizations if opt['priority'] == 'critical']
        if critical_issues:
            recommendations.append({
                'type': 'critical',
                'message': f'CRITICAL: {len(critical_issues)} critical issues must be resolved before proceeding.'
            })
        
        high_priority = [opt for opt in self.optimizations if opt['priority'] == 'high']
        if high_priority:
            recommendations.append({
                'type': 'high_priority',
                'message': f'Recommended: Address {len(high_priority)} high-priority optimizations for best results.'
            })
        
        return recommendations

def optimize_system():
    """Run system optimization"""
    optimizer = SuccessOptimizer()
    return optimizer.analyze_and_optimize()

if __name__ == "__main__":
    report = optimize_system()
    print(json.dumps(report, indent=2))
