# Quick Start Guide

Get up and running with Python AHK Power GUI in 5 minutes!

## Prerequisites Check

Before you begin, ensure you have:
- [ ] Python 3.8+ installed
- [ ] AutoHotkey installed
- [ ] pip package manager available

## Installation Steps

### Step 1: Install AutoHotkey
1. Visit https://www.autohotkey.com/
2. Download and install AutoHotkey v1.1+
3. Verify installation by running `autohotkey` from command prompt

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed customtkinter-5.2.0 ahk-1.6.0 ...
```

### Step 3: Launch the Application
```bash
python ahk_gui.py
```

The GUI should open with 8 tabs visible.

## First Actions

### 1. Test Mouse Control (30 seconds)
1. Click on "Mouse Control" tab
2. Click "Get Position" button
3. Click "Move Mouse" to move cursor
4. Try clicking buttons for Left Click, Right Click

### 2. Test Keyboard Automation (1 minute)
1. Go to "Keyboard" tab
2. Type some text in the text box
3. Open Notepad on your computer
4. Click in Notepad, then click "Send Text" in the GUI
5. Watch text appear in Notepad

### 3. Create Your First Hotkey (2 minutes)
1. Go to "Hotkeys" tab
2. Enter hotkey: `Ctrl+Shift+H`
3. Select Action: "Send Text"
4. Enter Value: `Hello from Python AHK!`
5. Click "Add Hotkey"
6. Open any text editor and press Ctrl+Shift+H

### 4. Try Window Management (1 minute)
1. Open a few programs (Notepad, Calculator, etc.)
2. Go to "Windows" tab
3. Click "Refresh Windows List"
4. See all your open windows listed
5. Enter a window title and try Minimize/Maximize

### 5. Run a Custom Script (1 minute)
1. Go to "Scripts" tab
2. The editor has a sample script loaded
3. Click "Run Script"
4. Press F1 or F2 to test the script hotkeys

## Common First-Use Issues

### "AHK Not Initialized"
**Fix**: Install AutoHotkey from https://www.autohotkey.com/

### "Module not found: customtkinter"
**Fix**: Run `pip install -r requirements.txt`

### Hotkeys don't work
**Fix**: Ensure no other application is using the same hotkey combination

### Permission errors
**Fix**: Run the application as administrator (Windows: right-click → Run as administrator)

## Quick Feature Overview

### 🎯 Hotkeys Tab
Create custom keyboard shortcuts that trigger actions

### 🖱️ Mouse Control Tab
Automate mouse movements, clicks, drags, and scrolling

### ⌨️ Keyboard Tab
Send text, special keys, and key combinations

### 🪟 Windows Tab
Manage application windows (move, resize, minimize, etc.)

### 🚀 Advanced Tab
Pixel detection, screen capture, process management

### 📝 Scripts Tab
Write and run custom AutoHotkey scripts

### 🎬 Macro Recorder Tab
Record and playback sequences of actions

### 💻 System Tab
System info, volume control, power options

## Example Use Cases

### Use Case 1: Text Expansion
**Goal**: Type `@email` to insert your email address

1. Hotkeys tab
2. Hotkey: Any key combo or leave blank for text expansion
3. Action: Send Text
4. Value: your.email@example.com
5. Add Hotkey

### Use Case 2: Auto-Login
**Goal**: Press F1 to fill login form

1. Scripts tab
2. Paste this script:
```ahk
F1::
    Send, your_username
    Send, {Tab}
    Send, your_password
    Send, {Enter}
return
```
3. Run Script
4. Navigate to login page and press F1

### Use Case 3: Window Organization
**Goal**: Quickly arrange windows side-by-side

1. Windows tab
2. Enter first window title
3. Set position: X=0, Y=0, Width=960, Height=1080
4. Move/Resize Window
5. Repeat for second window with X=960

## Next Steps

- Explore the example scripts in `example_scripts.ahk`
- Read the full README.md for detailed documentation
- Join the community for tips and tricks
- Create custom automation workflows

## Getting Help

- Check README.md for detailed documentation
- Review Troubleshooting section
- Visit GitHub Issues for support
- Read AutoHotkey documentation at https://www.autohotkey.com/docs/

## Tips for Success

1. **Start Simple**: Begin with basic text sending before complex scripts
2. **Test Safely**: Test automation in safe environments (Notepad, etc.)
3. **Save Often**: Save your hotkeys and scripts regularly
4. **Use Delays**: Add Sleep commands in scripts for reliability
5. **Backup**: Keep backups of important automation scripts

---

**You're ready to go! Start automating!** 🚀
