# 🎣 Post-Conversion Guide - How to Run Your macOS Fishing Macro

## ✅ Your Script Has Been Converted!

Congratulations! Your Windows fishing macro has been successfully converted to macOS. Here's everything you need to know to run it.

---

## 📁 What You Now Have

After conversion, you'll find these files in your `output/` folder:

```
output/
├── fishing_macro_macos.py    # 🎯 Your converted macro (MAIN FILE)
├── Config.txt                # ⚙️ Settings and configuration
├── Debug.txt                 # 📝 Error logs and debugging info
└── conversion_report.txt     # 📊 Conversion details and changes made
```

---

## 🚀 How to Run Your Converted Macro

### **Step 1: Navigate to Output Folder**
```bash
cd output/
```

### **Step 2: Test the Macro (Recommended First)**
```bash
# Test all functionality without running the actual macro
python3 fishing_macro_macos.py --test

# Expected output:
✅ Screen capture: Working
✅ Mouse control: Working  
✅ Keyboard detection: Working
✅ All systems ready!
```

### **Step 3: Run the Macro**
```bash
# Standard run
python3 fishing_macro_macos.py

# With custom config
python3 fishing_macro_macos.py --config my_settings.txt

# With debug mode (shows detailed logs)
python3 fishing_macro_macos.py --debug
```

---

## ⚙️ Configuration Guide

### **Editing Settings**
```bash
# Open config file
nano Config.txt

# Or use any text editor
open -a TextEdit Config.txt
```

### **Key Settings to Adjust**

#### **Hotkeys**
```ini
# Start/Stop Controls
START_HOTKEY = f1
STOP_HOTKEY = f2  
PAUSE_HOTKEY = f3
EMERGENCY_STOP = esc
```

#### **Screen Detection**
```ini
# Color Detection Thresholds
RED_THRESHOLD = 180
GREEN_THRESHOLD = 180
BLUE_THRESHOLD = 180
DETECTION_SENSITIVITY = 0.8
```

#### **Timing Settings**
```ini
# Performance Tuning
CAPTURE_RATE = 30          # Screenshots per second
CLICK_DELAY = 0.1          # Delay between clicks (seconds)
REACTION_TIME = 0.05       # Response delay (seconds)
SCAN_INTERVAL = 0.1        # How often to check for fish
```

#### **Screen Regions**
```ini
# Fishing Area (adjust for your screen)
FISHING_X = 100            # Left edge of fishing area
FISHING_Y = 100            # Top edge of fishing area  
FISHING_WIDTH = 800        # Width of fishing area
FISHING_HEIGHT = 600       # Height of fishing area
```

---

## 🎮 Daily Usage Workflow

### **Starting Your Fishing Session**

1. **Open Terminal**
   ```bash
   # Navigate to your macro folder
   cd /path/to/fishing-macro-macos/output/
   ```

2. **Launch the Game**
   - Start your fishing game
   - Position it on screen where the macro expects it
   - Make sure the fishing area is visible

3. **Run the Macro**
   ```bash
   python3 fishing_macro_macos.py
   ```

4. **Use Hotkeys to Control**
   - **F1** - Start fishing
   - **F2** - Stop fishing
   - **F3** - Pause/Resume
   - **ESC** - Emergency stop

### **Monitoring Performance**
```bash
# View real-time logs
tail -f Debug.txt

# Check performance stats
python3 fishing_macro_macos.py --stats

# Monitor system resources
top -pid $(pgrep -f fishing_macro_macos.py)
```

---

## 🔧 Advanced Usage

### **Command Line Options**
```bash
# All available options
python3 fishing_macro_macos.py --help

# Common options:
--test              # Test functionality without running
--debug             # Enable detailed logging
--config FILE       # Use custom config file
--stats             # Show performance statistics
--calibrate         # Run screen calibration wizard
--monitor N         # Use specific monitor (for multi-monitor)
```

### **Multi-Monitor Setup**
```bash
# List available monitors
python3 fishing_macro_macos.py --list-monitors

# Use specific monitor
python3 fishing_macro_macos.py --monitor 2
```

### **Performance Optimization**
```bash
# Run performance analysis
python3 fishing_macro_macos.py --analyze-performance

# Optimize for your system
python3 fishing_macro_macos.py --optimize
```

---

## 🛡️ macOS Permissions Reminder

### **Required Permissions**
Your macro needs these macOS permissions to work:

1. **Screen Recording** - To see the game screen
2. **Accessibility** - To control mouse and keyboard
3. **Input Monitoring** - To detect hotkey presses

### **How to Grant Permissions**
```
1. System Preferences → Security & Privacy
2. Click "Privacy" tab
3. Select "Screen Recording" from left sidebar
4. Click lock icon (🔒) and enter your password
5. Click + button and add Terminal
6. Check the box next to Terminal
7. Repeat steps 3-6 for "Accessibility" and "Input Monitoring"
8. RESTART Terminal (very important!)
```

### **Test Permissions**
```bash
python3 fishing_macro_macos.py --test-permissions

# Expected output:
✅ Screen Recording: Granted
✅ Accessibility: Granted
✅ Input Monitoring: Granted
🎯 All permissions ready!
```

---

## 📊 Understanding the Output

