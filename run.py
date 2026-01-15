#!/usr/bin/env python3

# Import the tkinter fix to patch the ScreenChanged error (only if GUI available)
try:
    import tkinter_fix
except ImportError:
    # GUI not available (e.g., on Android/Termux), skip tkinter fix
    pass

from modules import core

if __name__ == '__main__':
    core.run()
