#!/usr/bin/env python3
"""
IRUS V5.0 - Mobile Companion System
Discord-based mobile monitoring and control system
"""

import json
import time
import threading
import requests
from datetime import datetime
from typing import Dict, List, Optional
import psutil
import os

class MobileCompanionBot:
    """Discord-based mobile companion for remote monitoring and control"""
    
    def __init__(self):
        # Use feedback webhook for mobile companion (can be separate if needed)
        self.webhook_url = "https://discord.com/api/webhooks/1436233521537618040/rCpCZ4x4HeiTqXwHfrOQCINvIwqmxkwX4m9g9pqCJmYK-Xps_57VaHax-lhZr8qieSUQ"
        
        self.status_data = {
            'macro_running': False,
            'start_time': None,
            'fish_caught': 0,
            'errors_count': 0,
            'last_activity': None,
            'system_stats': {}
        }
        
        self.monitoring_active = False
        self.update_interval = 30  # seconds
        self.command_queue = []
        
    def start_monitoring(self):
        """Start mobile companion monitoring"""
        
        if self.monitoring_active:
            return
        
        self.monitoring_active = True
        
        # Send startup notification
        self.send_status_update("🚀 MOBILE_COMPANION_STARTED", {
            "message": "Mobile companion activated",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "update_interval": f"{self.update_interval}s"
        })
        
        # Start monitoring thread
        monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        monitor_thread.start()
        
        print("📱 Mobile companion started - Check Discord for updates")
    
    def stop_monitoring(self):
        """Stop mobile companion monitoring"""
        
        self.monitoring_active = False
        
        # Send shutdown notification
        self.send_status_update("🛑 MOBILE_COMPANION_STOPPED", {
            "message": "Mobile companion deactivated",
            "session_duration": self._get_session_duration(),
            "final_stats": self.status_data
        })
        
        print("📱 Mobile companion stopped")
    
    def _monitoring_loop(self):
        """Main monitoring loop"""
        
        while self.monitoring_active:
            try:
                # Update system stats
                self._update_system_stats()
                
                # Check for macro status changes
                self._check_macro_status()
                
                # Send periodic update
                self._send_periodic_update()
                
                # Process any commands
                self._process_commands()
                
                # Wait for next update
                time.sleep(self.update_interval)
                
            except Exception as e:
                print(f"❌ Monitoring error: {e}")
                time.sleep(5)  # Brief pause before retry
    
    def _update_system_stats(self):
        """Update system statistics"""
        
        try:
            # CPU and memory usage
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Disk usage
            disk = psutil.disk_usage('/')
            
            # Network stats (if available)
            network = psutil.net_io_counters()
            
            self.status_data['system_stats'] = {
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'memory_available_gb': round(memory.available / (1024**3), 2),
                'disk_free_gb': round(disk.free / (1024**3), 2),
                'network_sent_mb': round(network.bytes_sent / (1024**2), 2),
                'network_recv_mb': round(network.bytes_recv / (1024**2), 2)
            }
            
        except Exception as e:
            self.status_data['system_stats'] = {'error': str(e)}
    
    def _check_macro_status(self):
        """Check if fishing macro is running"""
        
        try:
            # Look for fishing macro process
            macro_running = False
            
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    cmdline = ' '.join(proc.info['cmdline'] or [])
                    if 'fishing_macro' in cmdline.lower() or 'fishing_bot' in cmdline.lower():
                        macro_running = True
                        break
                except:
                    continue
            
            # Status change detection
            if macro_running != self.status_data['macro_running']:
                if macro_running:
                    self._on_macro_started()
                else:
                    self._on_macro_stopped()
                
                self.status_data['macro_running'] = macro_running
            
            # Update last activity
            if macro_running:
                self.status_data['last_activity'] = datetime.now().isoformat()
                
        except Exception as e:
            print(f"❌ Error checking macro status: {e}")
    
    def _on_macro_started(self):
        """Handle macro start event"""
        
        self.status_data['start_time'] = datetime.now().isoformat()
        self.status_data['fish_caught'] = 0
        self.status_data['errors_count'] = 0
        
        self.send_status_update("🎣 MACRO_STARTED", {
            "message": "Fishing macro started",
            "start_time": self.status_data['start_time']
        })
    
    def _on_macro_stopped(self):
        """Handle macro stop event"""
        
        session_duration = self._get_session_duration()
        
        self.send_status_update("⏹️ MACRO_STOPPED", {
            "message": "Fishing macro stopped",
            "session_duration": session_duration,
            "fish_caught": self.status_data['fish_caught'],
            "errors_encountered": self.status_data['errors_count']
        })
    
    def _send_periodic_update(self):
        """Send periodic status update"""
        
        if not self.status_data['macro_running']:
            return  # Only send updates when macro is running
        
        # Check if it's time for an update (every 5 minutes when running)
        if hasattr(self, '_last_update'):
            time_since_update = time.time() - self._last_update
            if time_since_update < 300:  # 5 minutes
                return
        
        self._last_update = time.time()
        
        # Read recent logs for fish count and errors
        self._analyze_recent_logs()
        
        self.send_status_update("📊 PERIODIC_UPDATE", {
            "status": "Running",
            "session_duration": self._get_session_duration(),
            "fish_caught": self.status_data['fish_caught'],
            "errors_count": self.status_data['errors_count'],
            "system_stats": self.status_data['system_stats']
        })
    
    def _analyze_recent_logs(self):
        """Analyze recent log files for statistics"""
        
        try:
            log_files = ['Debug.txt', 'output/Debug.txt']
            
            for log_file in log_files:
                if os.path.exists(log_file):
                    with open(log_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # Analyze last 100 lines for recent activity
                    recent_lines = lines[-100:] if len(lines) > 100 else lines
                    
                    # Count fish caught (look for success indicators)
                    fish_indicators = ['fish caught', 'catch successful', 'fish detected']
                    for line in recent_lines:
                        line_lower = line.lower()
                        if any(indicator in line_lower for indicator in fish_indicators):
                            self.status_data['fish_caught'] += 1
                    
                    # Count errors
                    error_indicators = ['error', 'exception', 'failed', 'warning']
                    for line in recent_lines:
                        line_lower = line.lower()
                        if any(indicator in line_lower for indicator in error_indicators):
                            self.status_data['errors_count'] += 1
                    
                    break  # Use first available log file
                    
        except Exception as e:
            print(f"❌ Error analyzing logs: {e}")
    
    def _get_session_duration(self):
        """Get current session duration"""
        
        if not self.status_data['start_time']:
            return "Not started"
        
        start_time = datetime.fromisoformat(self.status_data['start_time'])
        duration = datetime.now() - start_time
        
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        
        if hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    
    def _process_commands(self):
        """Process remote commands (placeholder for future implementation)"""
        
        # This would integrate with Discord bot commands in the future
        # For now, it's a placeholder for the command processing system
        pass
    
    def send_status_update(self, status_type: str, details: Dict = None):
        """Send status update to Discord"""
        
        # Status type colors and emojis
        status_config = {
            'MOBILE_COMPANION_STARTED': {'color': 0x00FF00, 'emoji': '📱'},
            'MOBILE_COMPANION_STOPPED': {'color': 0xFF6600, 'emoji': '📱'},
            'MACRO_STARTED': {'color': 0x00FF00, 'emoji': '🎣'},
            'MACRO_STOPPED': {'color': 0xFF6600, 'emoji': '⏹️'},
            'PERIODIC_UPDATE': {'color': 0x0099FF, 'emoji': '📊'},
            'ERROR_ALERT': {'color': 0xFF0000, 'emoji': '🚨'},
            'SUCCESS_MILESTONE': {'color': 0x00FF00, 'emoji': '🎉'}
        }
        
        config = status_config.get(status_type, {'color': 0x0099FF, 'emoji': '📱'})
        
        # Create embed
        embed = {
            "title": f"{config['emoji']} IRUS Mobile Companion",
            "description": f"**Status:** {status_type.replace('_', ' ').title()}",
            "color": config['color'],
            "timestamp": datetime.utcnow().isoformat(),
            "fields": [],
            "footer": {
                "text": "IRUS V5.0 Mobile Companion",
                "icon_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png"
            }
        }
        
        # Add details as fields
        if details:
            for key, value in details.items():
                # Format field name
                field_name = key.replace('_', ' ').title()
                
                # Format field value
                if isinstance(value, dict):
                    field_value = '\n'.join([f"**{k}:** {v}" for k, v in value.items()])
                else:
                    field_value = str(value)
                
                embed['fields'].append({
                    "name": field_name,
                    "value": field_value[:1024],  # Discord field limit
                    "inline": len(field_value) < 50
                })
        
        # Add quick stats if macro is running
        if self.status_data['macro_running']:
            embed['fields'].append({
                "name": "📈 Quick Stats",
                "value": f"**Duration:** {self._get_session_duration()}\n"
                        f"**Fish Caught:** {self.status_data['fish_caught']}\n"
                        f"**Errors:** {self.status_data['errors_count']}",
                "inline": True
            })
        
        try:
            payload = {
                "username": "IRUS Mobile Companion",
                "avatar_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png",
                "embeds": [embed]
            }
            
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            return response.status_code == 204
            
        except Exception as e:
            print(f"❌ Failed to send mobile update: {e}")
            return False
    
    def send_milestone_alert(self, milestone_type: str, count: int):
        """Send milestone achievement alert"""
        
        milestones = {
            'fish_caught': {
                10: "🎣 First 10 fish caught!",
                50: "🐟 50 fish milestone reached!",
                100: "🏆 Century club - 100 fish!",
                500: "🌟 Amazing! 500 fish caught!",
                1000: "👑 Legendary! 1000 fish milestone!"
            }
        }
        
        if milestone_type in milestones and count in milestones[milestone_type]:
            message = milestones[milestone_type][count]
            
            self.send_status_update("SUCCESS_MILESTONE", {
                "achievement": message,
                "total_count": count,
                "session_duration": self._get_session_duration()
            })
    
    def send_error_alert(self, error_type: str, error_message: str):
        """Send error alert to mobile"""
        
        self.send_status_update("ERROR_ALERT", {
            "error_type": error_type,
            "error_message": error_message[:200],  # Truncate long messages
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "suggestion": "Check the main application for details"
        })

class MobileCompanionManager:
    """Manager for mobile companion functionality"""
    
    def __init__(self):
        self.companion = MobileCompanionBot()
        self.auto_start = True
        
    def start(self):
        """Start mobile companion"""
        
        print("📱 Starting IRUS Mobile Companion...")
        print("🔗 Updates will be sent to Discord")
        print("📊 Monitor your fishing macro remotely!")
        
        self.companion.start_monitoring()
        
        return True
    
    def stop(self):
        """Stop mobile companion"""
        
        self.companion.stop_monitoring()
        return True
    
    def send_test_update(self):
        """Send test update to verify connection"""
        
        return self.companion.send_status_update("📱 TEST_MESSAGE", {
            "message": "Mobile companion test successful!",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Connection verified"
        })

def setup_mobile_companion():
    """Setup mobile companion with user interaction"""
    
    print("📱 IRUS V5.0 Mobile Companion Setup")
    print("=" * 40)
    print()
    print("The mobile companion allows you to monitor your fishing macro")
    print("remotely through Discord notifications on your phone.")
    print()
    
    # Test connection
    print("🧪 Testing Discord connection...")
    manager = MobileCompanionManager()
    
    if manager.send_test_update():
        print("✅ Discord connection successful!")
        print()
        
        # Ask user if they want to start monitoring
        start_monitoring = input("Start mobile monitoring now? (y/n): ").lower().startswith('y')
        
        if start_monitoring:
            manager.start()
            
            print()
            print("📱 Mobile Companion Active!")
            print("🔔 You'll receive Discord notifications for:")
            print("  • Macro start/stop events")
            print("  • Fish caught milestones") 
            print("  • Error alerts")
            print("  • Periodic status updates")
            print()
            print("💡 Keep Discord open on your phone for real-time updates!")
            
            return manager
        else:
            print("📱 Mobile companion ready but not started.")
            print("💡 Use manager.start() to begin monitoring anytime.")
            return manager
    else:
        print("❌ Discord connection failed!")
        print("🔧 Please check your internet connection and try again.")
        return None

if __name__ == "__main__":
    # Setup and test mobile companion
    companion_manager = setup_mobile_companion()
    
    if companion_manager:
        try:
            # Keep running for demonstration
            print("\n⏸️ Press Ctrl+C to stop mobile companion...")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Stopping mobile companion...")
            companion_manager.stop()
            print("✅ Mobile companion stopped.")
