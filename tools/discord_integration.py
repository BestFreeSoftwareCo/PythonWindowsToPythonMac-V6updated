#!/usr/bin/env python3
"""
IRUS V5.0 - Discord Integration System
Advanced Discord webhook integration with content filtering and embeds
"""

import re
import json
import time
import requests
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ContentFilter:
    """Advanced content filtering system"""
    
    def __init__(self):
        # Comprehensive profanity and slur detection
        self.blocked_words = {
            # Racial slurs (partial list - add more as needed)
            'racial_slurs': [
                # Note: Using partial matching to catch variations
                'n1gg', 'n!gg', 'n*gg', 'f4gg', 'f@gg',
                'ch1nk', 'ch!nk', 'sp1c', 'sp!c', 'k1ke', 'k!ke'
            ],
            # General profanity
            'profanity': [
                'f*ck', 'f**k', 'sh*t', 'sh!t', 'b*tch', 'b!tch',
                'a**hole', 'a$$hole', 'd*mn', 'd@mn', 'h*ll', 'h@ll'
            ],
            # Hate speech indicators
            'hate_speech': [
                'kill yourself', 'kys', 'die in', 'go die', 'neck yourself',
                'hitler', 'nazi', 'holocaust', 'genocide'
            ]
        }
        
        # URL/Link patterns
        self.url_patterns = [
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            r'www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            r'[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}',
            r'discord\.gg/[a-zA-Z0-9]+',
            r'bit\.ly/[a-zA-Z0-9]+',
            r'tinyurl\.com/[a-zA-Z0-9]+'
        ]
        
        # Image file extensions
        self.image_extensions = [
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', 
            '.svg', '.tiff', '.ico', '.heic', '.heif'
        ]
    
    def check_content(self, text: str) -> Tuple[bool, List[str]]:
        """
        Check if content is appropriate
        Returns: (is_clean, violations)
        """
        violations = []
        text_lower = text.lower()
        
        # Check for racial slurs (highest priority)
        for category, words in self.blocked_words.items():
            for word in words:
                # Remove special characters for matching
                clean_word = re.sub(r'[^a-zA-Z0-9]', '', word.lower())
                clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text_lower)
                
                if clean_word in clean_text:
                    violations.append(f"{category}: {word}")
        
        # Check for URLs/links
        for pattern in self.url_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                violations.append("links_not_allowed")
        
        # Check for image references
        for ext in self.image_extensions:
            if ext.lower() in text_lower:
                violations.append("images_not_allowed")
        
        return len(violations) == 0, violations
    
    def get_warning_message(self, violations: List[str]) -> str:
        """Generate appropriate warning message"""
        
        if any('racial_slurs' in v or 'hate_speech' in v for v in violations):
            return "⚠️ **CONTENT BLOCKED**: Hate speech and discriminatory language are not tolerated. Please be respectful."
        
        if any('profanity' in v for v in violations):
            return "⚠️ **CONTENT BLOCKED**: Please keep your message professional and family-friendly."
        
        if 'links_not_allowed' in violations:
            return "⚠️ **LINKS NOT ALLOWED**: For security reasons, links are not permitted in bug reports. Please describe the issue in text."
        
        if 'images_not_allowed' in violations:
            return "⚠️ **IMAGES NOT ALLOWED**: Please describe your issue in text rather than referencing image files."
        
        return "⚠️ **CONTENT BLOCKED**: Your message contains inappropriate content. Please revise and try again."

