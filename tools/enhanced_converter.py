#!/usr/bin/env python3
"""
IRUS V4 - Enhanced Script Converter
Converts Windows fishing macros to macOS with bug fixes and clean comments
"""

import re
import os
import sys
from pathlib import Path

class EnhancedConverter:
    def __init__(self):
        self.conversion_log = []
        self.bugs_fixed = []
        
    def convert_script(self, input_path, output_path):
        """Convert Windows script to macOS with enhanced bug fixing"""
        
        print(f"🔄 Converting {input_path} to macOS...")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Error reading input file: {e}")
            return False
        
        # Apply conversions
        converted_content = self.apply_all_conversions(content)
        
        # Clean up comments
        converted_content = self.clean_comments(converted_content)
        
        # Fix common bugs
        converted_content = self.fix_common_bugs(converted_content)
        
        # Add macOS-specific optimizations
        converted_content = self.add_macos_optimizations(converted_content)
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(converted_content)
            
            print(f"✅ Conversion complete: {output_path}")
            self.print_conversion_summary()
            return True
            
        except Exception as e:
            print(f"❌ Error writing output file: {e}")
            return False
    
    def apply_all_conversions(self, content):
        """Apply all Windows to macOS conversions"""
        
        # Import conversions
        content = self.convert_imports(content)
        
        # Screen capture conversions
        content = self.convert_screen_capture(content)
        
        # Mouse control conversions
        content = self.convert_mouse_control(content)
        
        # Keyboard control conversions
        content = self.convert_keyboard_control(content)
        
        # System API conversions
        content = self.convert_system_apis(content)
        
        # File path conversions
        content = self.convert_file_paths(content)
        
        return content
    
    def convert_imports(self, content):
        """Convert Windows imports to macOS equivalents"""
        
        conversions = [
            # Screen capture
            (r'import mss', '# Screen capture - converted to Quartz\nfrom Quartz import CGWindowListCopyWindowInfo, CGDisplayCreateImage, CGMainDisplayID\nfrom Quartz.CoreGraphics import CGRectMake'),
            (r'from mss import mss', '# Screen capture - converted to Quartz\nfrom Quartz import CGWindowListCopyWindowInfo, CGDisplayCreateImage, CGMainDisplayID\nfrom Quartz.CoreGraphics import CGRectMake'),
            
            # Mouse control
            (r'import pyautogui', '# Mouse control - converted to pynput\nfrom pynput.mouse import Button, Listener as MouseListener\nfrom pynput import mouse'),
            (r'from pyautogui import.*', '# Mouse control - converted to pynput\nfrom pynput.mouse import Button, Listener as MouseListener\nfrom pynput import mouse'),
            
            # Keyboard control
            (r'import keyboard', '# Keyboard control - converted to pynput\nfrom pynput.keyboard import Key, Listener as KeyboardListener\nfrom pynput import keyboard'),
            (r'from keyboard import.*', '# Keyboard control - converted to pynput\nfrom pynput.keyboard import Key, Listener as KeyboardListener\nfrom pynput import keyboard'),
            
            # Windows-specific
            (r'import ctypes\.windll.*', '# Windows APIs removed - using macOS native APIs'),
            (r'from ctypes import windll', '# Windows APIs removed - using macOS native APIs'),
        ]
        
        for old_pattern, new_code in conversions:
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_code, content)
                self.conversion_log.append(f"Converted import: {old_pattern}")
        
        return content
    
    def convert_screen_capture(self, content):
        """Convert screen capture from mss to Quartz"""
        
        # Replace mss screen capture
        mss_patterns = [
            (r'with mss\.mss\(\) as sct:', 'def capture_screen():'),
            (r'sct\.grab\(monitor\)', 'capture_screen_region()'),
            (r'mss\.mss\(\)\.grab\([^)]+\)', 'capture_screen_region()'),
        ]
        
        for old_pattern, new_code in mss_patterns:
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_code, content)
                self.conversion_log.append(f"Converted screen capture: {old_pattern}")
        
        # Add macOS screen capture implementation
        if 'mss' in content or 'sct.grab' in content:
            screen_capture_code = '''
# macOS Screen Capture Implementation
def capture_screen_region(x=0, y=0, width=None, height=None):
    """Capture screen region using Quartz"""
    import Quartz
    from PIL import Image
    import numpy as np
    
    # Get main display
    display_id = Quartz.CGMainDisplayID()
    
    if width is None or height is None:
        # Get full screen dimensions
        bounds = Quartz.CGDisplayBounds(display_id)
        width = int(bounds.size.width)
        height = int(bounds.size.height)
    
    # Create image from display
    region = Quartz.CGRectMake(x, y, width, height)
    image_ref = Quartz.CGDisplayCreateImageForRect(display_id, region)
    
    if image_ref is None:
        return None
    
    # Convert to PIL Image
    width = Quartz.CGImageGetWidth(image_ref)
    height = Quartz.CGImageGetHeight(image_ref)
    bytes_per_row = Quartz.CGImageGetBytesPerRow(image_ref)
    
    # Get image data
    data_provider = Quartz.CGImageGetDataProvider(image_ref)
    data = Quartz.CGDataProviderCopyData(data_provider)
    
    # Convert to numpy array
    img_array = np.frombuffer(data, dtype=np.uint8)
    img_array = img_array.reshape((height, bytes_per_row))
    
    # Extract RGB channels (skip alpha)
    img_array = img_array[:, :width*4].reshape((height, width, 4))
    img_array = img_array[:, :, [2, 1, 0]]  # BGR to RGB
    
    return Image.fromarray(img_array)

'''
            content = screen_capture_code + content
            self.conversion_log.append("Added macOS screen capture implementation")
        
        return content
    
    def convert_mouse_control(self, content):
        """Convert mouse control from pyautogui to pynput"""
        
        mouse_conversions = [
            (r'pyautogui\.click\(([^)]+)\)', r'mouse_controller.click(Button.left, 1)  # Position: \1'),
            (r'pyautogui\.rightClick\(([^)]+)\)', r'mouse_controller.click(Button.right, 1)  # Position: \1'),
            (r'pyautogui\.moveTo\(([^)]+)\)', r'mouse_controller.position = (\1)'),
            (r'pyautogui\.drag\(([^)]+)\)', r'mouse_controller.drag(\1)'),
        ]
        
        for old_pattern, new_code in mouse_conversions:
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_code, content)
                self.conversion_log.append(f"Converted mouse control: {old_pattern}")
        
        # Add mouse controller initialization
        if 'pyautogui' in content:
            mouse_init = '''
# macOS Mouse Control Setup
from pynput import mouse
mouse_controller = mouse.Controller()

'''
            content = mouse_init + content
            self.conversion_log.append("Added macOS mouse controller")
        
        return content
    
    def convert_keyboard_control(self, content):
        """Convert keyboard control to pynput"""
        
        keyboard_conversions = [
            (r'keyboard\.is_pressed\([\'"]([^\'"]+)[\'"]\)', r'is_key_pressed("\1")'),
            (r'keyboard\.wait\([\'"]([^\'"]+)[\'"]\)', r'wait_for_key("\1")'),
            (r'keyboard\.press\([\'"]([^\'"]+)[\'"]\)', r'keyboard_controller.press(Key.\1)'),
        ]
        
        for old_pattern, new_code in keyboard_conversions:
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_code, content)
                self.conversion_log.append(f"Converted keyboard control: {old_pattern}")
        
        # Add keyboard helper functions
        if 'keyboard.is_pressed' in content or 'keyboard.wait' in content:
            keyboard_helpers = '''
# macOS Keyboard Control Setup
from pynput import keyboard
from pynput.keyboard import Key, Listener as KeyboardListener
import threading

keyboard_controller = keyboard.Controller()
pressed_keys = set()

def on_key_press(key):
    """Handle key press events"""
    try:
        pressed_keys.add(key.char)
    except AttributeError:
        pressed_keys.add(key)

def on_key_release(key):
    """Handle key release events"""
    try:
        pressed_keys.discard(key.char)
    except AttributeError:
        pressed_keys.discard(key)

def is_key_pressed(key_name):
    """Check if key is currently pressed"""
    return key_name in pressed_keys or getattr(Key, key_name, None) in pressed_keys

def wait_for_key(key_name):
    """Wait for key press"""
    while not is_key_pressed(key_name):
        time.sleep(0.01)

# Start keyboard listener
keyboard_listener = KeyboardListener(on_press=on_key_press, on_release=on_key_release)
keyboard_listener.start()

'''
            content = keyboard_helpers + content
            self.conversion_log.append("Added macOS keyboard helpers")
        
        return content
    
    def convert_system_apis(self, content):
        """Convert Windows system APIs to macOS equivalents"""
        
        # Remove Windows-specific API calls
        windows_apis = [
            r'ctypes\.windll\.[^(]+\([^)]*\)',
            r'windll\.[^(]+\([^)]*\)',
            r'GetDC\([^)]*\)',
            r'GetDeviceCaps\([^)]*\)',
            r'ReleaseDC\([^)]*\)',
        ]
        
        for api_pattern in windows_apis:
            if re.search(api_pattern, content):
                content = re.sub(api_pattern, '# Windows API removed - using macOS native APIs', content)
                self.conversion_log.append(f"Removed Windows API: {api_pattern}")
        
        return content
    
    def convert_file_paths(self, content):
        """Convert Windows file paths to Unix paths"""
        
        # Convert Windows paths
        path_conversions = [
            (r'[A-Z]:\\[^"\']*', lambda m: m.group(0).replace('\\', '/').replace('C:', '')),
            (r'\\\\', '/'),
            (r'\\', '/'),
        ]
        
        for old_pattern, replacement in path_conversions:
            if re.search(old_pattern, content):
                if callable(replacement):
                    content = re.sub(old_pattern, replacement, content)
                else:
                    content = re.sub(old_pattern, replacement, content)
                self.conversion_log.append(f"Converted file paths: {old_pattern}")
        
        return content
    
    def clean_comments(self, content):
        """Clean up comments - keep only functional explanations"""
        
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Keep comments that explain functionality
            if line.strip().startswith('#'):
                comment = line.strip()[1:].strip().lower()
                
                # Keep functional comments
                keep_comment = any(keyword in comment for keyword in [
                    'function', 'method', 'class', 'setup', 'initialization',
                    'main', 'loop', 'process', 'handle', 'detect', 'capture',
                    'control', 'configuration', 'parameters', 'variables',
                    'screen', 'mouse', 'keyboard', 'macro', 'fishing',
                    'converted', 'macos', 'implementation', 'helper'
                ])
                
                # Remove generic comments
                remove_comment = any(phrase in comment for phrase in [
                    'todo', 'fixme', 'hack', 'temporary', 'debug',
                    'test', 'example', 'sample', 'placeholder'
                ])
                
                if keep_comment and not remove_comment:
                    cleaned_lines.append(line)
                elif len(comment) > 50:  # Keep longer explanatory comments
                    cleaned_lines.append(line)
            else:
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def fix_common_bugs(self, content):
        """Fix common conversion bugs"""
        
        # Fix import order
        lines = content.split('\n')
        imports = []
        other_lines = []
        
        for line in lines:
            if line.strip().startswith(('import ', 'from ')) and not line.strip().startswith('#'):
                imports.append(line)
            else:
                other_lines.append(line)
        
        # Remove duplicate imports
        unique_imports = []
        seen_imports = set()
        
        for imp in imports:
            if imp.strip() not in seen_imports:
                unique_imports.append(imp)
                seen_imports.add(imp.strip())
        
        content = '\n'.join(unique_imports + [''] + other_lines)
        self.bugs_fixed.append("Fixed import order and removed duplicates")
        
        # Fix indentation issues
        content = re.sub(r'\t', '    ', content)  # Convert tabs to spaces
        self.bugs_fixed.append("Standardized indentation to 4 spaces")
        
        # Fix common syntax issues
        syntax_fixes = [
            (r'print ([^(][^\n]*)', r'print(\1)'),  # Fix print statements
            (r'except ([A-Za-z][A-Za-z0-9_]*), ([a-z])', r'except \1 as \2'),  # Fix except syntax
        ]
        
        for old_pattern, new_pattern in syntax_fixes:
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_pattern, content)
                self.bugs_fixed.append(f"Fixed syntax: {old_pattern}")
        
        return content
    
    def add_macos_optimizations(self, content):
        """Add macOS-specific optimizations"""
        
        # Add Retina display support
        retina_support = '''
# macOS Retina Display Support
def get_display_scale_factor():
    """Get display scale factor for Retina displays"""
    try:
        import Quartz
        display_id = Quartz.CGMainDisplayID()
        mode = Quartz.CGDisplayCopyDisplayMode(display_id)
        if mode:
            pixel_width = Quartz.CGDisplayModeGetPixelWidth(mode)
            width = Quartz.CGDisplayModeGetWidth(mode)
            return pixel_width / width if width > 0 else 1.0
    except:
        pass
    return 1.0

# Apply display scaling
DISPLAY_SCALE = get_display_scale_factor()

'''
        
        # Add performance optimizations
        performance_opts = '''
# macOS Performance Optimizations
import threading
from concurrent.futures import ThreadPoolExecutor

# Thread pool for background tasks
thread_pool = ThreadPoolExecutor(max_workers=2)

def run_in_background(func, *args, **kwargs):
    """Run function in background thread"""
    return thread_pool.submit(func, *args, **kwargs)

'''
        
        content = retina_support + performance_opts + content
        self.conversion_log.append("Added macOS optimizations")
        
        return content
    
    def print_conversion_summary(self):
        """Print summary of conversions performed"""
        
        print("\n" + "="*50)
        print("CONVERSION SUMMARY")
        print("="*50)
        
        print(f"✅ Conversions applied: {len(self.conversion_log)}")
        for conversion in self.conversion_log:
            print(f"  • {conversion}")
        
        print(f"\n🔧 Bugs fixed: {len(self.bugs_fixed)}")
        for bug_fix in self.bugs_fixed:
            print(f"  • {bug_fix}")
        
        print(f"\n🎯 Status: Conversion complete - ready for macOS!")

def convert_fishing_script(input_path, output_path=None):
    """Convert fishing script from Windows to macOS"""
    
    if output_path is None:
        # Generate output filename
        input_file = Path(input_path)
        output_path = input_file.parent / f"{input_file.stem}_macos.py"
    
    converter = EnhancedConverter()
    success = converter.convert_script(input_path, output_path)
    
    if success:
        print(f"\n🎣 Your macOS fishing macro is ready!")
        print(f"📁 Location: {output_path}")
        print(f"🚀 Run with: python3 {output_path}")
    
    return success

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 enhanced_converter.py <input_script.py> [output_script.py]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_fishing_script(input_file, output_file)
