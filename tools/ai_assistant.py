#!/usr/bin/env python3
"""
IRUS V5.0 - AI Assistant System
Machine learning powered user assistance and predictive support
"""

import json
import os
import time
import pickle
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import sqlite3

class UserBehaviorAnalyzer:
    """Machine learning system to analyze user behavior and predict issues"""
    
    def __init__(self):
        self.db_path = "user_analytics.db"
        self.model_path = "ai_models/"
        self.init_database()
        self.load_models()
        
    def init_database(self):
        """Initialize SQLite database for user analytics"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # User sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE,
                start_time TIMESTAMP,
                end_time TIMESTAMP,
                success BOOLEAN,
                errors_encountered TEXT,
                system_info TEXT,
                conversion_time REAL,
                user_actions TEXT
            )
        ''')
        
        # Error patterns table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS error_patterns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                error_type TEXT,
                error_message TEXT,
                system_context TEXT,
                resolution_method TEXT,
                success_rate REAL,
                frequency INTEGER DEFAULT 1,
                last_seen TIMESTAMP
            )
        ''')
        
        # User assistance events
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assistance_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                event_type TEXT,
                suggestion_given TEXT,
                user_accepted BOOLEAN,
                outcome TEXT,
                timestamp TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def load_models(self):
        """Load or initialize ML models"""
        
        os.makedirs(self.model_path, exist_ok=True)
        
        # Simple predictive models (can be enhanced with scikit-learn)
        self.error_prediction_model = {
            'patterns': {},
            'success_indicators': {},
            'risk_factors': {}
        }
        
        # Load existing model if available
        model_file = Path(self.model_path) / "prediction_model.pkl"
        if model_file.exists():
            try:
                with open(model_file, 'rb') as f:
                    self.error_prediction_model = pickle.load(f)
            except:
                pass  # Use default model
    
    def record_session(self, session_data: Dict):
        """Record user session for learning"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO user_sessions 
            (session_id, start_time, end_time, success, errors_encountered, 
             system_info, conversion_time, user_actions)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            session_data.get('session_id'),
            session_data.get('start_time'),
            session_data.get('end_time'),
            session_data.get('success', False),
            json.dumps(session_data.get('errors', [])),
            json.dumps(session_data.get('system_info', {})),
            session_data.get('conversion_time', 0),
            json.dumps(session_data.get('user_actions', []))
        ))
        
        conn.commit()
        conn.close()
        
        # Update ML model
        self.update_model(session_data)
    
    def record_error_pattern(self, error_type: str, error_message: str, 
                           system_context: Dict, resolution: str = None):
        """Record error patterns for learning"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if pattern exists
        cursor.execute('''
            SELECT id, frequency FROM error_patterns 
            WHERE error_type = ? AND error_message = ?
        ''', (error_type, error_message))
        
        result = cursor.fetchone()
        
        if result:
            # Update existing pattern
            cursor.execute('''
                UPDATE error_patterns 
                SET frequency = frequency + 1, last_seen = ?, resolution_method = ?
                WHERE id = ?
            ''', (datetime.now(), resolution, result[0]))
        else:
            # Insert new pattern
            cursor.execute('''
                INSERT INTO error_patterns 
                (error_type, error_message, system_context, resolution_method, last_seen)
                VALUES (?, ?, ?, ?, ?)
            ''', (error_type, error_message, json.dumps(system_context), 
                  resolution, datetime.now()))
        
        conn.commit()
        conn.close()
    
    def predict_issues(self, system_info: Dict) -> List[Dict]:
        """Predict potential issues based on system info"""
        
        predictions = []
        
        # Analyze system characteristics
        os_version = system_info.get('os_version', '')
        python_version = system_info.get('python_version', '')
        architecture = system_info.get('architecture', '')
        memory_gb = system_info.get('memory_total_gb', 0)
        
        # Rule-based predictions (can be enhanced with ML)
        
        # macOS version issues
        if 'macOS 10.' in os_version:
            version_num = float(os_version.split('macOS ')[1].split()[0])
            if version_num < 10.15:
                predictions.append({
                    'type': 'compatibility_warning',
                    'severity': 'HIGH',
                    'message': 'macOS version may be too old for optimal compatibility',
                    'suggestion': 'Consider upgrading to macOS 10.15 or newer',
                    'confidence': 0.9
                })
        
        # Python version issues
        if 'Python 3.' in python_version:
            version_parts = python_version.split('Python ')[1].split('.')
            if len(version_parts) >= 2:
                major, minor = int(version_parts[0]), int(version_parts[1])
                if major == 3 and minor < 8:
                    predictions.append({
                        'type': 'python_version_warning',
                        'severity': 'MEDIUM',
                        'message': 'Python version may cause compatibility issues',
                        'suggestion': 'Upgrade to Python 3.8 or newer',
                        'confidence': 0.8
                    })
        
        # Memory issues
        if memory_gb < 4:
            predictions.append({
                'type': 'memory_warning',
                'severity': 'MEDIUM',
                'message': 'Low system memory may affect performance',
                'suggestion': 'Close other applications before conversion',
                'confidence': 0.7
            })
        
        # Architecture-specific issues
        if architecture == 'arm64':
            predictions.append({
                'type': 'architecture_info',
                'severity': 'INFO',
                'message': 'Apple Silicon detected - using optimized packages',
                'suggestion': 'Ensure using native Python (not Rosetta)',
                'confidence': 0.6
            })
        
        # Query historical patterns
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT error_type, error_message, frequency, resolution_method
            FROM error_patterns 
            WHERE frequency > 2 
            ORDER BY frequency DESC 
            LIMIT 5
        ''')
        
        common_errors = cursor.fetchall()
        conn.close()
        
        for error_type, error_msg, frequency, resolution in common_errors:
            if frequency > 5:  # Common issue
                predictions.append({
                    'type': 'historical_pattern',
                    'severity': 'MEDIUM',
                    'message': f'Common issue: {error_type}',
                    'suggestion': resolution or 'Check documentation for solutions',
                    'confidence': min(0.9, frequency / 20)
                })
        
        return predictions
    
    def update_model(self, session_data: Dict):
        """Update ML model with new session data"""
        
        success = session_data.get('success', False)
        errors = session_data.get('errors', [])
        system_info = session_data.get('system_info', {})
        
        # Update success indicators
        for key, value in system_info.items():
            if key not in self.error_prediction_model['success_indicators']:
                self.error_prediction_model['success_indicators'][key] = {'success': 0, 'total': 0}
            
            self.error_prediction_model['success_indicators'][key]['total'] += 1
            if success:
                self.error_prediction_model['success_indicators'][key]['success'] += 1
        
        # Update error patterns
        for error in errors:
            error_key = f"{error.get('type', 'unknown')}:{error.get('message', '')[:50]}"
            if error_key not in self.error_prediction_model['patterns']:
                self.error_prediction_model['patterns'][error_key] = 0
            self.error_prediction_model['patterns'][error_key] += 1
        
        # Save updated model
        model_file = Path(self.model_path) / "prediction_model.pkl"
        try:
            with open(model_file, 'wb') as f:
                pickle.dump(self.error_prediction_model, f)
        except:
            pass  # Continue without saving

class AIAssistant:
    """AI-powered user assistant"""
    
    def __init__(self):
        self.behavior_analyzer = UserBehaviorAnalyzer()
        self.knowledge_base = self.load_knowledge_base()
        self.conversation_history = []
        
    def load_knowledge_base(self) -> Dict:
        """Load knowledge base for AI assistance"""
        
        return {
            'common_issues': {
                'ImportError': {
                    'solutions': [
                        'Install missing package: pip3 install [package_name]',
                        'Check Python environment: python3 --version',
                        'Verify package installation: pip3 list'
                    ],
                    'prevention': 'Run system validation before conversion'
                },
                'PermissionError': {
                    'solutions': [
                        'Grant macOS permissions in System Preferences',
                        'Restart Terminal after granting permissions',
                        'Check file permissions: ls -la'
                    ],
                    'prevention': 'Follow permission setup guide carefully'
                },
                'ModuleNotFoundError': {
                    'solutions': [
                        'Install required packages: pip3 install -r requirements.txt',
                        'Check virtual environment activation',
                        'Verify Python path: which python3'
                    ],
                    'prevention': 'Use automated installer for dependencies'
                }
            },
            'optimization_tips': {
                'performance': [
                    'Close unnecessary applications',
                    'Use native Python on Apple Silicon',
                    'Ensure sufficient disk space (500MB+)',
                    'Update to latest macOS version'
                ],
                'reliability': [
                    'Run system diagnostics first',
                    'Use stable internet connection',
                    'Avoid interrupting conversion process',
                    'Keep system updated'
                ]
            },
            'best_practices': [
                'Always test converted script before use',
                'Keep backup of original script',
                'Read post-conversion guide thoroughly',
                'Join Discord community for support'
            ]
        }
    
    def analyze_user_query(self, query: str, context: Dict = None) -> Dict:
        """Analyze user query and provide AI-powered assistance"""
        
        query_lower = query.lower()
        response = {
            'type': 'general',
            'confidence': 0.5,
            'suggestions': [],
            'actions': [],
            'resources': []
        }
        
        # Error-related queries
        if any(word in query_lower for word in ['error', 'failed', 'not working', 'broken']):
            response['type'] = 'error_assistance'
            response['confidence'] = 0.8
            
            # Extract potential error type
            for error_type in self.knowledge_base['common_issues']:
                if error_type.lower() in query_lower:
                    solutions = self.knowledge_base['common_issues'][error_type]['solutions']
                    response['suggestions'].extend(solutions)
                    response['confidence'] = 0.9
                    break
            
            if not response['suggestions']:
                response['suggestions'] = [
                    'Run system diagnostics: python3 tools/smart_diagnostics.py',
                    'Check Debug.txt for error details',
                    'Generate bug report: python3 tools/bug_reporter.py'
                ]
        
        # Performance-related queries
        elif any(word in query_lower for word in ['slow', 'performance', 'optimize', 'speed']):
            response['type'] = 'performance_optimization'
            response['confidence'] = 0.8
            response['suggestions'] = self.knowledge_base['optimization_tips']['performance']
        
        # Installation/setup queries
        elif any(word in query_lower for word in ['install', 'setup', 'configure', 'permission']):
            response['type'] = 'setup_assistance'
            response['confidence'] = 0.8
            response['suggestions'] = [
                'Follow installation guide: docs/post_conversion_guide.md',
                'Run automated installer: python3 gui/start_wizard.py',
                'Check system requirements: macOS 10.15+, Python 3.8+'
            ]
        
        # Usage queries
        elif any(word in query_lower for word in ['how to use', 'run', 'start', 'launch']):
            response['type'] = 'usage_guidance'
            response['confidence'] = 0.9
            response['suggestions'] = [
                'Navigate to output folder: cd output/',
                'Test the script: python3 fishing_macro_macos.py --test',
                'Run the macro: python3 fishing_macro_macos.py',
                'Configure settings: nano Config.txt'
            ]
        
        # Add contextual suggestions based on system info
        if context and context.get('system_info'):
            predictions = self.behavior_analyzer.predict_issues(context['system_info'])
            for prediction in predictions:
                if prediction['confidence'] > 0.7:
                    response['suggestions'].append(f"⚠️ {prediction['message']}: {prediction['suggestion']}")
        
        # Add relevant resources
        response['resources'] = [
            'Complete Guide: docs/post_conversion_guide.md',
            'Discord Support: [Join our community]',
            'Bug Reports: python3 tools/bug_reporter.py'
        ]
        
        return response
    
    def provide_proactive_assistance(self, session_data: Dict) -> List[Dict]:
        """Provide proactive assistance based on session analysis"""
        
        suggestions = []
        
        # Analyze session progress
        if session_data.get('current_step') == 'package_installation':
            if session_data.get('installation_time', 0) > 300:  # 5 minutes
                suggestions.append({
                    'type': 'performance_tip',
                    'message': 'Installation taking longer than usual',
                    'suggestion': 'Check internet connection and close other applications',
                    'priority': 'medium'
                })
        
        # Check for repeated errors
        errors = session_data.get('errors', [])
        if len(errors) > 2:
            error_types = [e.get('type') for e in errors]
            if len(set(error_types)) == 1:  # Same error type repeated
                suggestions.append({
                    'type': 'error_pattern',
                    'message': f'Repeated {error_types[0]} errors detected',
                    'suggestion': 'Consider running system diagnostics or reinstall script',
                    'priority': 'high'
                })
        
        # System-specific suggestions
        system_info = session_data.get('system_info', {})
        predictions = self.behavior_analyzer.predict_issues(system_info)
        
        for prediction in predictions:
            if prediction['confidence'] > 0.8:
                suggestions.append({
                    'type': 'predictive_assistance',
                    'message': prediction['message'],
                    'suggestion': prediction['suggestion'],
                    'priority': prediction['severity'].lower()
                })
        
        return suggestions
    
    def generate_smart_response(self, user_input: str, context: Dict = None) -> str:
        """Generate intelligent response to user input"""
        
        analysis = self.analyze_user_query(user_input, context)
        
        response_parts = []
        
        # Greeting based on confidence
        if analysis['confidence'] > 0.8:
            response_parts.append("🤖 I understand your question! Here's what I recommend:")
        elif analysis['confidence'] > 0.6:
            response_parts.append("🤖 I think I can help with that. Here are some suggestions:")
        else:
            response_parts.append("🤖 Let me provide some general assistance:")
        
        # Add suggestions
        if analysis['suggestions']:
            response_parts.append("\n📋 **Suggestions:**")
            for i, suggestion in enumerate(analysis['suggestions'][:3], 1):
                response_parts.append(f"{i}. {suggestion}")
        
        # Add resources
        if analysis['resources']:
            response_parts.append("\n📚 **Helpful Resources:**")
            for resource in analysis['resources'][:2]:
                response_parts.append(f"• {resource}")
        
        # Add follow-up
        response_parts.append("\n💬 Need more help? Generate a bug report or join our Discord community!")
        
        return "\n".join(response_parts)

def create_ai_chat_interface():
    """Create interactive AI chat interface"""
    
    assistant = AIAssistant()
    
    def chat_loop():
        print("🤖 IRUS V5.0 AI Assistant")
        print("=" * 40)
        print("Ask me anything about IRUS! Type 'quit' to exit.")
        print()
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 Goodbye! Feel free to ask for help anytime.")
                break
            
            if not user_input:
                continue
            
            # Generate AI response
            response = assistant.generate_smart_response(user_input)
            print(f"\n🤖 AI Assistant:\n{response}\n")
    
    return chat_loop

if __name__ == "__main__":
    # Test AI assistant
    assistant = AIAssistant()
    
    test_queries = [
        "I'm getting an ImportError",
        "How do I run the converted script?",
        "The conversion is very slow",
        "I need help with permissions"
    ]
    
    print("🧪 Testing AI Assistant...")
    for query in test_queries:
        print(f"\nQuery: {query}")
        response = assistant.generate_smart_response(query)
        print(f"Response: {response[:100]}...")
    
    print("\n✅ AI Assistant system ready!")