class DiscordWebhookManager:
    """Advanced Discord webhook management"""
    
    def __init__(self):
        self.bug_report_webhook = "https://discord.com/api/webhooks/1436231279346454598/RTHmUHi_vCVsUKa7ER6W7iQGhnz9Iuqz3CfXhMzat-NyPeAi-0DcbpfM4UvXJcfuAWp1"
        self.feedback_webhook = "https://discord.com/api/webhooks/1436233521537618040/rCpCZ4x4HeiTqXwHfrOQCINvIwqmxkwX4m9g9pqCJmYK-Xps_57VaHax-lhZr8qieSUQ"
        self.content_filter = ContentFilter()
        
    def create_bug_report_embed(self, report_data: Dict) -> Dict:
        """Create rich embed for bug reports"""
        
        # Determine embed color based on severity
        severity_colors = {
            'CRITICAL': 0xFF0000,  # Red
            'HIGH': 0xFF6600,      # Orange
            'MEDIUM': 0xFFFF00,    # Yellow
            'LOW': 0x00FF00,       # Green
            'INFO': 0x0099FF       # Blue
        }
        
        severity = 'MEDIUM'
        if report_data.get('error_details', {}).get('error_type'):
            error_type = report_data['error_details']['error_type']
            if error_type in ['ImportError', 'ModuleNotFoundError', 'SyntaxError']:
                severity = 'CRITICAL'
            elif error_type in ['PermissionError', 'FileNotFoundError']:
                severity = 'HIGH'
        
        color = severity_colors.get(severity, 0x0099FF)
        
        # Create embed
        embed = {
            "title": "🐛 IRUS V5.0 Bug Report",
            "description": f"**Report ID:** `{report_data.get('report_id', 'Unknown')}`",
            "color": color,
            "timestamp": datetime.utcnow().isoformat(),
            "fields": [
                {
                    "name": "📊 System Information",
                    "value": f"**OS:** {report_data.get('system_info', {}).get('os', 'Unknown')}\n"
                            f"**Python:** {report_data.get('system_info', {}).get('python_version', 'Unknown').split()[0]}\n"
                            f"**Architecture:** {report_data.get('system_info', {}).get('architecture', 'Unknown')}",
                    "inline": True
                },
                {
                    "name": "🚨 Error Details",
                    "value": f"**Type:** `{report_data.get('error_details', {}).get('error_type', 'General Issue')}`\n"
                            f"**Message:** `{report_data.get('error_details', {}).get('error_message', 'No specific error')[:100]}...`",
                    "inline": True
                },
                {
                    "name": "💬 User Description",
                    "value": report_data.get('user_description', 'No description provided')[:500] + 
                            ('...' if len(report_data.get('user_description', '')) > 500 else ''),
                    "inline": False
                }
            ],
            "footer": {
                "text": f"IRUS V5.0 • Severity: {severity}",
                "icon_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png"  # Replace with actual icon
            }
        }
        
        # Add contact info if provided
        if report_data.get('contact_info'):
            embed['fields'].append({
                "name": "📞 Contact Information",
                "value": report_data['contact_info'][:100],
                "inline": True
            })
        
        # Add log file info
        if report_data.get('log_files'):
            log_info = f"**Files Collected:** {len(report_data['log_files'])}\n"
            for log_file in report_data['log_files'][:3]:  # Show first 3
                log_info += f"• {log_file.get('filename', 'Unknown')}\n"
            
            embed['fields'].append({
                "name": "📝 Log Files",
                "value": log_info,
                "inline": True
            })
        
        return embed
    
    def create_feedback_embed(self, rating: int, feedback_text: str, user_info: str = "") -> Dict:
        """Create rich embed for feedback"""
        
        # Rating colors and emojis
        rating_config = {
            5: {"color": 0x00FF00, "emoji": "⭐⭐⭐⭐⭐", "title": "Excellent Feedback!"},
            4: {"color": 0x99FF00, "emoji": "⭐⭐⭐⭐", "title": "Great Feedback!"},
            3: {"color": 0xFFFF00, "emoji": "⭐⭐⭐", "title": "Good Feedback"},
            2: {"color": 0xFF9900, "emoji": "⭐⭐", "title": "Feedback Received"},
            1: {"color": 0xFF0000, "emoji": "⭐", "title": "Feedback Received"}
        }
        
        config = rating_config.get(rating, rating_config[3])
        
        embed = {
            "title": f"📝 {config['title']}",
            "description": f"{config['emoji']} **{rating}/5 Stars**",
            "color": config['color'],
            "timestamp": datetime.utcnow().isoformat(),
            "fields": [
                {
                    "name": "💬 User Feedback",
                    "value": feedback_text[:1000] + ('...' if len(feedback_text) > 1000 else ''),
                    "inline": False
                }
            ],
            "footer": {
                "text": "IRUS V5.0 Feedback System",
                "icon_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png"  # Replace with actual icon
            }
        }
        
        if user_info:
            embed['fields'].append({
                "name": "👤 User Info",
                "value": user_info[:100],
                "inline": True
            })
        
        return embed
    
    def send_bug_report(self, report_data: Dict) -> Tuple[bool, str]:
        """Send bug report to Discord with content filtering"""
        
        # Filter user description
        user_desc = report_data.get('user_description', '')
        is_clean, violations = self.content_filter.check_content(user_desc)
        
        if not is_clean:
            warning = self.content_filter.get_warning_message(violations)
            return False, warning
        
        # Filter contact info
        contact_info = report_data.get('contact_info', '')
        if contact_info:
            is_clean, violations = self.content_filter.check_content(contact_info)
            if not is_clean:
                warning = self.content_filter.get_warning_message(violations)
                return False, warning
        
        try:
            embed = self.create_bug_report_embed(report_data)
            
            payload = {
                "username": "IRUS Bug Reporter",
                "avatar_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png",  # Replace with actual icon
                "embeds": [embed]
            }
            
            response = requests.post(
                self.bug_report_webhook,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 204:
                return True, "✅ Bug report submitted successfully to Discord!"
            else:
                return False, f"❌ Discord submission failed: HTTP {response.status_code}"
                
        except requests.exceptions.Timeout:
            return False, "❌ Request timed out. Please check your internet connection."
        except requests.exceptions.RequestException as e:
            return False, f"❌ Network error: {str(e)}"
        except Exception as e:
            return False, f"❌ Unexpected error: {str(e)}"
    
    def send_feedback(self, rating: int, feedback_text: str, user_info: str = "") -> Tuple[bool, str]:
        """Send feedback to Discord with content filtering"""
        
        # Validate rating
        if not 1 <= rating <= 5:
            return False, "❌ Rating must be between 1 and 5 stars."
        
        # Filter feedback text
        is_clean, violations = self.content_filter.check_content(feedback_text)
        if not is_clean:
            warning = self.content_filter.get_warning_message(violations)
            return False, warning
        
        # Filter user info
        if user_info:
            is_clean, violations = self.content_filter.check_content(user_info)
            if not is_clean:
                warning = self.content_filter.get_warning_message(violations)
                return False, warning
        
        try:
            embed = self.create_feedback_embed(rating, feedback_text, user_info)
            
            payload = {
                "username": "IRUS Feedback System",
                "avatar_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png",  # Replace with actual icon
                "embeds": [embed]
            }
            
            response = requests.post(
                self.feedback_webhook,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 204:
                return True, f"✅ Thank you for your {rating}-star feedback! Submitted to Discord successfully."
            else:
                return False, f"❌ Discord submission failed: HTTP {response.status_code}"
                
        except requests.exceptions.Timeout:
            return False, "❌ Request timed out. Please check your internet connection."
        except requests.exceptions.RequestException as e:
            return False, f"❌ Network error: {str(e)}"
        except Exception as e:
            return False, f"❌ Unexpected error: {str(e)}"

class MobileCompanionBot:
    """Discord-based mobile companion for monitoring and control"""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self.status_messages = []
        
    def send_status_update(self, status: str, details: Dict = None) -> bool:
        """Send status update to Discord for mobile monitoring"""
        
        status_colors = {
            'STARTED': 0x00FF00,
            'RUNNING': 0x0099FF,
            'PAUSED': 0xFFFF00,
            'STOPPED': 0xFF6600,
            'ERROR': 0xFF0000,
            'SUCCESS': 0x00FF00
        }
        
        embed = {
            "title": "🎣 IRUS Mobile Companion",
            "description": f"**Status:** {status}",
            "color": status_colors.get(status, 0x0099FF),
            "timestamp": datetime.utcnow().isoformat(),
            "fields": [],
            "footer": {
                "text": "IRUS V5.0 Mobile Companion",
                "icon_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png"
            }
        }
        
        if details:
            for key, value in details.items():
                embed['fields'].append({
                    "name": key.replace('_', ' ').title(),
                    "value": str(value),
                    "inline": True
                })
        
        try:
            payload = {
                "username": "IRUS Mobile Companion",
                "embeds": [embed]
            }
            
            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=5
            )
            
            return response.status_code == 204
            
        except:
            return False

# Integration functions for existing systems
def integrate_discord_with_bug_reporter():
    """Update existing bug reporter to use Discord webhooks"""
    
    discord_manager = DiscordWebhookManager()
    
    def enhanced_report_bug(report_data):
        """Enhanced bug reporting with Discord integration"""
        
        # Send to Discord
        success, message = discord_manager.send_bug_report(report_data)
        
        if success:
            print(message)
            print(f"📋 Report ID: {report_data.get('report_id', 'Unknown')}")
            print(f"🔗 Check Discord for community support and developer response")
        else:
            print(message)
            print(f"📄 Report saved locally for manual submission")
        
        return success
    
    return enhanced_report_bug

def create_feedback_system():
    """Create interactive feedback system"""
    
    discord_manager = DiscordWebhookManager()
    
    def collect_feedback():
        """Interactive feedback collection"""
        
        print("⭐ IRUS V5.0 Feedback System")
        print("=" * 40)
        
        # Get rating
        while True:
            try:
                rating = int(input("Rate your experience (1-5 stars): "))
                if 1 <= rating <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get feedback text
        print("\nTell us about your experience:")
        feedback_text = input("> ")
        
        # Get optional user info
        print("\nOptional - Your Discord username or contact info:")
        user_info = input("> ")
        
        # Submit feedback
        print("\n📤 Submitting feedback...")
        success, message = discord_manager.send_feedback(rating, feedback_text, user_info)
        print(message)
        
        return success
    
    return collect_feedback

if __name__ == "__main__":
    # Test the systems
    print("🧪 Testing Discord Integration...")
    
    # Test content filter
    filter_test = ContentFilter()
    test_messages = [
        "This is a clean message",
        "Check out this link: https://example.com",
        "Here's my screenshot.png",
        "This contains bad words that should be blocked"
    ]
    
    for msg in test_messages:
        is_clean, violations = filter_test.check_content(msg)
        print(f"Message: '{msg[:30]}...' - Clean: {is_clean}")
        if violations:
            print(f"  Violations: {violations}")
    
    print("\n✅ Discord integration system ready!")
