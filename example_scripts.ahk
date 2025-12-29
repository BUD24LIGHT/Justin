; =============================================================================
; Python AHK GUI - Example Scripts Collection
; =============================================================================
; This file contains example AutoHotkey scripts that demonstrate various
; automation capabilities. Copy and paste these into the Script Editor tab.
; =============================================================================

; -----------------------------------------------------------------------------
; BASIC TEXT AUTOMATION
; -----------------------------------------------------------------------------

; F1: Insert current date and time
F1::
    FormatTime, CurrentDateTime,, yyyy-MM-dd HH:mm:ss
    Send, %CurrentDateTime%
return

; F2: Type a common email signature
F2::
    Send, Best regards,{Enter}
    Send, Your Name{Enter}
    Send, your.email@example.com{Enter}
    Send, Phone: (555) 123-4567
return

; -----------------------------------------------------------------------------
; WINDOW MANAGEMENT
; -----------------------------------------------------------------------------

; Ctrl+Alt+N: Open Notepad
^!n::
    Run, notepad.exe
return

; Ctrl+Alt+C: Open Calculator
^!c::
    Run, calc.exe
return

; Ctrl+Alt+B: Open Default Browser
^!b::
    Run, https://www.google.com
return

; Win+Up: Maximize active window
#Up::
    WinMaximize, A
return

; Win+Down: Minimize active window
#Down::
    WinMinimize, A
return

; -----------------------------------------------------------------------------
; TEXT EXPANSION
; -----------------------------------------------------------------------------

; Type abbreviations that auto-expand
:*:btw::by the way
:*:omw::on my way
:*:brb::be right back
:*:imo::in my opinion
:*:tyvm::thank you very much

; Email expansions
:*:@gmail::youremail@gmail.com
:*:@work::yourwork@company.com

; -----------------------------------------------------------------------------
; CLIPBOARD OPERATIONS
; -----------------------------------------------------------------------------

; Ctrl+Shift+C: Copy and show confirmation
^+c::
    Send, ^c
    Sleep, 100
    ToolTip, Text Copied!
    SetTimer, RemoveToolTip, 1000
return

; Ctrl+Shift+V: Paste as plain text
^+v::
    Clipboard := Clipboard  ; Convert to plain text
    Send, ^v
return

RemoveToolTip:
    SetTimer, RemoveToolTip, Off
    ToolTip
return

; -----------------------------------------------------------------------------
; MOUSE AUTOMATION
; -----------------------------------------------------------------------------

; F5: Click at specific coordinates (adjust as needed)
F5::
    Click, 500, 300
return

; F6: Double-click at current position
F6::
    Click, 2
return

; F7: Right-click at current position
F7::
    Click, Right
return

; -----------------------------------------------------------------------------
; PRODUCTIVITY HOTKEYS
; -----------------------------------------------------------------------------

; Ctrl+Alt+S: Save screenshot to desktop
^!s::
    FormatTime, TimeString,, yyyy-MM-dd_HHmmss
    FileName := A_Desktop . "\Screenshot_" . TimeString . ".png"
    Send, {PrintScreen}
    Sleep, 100
    MsgBox, Screenshot captured! (Save manually)
return

; Ctrl+Alt+L: Lock computer
^!l::
    DllCall("LockWorkStation")
return

; -----------------------------------------------------------------------------
; ADVANCED AUTOMATION
; -----------------------------------------------------------------------------

; F8: Auto-fill form demo (adjust selectors)
F8::
    Send, John Doe
    Send, {Tab}
    Send, john.doe@email.com
    Send, {Tab}
    Send, (555) 123-4567
    Send, {Tab}
    Send, 123 Main Street
return

; F9: Repeat last action 5 times
F9::
    Loop, 5
    {
        Send, Repeated action %A_Index%{Enter}
        Sleep, 500
    }
return

; -----------------------------------------------------------------------------
; MEDIA CONTROLS
; -----------------------------------------------------------------------------

; Ctrl+Alt+Up: Volume Up
^!Up::
    Send, {Volume_Up}
return

; Ctrl+Alt+Down: Volume Down
^!Down::
    Send, {Volume_Down}
return

; Ctrl+Alt+M: Mute
^!m::
    Send, {Volume_Mute}
return

; Ctrl+Alt+P: Play/Pause media
^!p::
    Send, {Media_Play_Pause}
return

; -----------------------------------------------------------------------------
; WORK-SPECIFIC AUTOMATION
; -----------------------------------------------------------------------------

; F10: Open commonly used programs
F10::
    MsgBox, 4, Open Programs, Open work programs?
    IfMsgBox Yes
    {
        Run, notepad.exe
        Sleep, 500
        Run, calc.exe
        Sleep, 500
        Run, explorer.exe
    }
return

; F11: Insert common code snippet
F11::
    Send, def function_name():{Enter}
    Send,     """Docstring"""{Enter}
    Send,     pass{Enter}
return

; F12: Create timestamp log entry
F12::
    FormatTime, TimeStamp,, [yyyy-MM-dd HH:mm:ss]
    Send, %TimeStamp% -
return

; -----------------------------------------------------------------------------
; WINDOW ARRANGEMENT
; -----------------------------------------------------------------------------

; Ctrl+Win+Left: Move window to left half of screen
^#Left::
    WinGetPos, X, Y, Width, Height, A
    WinMove, A,, 0, 0, A_ScreenWidth/2, A_ScreenHeight
return

; Ctrl+Win+Right: Move window to right half of screen
^#Right::
    WinGetPos, X, Y, Width, Height, A
    WinMove, A,, A_ScreenWidth/2, 0, A_ScreenWidth/2, A_ScreenHeight
return

; -----------------------------------------------------------------------------
; CUSTOM FUNCTIONS
; -----------------------------------------------------------------------------

; Ctrl+Shift+R: Reload this script
^+r::
    Reload
return

; Ctrl+Shift+E: Edit this script
^+e::
    Edit
return

; Ctrl+Shift+Q: Exit script
^+q::
    ExitApp
return

; -----------------------------------------------------------------------------
; ADVANCED: WEB AUTOMATION
; -----------------------------------------------------------------------------

; Alt+G: Google search selected text
!g::
    Send, ^c
    Sleep, 50
    Run, https://www.google.com/search?q=%clipboard%
return

; Alt+Y: YouTube search selected text
!y::
    Send, ^c
    Sleep, 50
    Run, https://www.youtube.com/results?search_query=%clipboard%
return

; -----------------------------------------------------------------------------
; ADVANCED: CONDITIONAL AUTOMATION
; -----------------------------------------------------------------------------

; #IfWinActive example: Different behavior in different applications
#IfWinActive, ahk_exe notepad.exe
    ; Ctrl+S in Notepad shows custom save dialog
    ^s::
        MsgBox, Saving in Notepad!
        Send, ^s
    return
#IfWinActive

; -----------------------------------------------------------------------------
; TIPS:
; -----------------------------------------------------------------------------
; - Adjust coordinates and timings based on your system
; - Test scripts in safe environments first
; - Use SetTimer for repeated actions
; - Combine with Python GUI for dynamic parameter input
; - Always include error handling for production use
; =============================================================================