### **Console Messages**
```bash
# Normal operation
🎣 Fishing macro started
🔍 Scanning for fish...
🎯 Fish detected at (450, 300)
🖱️ Casting line...
✅ Fish caught!

# Status messages
⏸️ Macro paused (F3 pressed)
▶️ Macro resumed
🛑 Macro stopped (F2 pressed)
```

### **Debug Log (Debug.txt)**
```
[2025-11-07 15:30:15] INFO: Macro initialized
[2025-11-07 15:30:16] DEBUG: Screen capture rate: 30 FPS
[2025-11-07 15:30:17] INFO: Fish detection active
[2025-11-07 15:30:18] DEBUG: Color match: R=185, G=120, B=95 (threshold: 0.8)
[2025-11-07 15:30:19] INFO: Fish caught successfully
```

---

## 🎯 Calibration Guide

### **Screen Calibration**
```bash
# Run calibration wizard
python3 fishing_macro_macos.py --calibrate

# Follow the prompts:
1. Position your mouse over the fishing area
2. Press SPACE to mark corners
3. Adjust color detection thresholds
4. Test the detection
5. Save settings
```

### **Color Calibration**
```bash
# Interactive color picker
python3 fishing_macro_macos.py --color-picker

# This will help you:
1. Identify the exact colors of fish/bobbers
2. Set optimal detection thresholds
3. Test color matching in real-time
```

---

## ⚡ Performance Tips

### **Optimize for Speed**
```ini
# In Config.txt - High Performance Mode
CAPTURE_RATE = 60          # Higher FPS for faster detection
CLICK_DELAY = 0.05         # Faster clicking
DETECTION_SENSITIVITY = 0.9 # More precise detection
```

### **Optimize for Accuracy**
```ini
# In Config.txt - High Accuracy Mode  
CAPTURE_RATE = 15          # Lower FPS for stability
CLICK_DELAY = 0.2          # Slower, more deliberate clicks
DETECTION_SENSITIVITY = 0.7 # More forgiving detection
```

### **Battery Saving (Laptops)**
```ini
# In Config.txt - Power Saving Mode
CAPTURE_RATE = 10          # Much lower FPS
SCAN_INTERVAL = 0.2        # Less frequent scanning
SLEEP_BETWEEN_SCANS = 0.1  # CPU rest periods
```

---

## 🔄 Updating Your Macro

### **When to Update**
- Game updates change the interface
- You want to adjust detection settings
- Performance needs optimization
- Bug fixes are available

### **How to Update Settings**
```bash
# Backup current config
cp Config.txt Config_backup.txt

# Edit settings
nano Config.txt

# Test changes
python3 fishing_macro_macos.py --test

# If issues occur, restore backup
cp Config_backup.txt Config.txt
```

---

## 🆘 Troubleshooting Quick Fixes

### **Macro Won't Start**
```bash
# Check permissions
python3 fishing_macro_macos.py --test-permissions

# Check packages
python3 -c "import PIL, numpy, cv2, pynput, Quartz; print('All packages OK')"

# Check script syntax
python3 -m py_compile fishing_macro_macos.py
```

### **Poor Detection**
```bash
# Recalibrate colors
python3 fishing_macro_macos.py --calibrate

# Check screen region
python3 fishing_macro_macos.py --show-region

# Adjust sensitivity in Config.txt
DETECTION_SENSITIVITY = 0.6  # Lower = more forgiving
```

### **Performance Issues**
```bash
# Check system resources
python3 fishing_macro_macos.py --stats

# Reduce capture rate
# Edit Config.txt: CAPTURE_RATE = 15

# Close other applications
```

---

## 📱 Getting Help

### **Built-in Help**
```bash
# Show all options
python3 fishing_macro_macos.py --help

# Show current settings
python3 fishing_macro_macos.py --show-config

# Run diagnostics
python3 fishing_macro_macos.py --diagnose
```

### **Log Analysis**
```bash
# View recent errors
tail -20 Debug.txt

# Search for specific issues
grep "ERROR" Debug.txt
grep "WARNING" Debug.txt
```

### **Performance Analysis**
```bash
# Detailed performance report
python3 fishing_macro_macos.py --performance-report

# This shows:
# - Average FPS
# - Detection accuracy
# - Response times
# - Resource usage
```

---

## 🎊 Success Tips

### **For Best Results**
1. **Stable lighting** - Avoid changing screen brightness
2. **Consistent positioning** - Keep game window in same place
3. **Clean background** - Minimize visual distractions
4. **Regular calibration** - Recalibrate after game updates
5. **Monitor performance** - Check Debug.txt occasionally

### **Common Success Patterns**
```ini
# Settings that work well for most users:
CAPTURE_RATE = 30
DETECTION_SENSITIVITY = 0.75
CLICK_DELAY = 0.1
REACTION_TIME = 0.05
```

---

## 🎯 You're Ready to Fish!

Your converted macro is now ready for macOS. Remember:

✅ **Test first** - Always run `--test` before fishing  
✅ **Check permissions** - Ensure all macOS permissions are granted  
✅ **Monitor logs** - Keep an eye on Debug.txt for issues  
✅ **Calibrate regularly** - Adjust settings as needed  
✅ **Have fun!** - Enjoy automated fishing on macOS  

**Happy fishing!** 🎣
