"""
Python AHK GUI - A comprehensive AutoHotkey interface powered by Python
Author: Claude
Description: Dynamic GUI that flexes the power of Python with full AHK integration
"""

import customtkinter as ctk
from ahk import AHK
import threading
import time
import json
import os
from datetime import datetime
from tkinter import messagebox, scrolledtext
import pyperclip
from PIL import Image, ImageGrab
import psutil

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PythonAHKGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize AHK
        try:
            self.ahk = AHK()
        except Exception as e:
            messagebox.showerror("AHK Error", f"Failed to initialize AutoHotkey: {str(e)}\n\nPlease ensure AutoHotkey is installed.")
            self.ahk = None

        # Configure window
        self.title("Python AHK Power GUI")
        self.geometry("1200x800")

        # Variables
        self.hotkeys = {}
        self.running_scripts = []
        self.recorded_actions = []
        self.is_recording = False

        # Create UI
        self.create_widgets()

        # Load saved hotkeys
        self.load_hotkeys()

    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create tabview
        self.tabview = ctk.CTkTabview(self, width=1180, height=780)
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Add tabs
        self.tab_hotkeys = self.tabview.add("Hotkeys")
        self.tab_mouse = self.tabview.add("Mouse Control")
        self.tab_keyboard = self.tabview.add("Keyboard")
        self.tab_windows = self.tabview.add("Windows")
        self.tab_advanced = self.tabview.add("Advanced")
        self.tab_scripts = self.tabview.add("Scripts")
        self.tab_recorder = self.tabview.add("Macro Recorder")
        self.tab_system = self.tabview.add("System")

        # Setup each tab
        self.setup_hotkeys_tab()
        self.setup_mouse_tab()
        self.setup_keyboard_tab()
        self.setup_windows_tab()
        self.setup_advanced_tab()
        self.setup_scripts_tab()
        self.setup_recorder_tab()
        self.setup_system_tab()

    def setup_hotkeys_tab(self):
        """Setup hotkeys management tab"""
        # Title
        title = ctk.CTkLabel(self.tab_hotkeys, text="Hotkey Management",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Input frame
        input_frame = ctk.CTkFrame(self.tab_hotkeys)
        input_frame.pack(pady=10, padx=20, fill="x")

        # Hotkey input
        ctk.CTkLabel(input_frame, text="Hotkey:").grid(row=0, column=0, padx=5, pady=5)
        self.hotkey_input = ctk.CTkEntry(input_frame, width=200,
                                         placeholder_text="e.g., Ctrl+Shift+A")
        self.hotkey_input.grid(row=0, column=1, padx=5, pady=5)

        # Action type
        ctk.CTkLabel(input_frame, text="Action:").grid(row=0, column=2, padx=5, pady=5)
        self.hotkey_action = ctk.CTkComboBox(input_frame, width=150,
                                             values=["Send Text", "Run Script", "Mouse Click",
                                                    "Open Program", "Custom AHK"])
        self.hotkey_action.grid(row=0, column=3, padx=5, pady=5)

        # Action value
        ctk.CTkLabel(input_frame, text="Value:").grid(row=1, column=0, padx=5, pady=5)
        self.hotkey_value = ctk.CTkEntry(input_frame, width=400,
                                         placeholder_text="Action value...")
        self.hotkey_value.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Buttons
        btn_frame = ctk.CTkFrame(self.tab_hotkeys)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Add Hotkey", command=self.add_hotkey,
                     fg_color="green", hover_color="darkgreen").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Remove Selected", command=self.remove_hotkey,
                     fg_color="red", hover_color="darkred").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Clear All", command=self.clear_hotkeys,
                     fg_color="orange", hover_color="darkorange").pack(side="left", padx=5)

        # Hotkeys list
        list_frame = ctk.CTkFrame(self.tab_hotkeys)
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(list_frame, text="Active Hotkeys:",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.hotkeys_listbox = ctk.CTkTextbox(list_frame, height=300)
        self.hotkeys_listbox.pack(fill="both", expand=True, padx=10, pady=10)

    def setup_mouse_tab(self):
        """Setup mouse control tab"""
        title = ctk.CTkLabel(self.tab_mouse, text="Mouse Automation",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Position frame
        pos_frame = ctk.CTkFrame(self.tab_mouse)
        pos_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(pos_frame, text="Mouse Position Control",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        coord_frame = ctk.CTkFrame(pos_frame)
        coord_frame.pack(pady=5)

        ctk.CTkLabel(coord_frame, text="X:").pack(side="left", padx=5)
        self.mouse_x = ctk.CTkEntry(coord_frame, width=100)
        self.mouse_x.pack(side="left", padx=5)

        ctk.CTkLabel(coord_frame, text="Y:").pack(side="left", padx=5)
        self.mouse_y = ctk.CTkEntry(coord_frame, width=100)
        self.mouse_y.pack(side="left", padx=5)

        ctk.CTkButton(coord_frame, text="Get Position",
                     command=self.get_mouse_position).pack(side="left", padx=5)
        ctk.CTkButton(coord_frame, text="Move Mouse",
                     command=self.move_mouse).pack(side="left", padx=5)

        # Click frame
        click_frame = ctk.CTkFrame(self.tab_mouse)
        click_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(click_frame, text="Mouse Clicks",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        btn_frame = ctk.CTkFrame(click_frame)
        btn_frame.pack(pady=5)

        ctk.CTkButton(btn_frame, text="Left Click",
                     command=lambda: self.mouse_click("left")).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Right Click",
                     command=lambda: self.mouse_click("right")).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Middle Click",
                     command=lambda: self.mouse_click("middle")).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Double Click",
                     command=lambda: self.mouse_click("left", 2)).pack(side="left", padx=5)

        # Advanced mouse
        adv_frame = ctk.CTkFrame(self.tab_mouse)
        adv_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(adv_frame, text="Advanced Mouse Actions",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        # Drag and drop
        drag_frame = ctk.CTkFrame(adv_frame)
        drag_frame.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(drag_frame, text="Drag from X:").pack(side="left", padx=5)
        self.drag_x1 = ctk.CTkEntry(drag_frame, width=80)
        self.drag_x1.pack(side="left", padx=5)

        ctk.CTkLabel(drag_frame, text="Y:").pack(side="left", padx=5)
        self.drag_y1 = ctk.CTkEntry(drag_frame, width=80)
        self.drag_y1.pack(side="left", padx=5)

        ctk.CTkLabel(drag_frame, text="to X:").pack(side="left", padx=5)
        self.drag_x2 = ctk.CTkEntry(drag_frame, width=80)
        self.drag_x2.pack(side="left", padx=5)

        ctk.CTkLabel(drag_frame, text="Y:").pack(side="left", padx=5)
        self.drag_y2 = ctk.CTkEntry(drag_frame, width=80)
        self.drag_y2.pack(side="left", padx=5)

        ctk.CTkButton(drag_frame, text="Drag", command=self.mouse_drag).pack(side="left", padx=5)

        # Mouse wheel
        wheel_frame = ctk.CTkFrame(adv_frame)
        wheel_frame.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(wheel_frame, text="Scroll Amount:").pack(side="left", padx=5)
        self.scroll_amount = ctk.CTkEntry(wheel_frame, width=100)
        self.scroll_amount.insert(0, "3")
        self.scroll_amount.pack(side="left", padx=5)

        ctk.CTkButton(wheel_frame, text="Scroll Up",
                     command=lambda: self.mouse_wheel("up")).pack(side="left", padx=5)
        ctk.CTkButton(wheel_frame, text="Scroll Down",
                     command=lambda: self.mouse_wheel("down")).pack(side="left", padx=5)

        # Status
        self.mouse_status = ctk.CTkTextbox(adv_frame, height=100)
        self.mouse_status.pack(pady=10, padx=10, fill="both", expand=True)

    def setup_keyboard_tab(self):
        """Setup keyboard automation tab"""
        title = ctk.CTkLabel(self.tab_keyboard, text="Keyboard Automation",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Send text
        text_frame = ctk.CTkFrame(self.tab_keyboard)
        text_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(text_frame, text="Send Text",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.text_to_send = ctk.CTkTextbox(text_frame, height=100)
        self.text_to_send.pack(pady=5, padx=10, fill="x")

        btn_frame = ctk.CTkFrame(text_frame)
        btn_frame.pack(pady=5)

        ctk.CTkLabel(btn_frame, text="Delay (ms):").pack(side="left", padx=5)
        self.type_delay = ctk.CTkEntry(btn_frame, width=100)
        self.type_delay.insert(0, "50")
        self.type_delay.pack(side="left", padx=5)

        ctk.CTkButton(btn_frame, text="Send Text",
                     command=self.send_text).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Send Raw",
                     command=self.send_raw_text).pack(side="left", padx=5)

        # Send keys
        keys_frame = ctk.CTkFrame(self.tab_keyboard)
        keys_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(keys_frame, text="Send Special Keys",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        special_frame = ctk.CTkFrame(keys_frame)
        special_frame.pack(pady=5)

        keys = ["Enter", "Tab", "Escape", "Backspace", "Delete", "Space",
                "Up", "Down", "Left", "Right", "Home", "End", "PageUp", "PageDown"]

        for i, key in enumerate(keys):
            row = i // 7
            col = i % 7
            ctk.CTkButton(special_frame, text=key, width=100,
                         command=lambda k=key: self.send_key(k)).grid(row=row, column=col, padx=3, pady=3)

        # Modifier keys
        mod_frame = ctk.CTkFrame(self.tab_keyboard)
        mod_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(mod_frame, text="Modifier Combinations",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        combo_frame = ctk.CTkFrame(mod_frame)
        combo_frame.pack(pady=5)

        ctk.CTkLabel(combo_frame, text="Key Combo:").pack(side="left", padx=5)
        self.key_combo = ctk.CTkEntry(combo_frame, width=200,
                                      placeholder_text="e.g., Ctrl+C, Alt+Tab")
        self.key_combo.pack(side="left", padx=5)
        ctk.CTkButton(combo_frame, text="Send Combo",
                     command=self.send_combo).pack(side="left", padx=5)

        # Clipboard
        clip_frame = ctk.CTkFrame(self.tab_keyboard)
        clip_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(clip_frame, text="Clipboard Operations",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.clipboard_text = ctk.CTkTextbox(clip_frame, height=150)
        self.clipboard_text.pack(pady=5, padx=10, fill="both", expand=True)

        clip_btn_frame = ctk.CTkFrame(clip_frame)
        clip_btn_frame.pack(pady=5)

        ctk.CTkButton(clip_btn_frame, text="Get Clipboard",
                     command=self.get_clipboard).pack(side="left", padx=5)
        ctk.CTkButton(clip_btn_frame, text="Set Clipboard",
                     command=self.set_clipboard).pack(side="left", padx=5)
        ctk.CTkButton(clip_btn_frame, text="Clear Clipboard",
                     command=self.clear_clipboard).pack(side="left", padx=5)

    def setup_windows_tab(self):
        """Setup window management tab"""
        title = ctk.CTkLabel(self.tab_windows, text="Window Management",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Window list
        list_frame = ctk.CTkFrame(self.tab_windows)
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(list_frame, text="Active Windows",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.windows_list = ctk.CTkTextbox(list_frame, height=200)
        self.windows_list.pack(pady=5, padx=10, fill="both", expand=True)

        ctk.CTkButton(list_frame, text="Refresh Windows List",
                     command=self.refresh_windows).pack(pady=5)

        # Window operations
        ops_frame = ctk.CTkFrame(self.tab_windows)
        ops_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(ops_frame, text="Window Operations",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        title_frame = ctk.CTkFrame(ops_frame)
        title_frame.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(title_frame, text="Window Title:").pack(side="left", padx=5)
        self.window_title = ctk.CTkEntry(title_frame, width=300)
        self.window_title.pack(side="left", padx=5)

        btn_frame = ctk.CTkFrame(ops_frame)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Activate",
                     command=self.activate_window).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Minimize",
                     command=self.minimize_window).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Maximize",
                     command=self.maximize_window).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Close",
                     command=self.close_window).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Hide",
                     command=self.hide_window).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Show",
                     command=self.show_window).pack(side="left", padx=5)

        # Window positioning
        pos_frame = ctk.CTkFrame(self.tab_windows)
        pos_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(pos_frame, text="Window Position & Size",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        coord_frame = ctk.CTkFrame(pos_frame)
        coord_frame.pack(pady=5)

        ctk.CTkLabel(coord_frame, text="X:").pack(side="left", padx=5)
        self.win_x = ctk.CTkEntry(coord_frame, width=80)
        self.win_x.pack(side="left", padx=5)

        ctk.CTkLabel(coord_frame, text="Y:").pack(side="left", padx=5)
        self.win_y = ctk.CTkEntry(coord_frame, width=80)
        self.win_y.pack(side="left", padx=5)

        ctk.CTkLabel(coord_frame, text="Width:").pack(side="left", padx=5)
        self.win_width = ctk.CTkEntry(coord_frame, width=80)
        self.win_width.pack(side="left", padx=5)

        ctk.CTkLabel(coord_frame, text="Height:").pack(side="left", padx=5)
        self.win_height = ctk.CTkEntry(coord_frame, width=80)
        self.win_height.pack(side="left", padx=5)

        ctk.CTkButton(coord_frame, text="Move/Resize Window",
                     command=self.move_resize_window).pack(side="left", padx=5)

    def setup_advanced_tab(self):
        """Setup advanced AHK features tab"""
        title = ctk.CTkLabel(self.tab_advanced, text="Advanced Features",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Image search
        img_frame = ctk.CTkFrame(self.tab_advanced)
        img_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(img_frame, text="Image Search",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        img_input_frame = ctk.CTkFrame(img_frame)
        img_input_frame.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(img_input_frame, text="Image Path:").pack(side="left", padx=5)
        self.image_path = ctk.CTkEntry(img_input_frame, width=300)
        self.image_path.pack(side="left", padx=5)
        ctk.CTkButton(img_input_frame, text="Search Screen",
                     command=self.image_search).pack(side="left", padx=5)

        # Pixel color detection
        pixel_frame = ctk.CTkFrame(self.tab_advanced)
        pixel_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(pixel_frame, text="Pixel Color Detection",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        pixel_input_frame = ctk.CTkFrame(pixel_frame)
        pixel_input_frame.pack(pady=5)

        ctk.CTkLabel(pixel_input_frame, text="X:").pack(side="left", padx=5)
        self.pixel_x = ctk.CTkEntry(pixel_input_frame, width=100)
        self.pixel_x.pack(side="left", padx=5)

        ctk.CTkLabel(pixel_input_frame, text="Y:").pack(side="left", padx=5)
        self.pixel_y = ctk.CTkEntry(pixel_input_frame, width=100)
        self.pixel_y.pack(side="left", padx=5)

        ctk.CTkButton(pixel_input_frame, text="Get Pixel Color",
                     command=self.get_pixel_color).pack(side="left", padx=5)

        self.pixel_result = ctk.CTkLabel(pixel_frame, text="Color: ",
                                         font=ctk.CTkFont(size=12))
        self.pixel_result.pack(pady=5)

        # Screen capture
        capture_frame = ctk.CTkFrame(self.tab_advanced)
        capture_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(capture_frame, text="Screen Capture",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        capture_btn_frame = ctk.CTkFrame(capture_frame)
        capture_btn_frame.pack(pady=5)

        ctk.CTkLabel(capture_btn_frame, text="Save to:").pack(side="left", padx=5)
        self.screenshot_path = ctk.CTkEntry(capture_btn_frame, width=250)
        self.screenshot_path.insert(0, "screenshot.png")
        self.screenshot_path.pack(side="left", padx=5)

        ctk.CTkButton(capture_btn_frame, text="Capture Screen",
                     command=self.capture_screen).pack(side="left", padx=5)

        # Process management
        process_frame = ctk.CTkFrame(self.tab_advanced)
        process_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(process_frame, text="Process Management",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        proc_input_frame = ctk.CTkFrame(process_frame)
        proc_input_frame.pack(pady=5)

        ctk.CTkLabel(proc_input_frame, text="Process Name:").pack(side="left", padx=5)
        self.process_name = ctk.CTkEntry(proc_input_frame, width=200)
        self.process_name.pack(side="left", padx=5)

        ctk.CTkButton(proc_input_frame, text="Check Process",
                     command=self.check_process).pack(side="left", padx=5)
        ctk.CTkButton(proc_input_frame, text="List All Processes",
                     command=self.list_processes).pack(side="left", padx=5)

        self.process_output = ctk.CTkTextbox(process_frame, height=150)
        self.process_output.pack(pady=5, padx=10, fill="both", expand=True)

    def setup_scripts_tab(self):
        """Setup AHK scripts tab"""
        title = ctk.CTkLabel(self.tab_scripts, text="Custom AHK Scripts",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Script editor
        editor_frame = ctk.CTkFrame(self.tab_scripts)
        editor_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(editor_frame, text="Script Editor",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.script_editor = ctk.CTkTextbox(editor_frame, height=400)
        self.script_editor.pack(pady=5, padx=10, fill="both", expand=True)

        # Sample script
        sample_script = """#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; Sample AHK Script
; Press F1 to show a message box
F1::
    MsgBox, Hello from AHK!
return

; Press F2 to type some text
F2::
    Send, This is automated text!
return

; Press Ctrl+Alt+S to save something
^!s::
    MsgBox, Save hotkey triggered!
return
"""
        self.script_editor.insert("1.0", sample_script)

        # Buttons
        btn_frame = ctk.CTkFrame(self.tab_scripts)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Run Script", command=self.run_ahk_script,
                     fg_color="green", hover_color="darkgreen").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Stop All Scripts", command=self.stop_all_scripts,
                     fg_color="red", hover_color="darkred").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Save Script", command=self.save_script).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Load Script", command=self.load_script).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Clear", command=lambda: self.script_editor.delete("1.0", "end")).pack(side="left", padx=5)

        # Output
        output_frame = ctk.CTkFrame(self.tab_scripts)
        output_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(output_frame, text="Script Output",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.script_output = ctk.CTkTextbox(output_frame, height=100)
        self.script_output.pack(pady=5, padx=10, fill="x")

    def setup_recorder_tab(self):
        """Setup macro recorder tab"""
        title = ctk.CTkLabel(self.tab_recorder, text="Macro Recorder",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # Recording controls
        control_frame = ctk.CTkFrame(self.tab_recorder)
        control_frame.pack(pady=10, padx=20, fill="x")

        self.record_btn = ctk.CTkButton(control_frame, text="Start Recording",
                                       command=self.toggle_recording,
                                       fg_color="green", hover_color="darkgreen")
        self.record_btn.pack(side="left", padx=5, pady=10)

        ctk.CTkButton(control_frame, text="Playback",
                     command=self.playback_macro,
                     fg_color="blue", hover_color="darkblue").pack(side="left", padx=5, pady=10)

        ctk.CTkButton(control_frame, text="Clear Recording",
                     command=self.clear_recording,
                     fg_color="orange", hover_color="darkorange").pack(side="left", padx=5, pady=10)

        ctk.CTkButton(control_frame, text="Save Macro",
                     command=self.save_macro).pack(side="left", padx=5, pady=10)

        ctk.CTkButton(control_frame, text="Load Macro",
                     command=self.load_macro).pack(side="left", padx=5, pady=10)

        # Options
        options_frame = ctk.CTkFrame(self.tab_recorder)
        options_frame.pack(pady=10, padx=20, fill="x")

        self.record_mouse = ctk.CTkCheckBox(options_frame, text="Record Mouse Movements")
        self.record_mouse.pack(side="left", padx=10)
        self.record_mouse.select()

        self.record_clicks = ctk.CTkCheckBox(options_frame, text="Record Mouse Clicks")
        self.record_clicks.pack(side="left", padx=10)
        self.record_clicks.select()

        self.record_keyboard = ctk.CTkCheckBox(options_frame, text="Record Keyboard")
        self.record_keyboard.pack(side="left", padx=10)
        self.record_keyboard.select()

        # Recorded actions display
        display_frame = ctk.CTkFrame(self.tab_recorder)
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(display_frame, text="Recorded Actions",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.recorded_display = ctk.CTkTextbox(display_frame, height=400)
        self.recorded_display.pack(pady=5, padx=10, fill="both", expand=True)

        # Status
        self.record_status = ctk.CTkLabel(self.tab_recorder, text="Status: Not Recording",
                                         font=ctk.CTkFont(size=12))
        self.record_status.pack(pady=5)

    def setup_system_tab(self):
        """Setup system information and control tab"""
        title = ctk.CTkLabel(self.tab_system, text="System Information & Control",
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        # System info
        info_frame = ctk.CTkFrame(self.tab_system)
        info_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(info_frame, text="System Information",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        self.system_info = ctk.CTkTextbox(info_frame, height=200)
        self.system_info.pack(pady=5, padx=10, fill="both", expand=True)

        ctk.CTkButton(info_frame, text="Refresh System Info",
                     command=self.refresh_system_info).pack(pady=5)

        # Sound controls
        sound_frame = ctk.CTkFrame(self.tab_system)
        sound_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(sound_frame, text="Sound Controls",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        sound_btn_frame = ctk.CTkFrame(sound_frame)
        sound_btn_frame.pack(pady=5)

        ctk.CTkButton(sound_btn_frame, text="Volume Up",
                     command=lambda: self.adjust_volume("up")).pack(side="left", padx=5)
        ctk.CTkButton(sound_btn_frame, text="Volume Down",
                     command=lambda: self.adjust_volume("down")).pack(side="left", padx=5)
        ctk.CTkButton(sound_btn_frame, text="Mute",
                     command=lambda: self.adjust_volume("mute")).pack(side="left", padx=5)

        # Power options
        power_frame = ctk.CTkFrame(self.tab_system)
        power_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(power_frame, text="⚠️ Power Options (Use with Caution)",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color="orange").pack(pady=5)

        power_btn_frame = ctk.CTkFrame(power_frame)
        power_btn_frame.pack(pady=5)

        ctk.CTkButton(power_btn_frame, text="Lock Screen",
                     command=self.lock_screen).pack(side="left", padx=5)
        ctk.CTkButton(power_btn_frame, text="Log Off",
                     command=self.confirm_logoff,
                     fg_color="orange", hover_color="darkorange").pack(side="left", padx=5)
        ctk.CTkButton(power_btn_frame, text="Shutdown",
                     command=self.confirm_shutdown,
                     fg_color="red", hover_color="darkred").pack(side="left", padx=5)
        ctk.CTkButton(power_btn_frame, text="Restart",
                     command=self.confirm_restart,
                     fg_color="red", hover_color="darkred").pack(side="left", padx=5)

        # Initialize system info
        self.refresh_system_info()

    # ===== Hotkey Methods =====

    def add_hotkey(self):
        """Add a new hotkey"""
        hotkey = self.hotkey_input.get().strip()
        action = self.hotkey_action.get()
        value = self.hotkey_value.get().strip()

        if not hotkey or not value:
            messagebox.showwarning("Input Error", "Please enter both hotkey and value")
            return

        if not self.ahk:
            messagebox.showerror("AHK Error", "AutoHotkey not initialized")
            return

        try:
            self.hotkeys[hotkey] = {"action": action, "value": value}
            self.update_hotkeys_display()
            self.save_hotkeys()
            messagebox.showinfo("Success", f"Hotkey '{hotkey}' added successfully!")

            # Clear inputs
            self.hotkey_input.delete(0, "end")
            self.hotkey_value.delete(0, "end")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add hotkey: {str(e)}")

    def remove_hotkey(self):
        """Remove selected hotkey"""
        # This is a simplified version - you'd need to track selection
        messagebox.showinfo("Info", "Select a hotkey from the list and click Remove")

    def clear_hotkeys(self):
        """Clear all hotkeys"""
        if messagebox.askyesno("Confirm", "Clear all hotkeys?"):
            self.hotkeys.clear()
            self.update_hotkeys_display()
            self.save_hotkeys()

    def update_hotkeys_display(self):
        """Update the hotkeys list display"""
        self.hotkeys_listbox.delete("1.0", "end")
        for hotkey, data in self.hotkeys.items():
            self.hotkeys_listbox.insert("end",
                f"{hotkey} → {data['action']}: {data['value']}\n")

    def save_hotkeys(self):
        """Save hotkeys to file"""
        try:
            with open("hotkeys.json", "w") as f:
                json.dump(self.hotkeys, f, indent=2)
        except Exception as e:
            print(f"Error saving hotkeys: {e}")

    def load_hotkeys(self):
        """Load hotkeys from file"""
        try:
            if os.path.exists("hotkeys.json"):
                with open("hotkeys.json", "r") as f:
                    self.hotkeys = json.load(f)
                self.update_hotkeys_display()
        except Exception as e:
            print(f"Error loading hotkeys: {e}")

    # ===== Mouse Methods =====

    def get_mouse_position(self):
        """Get current mouse position"""
        if not self.ahk:
            return
        try:
            pos = self.ahk.mouse_position
            self.mouse_x.delete(0, "end")
            self.mouse_x.insert(0, str(pos[0]))
            self.mouse_y.delete(0, "end")
            self.mouse_y.insert(0, str(pos[1]))
            self.update_mouse_status(f"Current position: X={pos[0]}, Y={pos[1]}")
        except Exception as e:
            self.update_mouse_status(f"Error: {str(e)}")

    def move_mouse(self):
        """Move mouse to specified position"""
        if not self.ahk:
            return
        try:
            x = int(self.mouse_x.get())
            y = int(self.mouse_y.get())
            self.ahk.mouse_move(x, y)
            self.update_mouse_status(f"Moved mouse to X={x}, Y={y}")
        except ValueError:
            self.update_mouse_status("Error: Invalid coordinates")
        except Exception as e:
            self.update_mouse_status(f"Error: {str(e)}")

    def mouse_click(self, button="left", clicks=1):
        """Perform mouse click"""
        if not self.ahk:
            return
        try:
            for _ in range(clicks):
                self.ahk.click(button=button)
                time.sleep(0.1)
            self.update_mouse_status(f"{button.capitalize()} clicked {clicks} time(s)")
        except Exception as e:
            self.update_mouse_status(f"Error: {str(e)}")

    def mouse_drag(self):
        """Drag mouse from one position to another"""
        if not self.ahk:
            return
        try:
            x1 = int(self.drag_x1.get())
            y1 = int(self.drag_y1.get())
            x2 = int(self.drag_x2.get())
            y2 = int(self.drag_y2.get())

            self.ahk.mouse_move(x1, y1)
            time.sleep(0.1)
            self.ahk.mouse_drag(x2, y2)
            self.update_mouse_status(f"Dragged from ({x1},{y1}) to ({x2},{y2})")
        except ValueError:
            self.update_mouse_status("Error: Invalid coordinates")
        except Exception as e:
            self.update_mouse_status(f"Error: {str(e)}")

    def mouse_wheel(self, direction):
        """Scroll mouse wheel"""
        if not self.ahk:
            return
        try:
            amount = int(self.scroll_amount.get())
            if direction == "down":
                amount = -amount
            self.ahk.wheel_down(abs(amount)) if direction == "down" else self.ahk.wheel_up(amount)
            self.update_mouse_status(f"Scrolled {direction} by {abs(amount)}")
        except ValueError:
            self.update_mouse_status("Error: Invalid scroll amount")
        except Exception as e:
            self.update_mouse_status(f"Error: {str(e)}")

    def update_mouse_status(self, message):
        """Update mouse status display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.mouse_status.insert("end", f"[{timestamp}] {message}\n")
        self.mouse_status.see("end")

    # ===== Keyboard Methods =====

    def send_text(self):
        """Send text with typing"""
        if not self.ahk:
            return
        try:
            text = self.text_to_send.get("1.0", "end-1c")
            delay = int(self.type_delay.get())

            def type_text():
                for char in text:
                    self.ahk.type(char)
                    time.sleep(delay / 1000.0)

            thread = threading.Thread(target=type_text)
            thread.daemon = True
            thread.start()

            messagebox.showinfo("Success", "Typing started...")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send text: {str(e)}")

    def send_raw_text(self):
        """Send text instantly"""
        if not self.ahk:
            return
        try:
            text = self.text_to_send.get("1.0", "end-1c")
            self.ahk.type(text)
            messagebox.showinfo("Success", "Text sent!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send text: {str(e)}")

    def send_key(self, key):
        """Send a special key"""
        if not self.ahk:
            return
        try:
            self.ahk.send(f"{{{key}}}")
            messagebox.showinfo("Success", f"'{key}' key sent!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send key: {str(e)}")

    def send_combo(self):
        """Send key combination"""
        if not self.ahk:
            return
        try:
            combo = self.key_combo.get().strip()
            if not combo:
                return

            # Convert common notation to AHK format
            combo = combo.replace("Ctrl", "^").replace("Alt", "!").replace("Shift", "+").replace("Win", "#")
            self.ahk.send(combo)
            messagebox.showinfo("Success", f"Combo '{combo}' sent!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send combo: {str(e)}")

    def get_clipboard(self):
        """Get clipboard content"""
        try:
            content = pyperclip.paste()
            self.clipboard_text.delete("1.0", "end")
            self.clipboard_text.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get clipboard: {str(e)}")

    def set_clipboard(self):
        """Set clipboard content"""
        try:
            content = self.clipboard_text.get("1.0", "end-1c")
            pyperclip.copy(content)
            messagebox.showinfo("Success", "Clipboard updated!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to set clipboard: {str(e)}")

    def clear_clipboard(self):
        """Clear clipboard"""
        try:
            pyperclip.copy("")
            self.clipboard_text.delete("1.0", "end")
            messagebox.showinfo("Success", "Clipboard cleared!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear clipboard: {str(e)}")

    # ===== Window Methods =====

    def refresh_windows(self):
        """Refresh the list of windows"""
        if not self.ahk:
            return
        try:
            windows = self.ahk.windows()
            self.windows_list.delete("1.0", "end")
            for i, win in enumerate(windows[:50], 1):  # Limit to 50 windows
                try:
                    title = win.title
                    if title:
                        self.windows_list.insert("end", f"{i}. {title}\n")
                except:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh windows: {str(e)}")

    def activate_window(self):
        """Activate window by title"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            if not title:
                return
            win = self.ahk.find_window(title=title)
            if win:
                win.activate()
                messagebox.showinfo("Success", f"Window '{title}' activated!")
            else:
                messagebox.showwarning("Not Found", f"Window '{title}' not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to activate window: {str(e)}")

    def minimize_window(self):
        """Minimize window"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            win = self.ahk.find_window(title=title)
            if win:
                win.minimize()
                messagebox.showinfo("Success", f"Window minimized!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to minimize: {str(e)}")

    def maximize_window(self):
        """Maximize window"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            win = self.ahk.find_window(title=title)
            if win:
                win.maximize()
                messagebox.showinfo("Success", f"Window maximized!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to maximize: {str(e)}")

    def close_window(self):
        """Close window"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            if messagebox.askyesno("Confirm", f"Close window '{title}'?"):
                win = self.ahk.find_window(title=title)
                if win:
                    win.close()
                    messagebox.showinfo("Success", f"Window closed!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to close window: {str(e)}")

    def hide_window(self):
        """Hide window"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            win = self.ahk.find_window(title=title)
            if win:
                win.hide()
                messagebox.showinfo("Success", f"Window hidden!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to hide window: {str(e)}")

    def show_window(self):
        """Show window"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            win = self.ahk.find_window(title=title)
            if win:
                win.show()
                messagebox.showinfo("Success", f"Window shown!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show window: {str(e)}")

    def move_resize_window(self):
        """Move and resize window"""
        if not self.ahk:
            return
        try:
            title = self.window_title.get().strip()
            x = int(self.win_x.get())
            y = int(self.win_y.get())
            width = int(self.win_width.get())
            height = int(self.win_height.get())

            win = self.ahk.find_window(title=title)
            if win:
                win.move(x, y, width, height)
                messagebox.showinfo("Success", f"Window moved/resized!")
        except ValueError:
            messagebox.showerror("Error", "Invalid coordinates or dimensions")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to move/resize: {str(e)}")

    # ===== Advanced Methods =====

    def image_search(self):
        """Search for image on screen"""
        messagebox.showinfo("Info", "Image search requires additional setup with computer vision libraries")

    def get_pixel_color(self):
        """Get pixel color at coordinates"""
        try:
            x = int(self.pixel_x.get())
            y = int(self.pixel_y.get())

            screenshot = ImageGrab.grab()
            pixel = screenshot.getpixel((x, y))

            hex_color = '#{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])
            self.pixel_result.configure(text=f"Color: RGB{pixel} = {hex_color}")

        except ValueError:
            messagebox.showerror("Error", "Invalid coordinates")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get pixel: {str(e)}")

    def capture_screen(self):
        """Capture screenshot"""
        try:
            path = self.screenshot_path.get().strip()
            if not path:
                path = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

            screenshot = ImageGrab.grab()
            screenshot.save(path)
            messagebox.showinfo("Success", f"Screenshot saved to {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to capture: {str(e)}")

    def check_process(self):
        """Check if process is running"""
        try:
            name = self.process_name.get().strip()
            if not name:
                return

            found = False
            for proc in psutil.process_iter(['name']):
                if proc.info['name'].lower() == name.lower():
                    found = True
                    break

            result = f"Process '{name}' is {'RUNNING' if found else 'NOT RUNNING'}"
            self.process_output.delete("1.0", "end")
            self.process_output.insert("1.0", result)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to check process: {str(e)}")

    def list_processes(self):
        """List all running processes"""
        try:
            self.process_output.delete("1.0", "end")
            self.process_output.insert("1.0", "Running Processes:\n\n")

            processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    processes.append(f"PID {proc.info['pid']}: {proc.info['name']}")
                except:
                    pass

            for proc in sorted(processes)[:100]:  # Limit to 100
                self.process_output.insert("end", proc + "\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to list processes: {str(e)}")

    # ===== Script Methods =====

    def run_ahk_script(self):
        """Run AHK script"""
        if not self.ahk:
            return
        try:
            script = self.script_editor.get("1.0", "end-1c")
            if not script.strip():
                messagebox.showwarning("Warning", "No script to run")
                return

            # Save and run script
            with open("temp_script.ahk", "w") as f:
                f.write(script)

            result = self.ahk.run_script(script)
            self.script_output.delete("1.0", "end")
            self.script_output.insert("1.0", f"Script started at {datetime.now().strftime('%H:%M:%S')}\n")
            self.script_output.insert("end", "Check AutoHotkey system tray icon for running scripts")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to run script: {str(e)}")

    def stop_all_scripts(self):
        """Stop all running AHK scripts"""
        if messagebox.askyesno("Confirm", "Stop all AutoHotkey scripts?"):
            try:
                # This would need platform-specific implementation
                messagebox.showinfo("Info", "Use AutoHotkey system tray to stop scripts")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to stop scripts: {str(e)}")

    def save_script(self):
        """Save script to file"""
        try:
            script = self.script_editor.get("1.0", "end-1c")
            filename = f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ahk"

            with open(filename, "w") as f:
                f.write(script)

            messagebox.showinfo("Success", f"Script saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")

    def load_script(self):
        """Load script from file"""
        from tkinter import filedialog
        try:
            filename = filedialog.askopenfilename(
                title="Select AHK Script",
                filetypes=[("AHK Scripts", "*.ahk"), ("All Files", "*.*")]
            )

            if filename:
                with open(filename, "r") as f:
                    script = f.read()

                self.script_editor.delete("1.0", "end")
                self.script_editor.insert("1.0", script)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load: {str(e)}")

    # ===== Recorder Methods =====

    def toggle_recording(self):
        """Toggle macro recording"""
        self.is_recording = not self.is_recording

        if self.is_recording:
            self.record_btn.configure(text="Stop Recording", fg_color="red")
            self.record_status.configure(text="Status: Recording...")
            self.start_recording()
        else:
            self.record_btn.configure(text="Start Recording", fg_color="green")
            self.record_status.configure(text="Status: Not Recording")
            self.stop_recording()

    def start_recording(self):
        """Start recording macro"""
        messagebox.showinfo("Info", "Macro recording started!\n\nNote: Full implementation requires additional keyboard/mouse listeners")
        # Would implement with pynput keyboard and mouse listeners

    def stop_recording(self):
        """Stop recording macro"""
        self.update_recorded_display()

    def playback_macro(self):
        """Playback recorded macro"""
        if not self.recorded_actions:
            messagebox.showwarning("Warning", "No macro recorded")
            return

        messagebox.showinfo("Info", "Macro playback would execute recorded actions")

    def clear_recording(self):
        """Clear recorded actions"""
        if messagebox.askyesno("Confirm", "Clear all recorded actions?"):
            self.recorded_actions.clear()
            self.recorded_display.delete("1.0", "end")

    def save_macro(self):
        """Save macro to file"""
        try:
            if not self.recorded_actions:
                messagebox.showwarning("Warning", "No macro to save")
                return

            filename = f"macro_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, "w") as f:
                json.dump(self.recorded_actions, f, indent=2)

            messagebox.showinfo("Success", f"Macro saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save macro: {str(e)}")

    def load_macro(self):
        """Load macro from file"""
        from tkinter import filedialog
        try:
            filename = filedialog.askopenfilename(
                title="Select Macro File",
                filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
            )

            if filename:
                with open(filename, "r") as f:
                    self.recorded_actions = json.load(f)

                self.update_recorded_display()
                messagebox.showinfo("Success", "Macro loaded!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load macro: {str(e)}")

    def update_recorded_display(self):
        """Update recorded actions display"""
        self.recorded_display.delete("1.0", "end")
        for i, action in enumerate(self.recorded_actions, 1):
            self.recorded_display.insert("end", f"{i}. {action}\n")

    # ===== System Methods =====

    def refresh_system_info(self):
        """Refresh system information"""
        try:
            self.system_info.delete("1.0", "end")

            info = []
            info.append("=== System Information ===\n")
            info.append(f"CPU Usage: {psutil.cpu_percent()}%")
            info.append(f"Memory Usage: {psutil.virtual_memory().percent}%")
            info.append(f"Disk Usage: {psutil.disk_usage('/').percent}%")
            info.append(f"Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}")
            info.append(f"\nRunning Processes: {len(list(psutil.process_iter()))}")

            self.system_info.insert("1.0", "\n".join(info))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get system info: {str(e)}")

    def adjust_volume(self, action):
        """Adjust system volume"""
        if not self.ahk:
            return
        try:
            if action == "up":
                self.ahk.send("{Volume_Up}")
            elif action == "down":
                self.ahk.send("{Volume_Down}")
            elif action == "mute":
                self.ahk.send("{Volume_Mute}")

            messagebox.showinfo("Success", f"Volume {action} executed")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to adjust volume: {str(e)}")

    def lock_screen(self):
        """Lock the screen"""
        if not self.ahk:
            return
        try:
            import subprocess
            subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to lock screen: {str(e)}")

    def confirm_logoff(self):
        """Confirm and log off"""
        if messagebox.askyesno("Confirm", "Are you sure you want to log off?"):
            messagebox.showinfo("Info", "Logoff command would be executed here")

    def confirm_shutdown(self):
        """Confirm and shutdown"""
        if messagebox.askyesno("Confirm", "Are you sure you want to shutdown?"):
            messagebox.showinfo("Info", "Shutdown command would be executed here")

    def confirm_restart(self):
        """Confirm and restart"""
        if messagebox.askyesno("Confirm", "Are you sure you want to restart?"):
            messagebox.showinfo("Info", "Restart command would be executed here")


def main():
    """Main entry point"""
    app = PythonAHKGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
