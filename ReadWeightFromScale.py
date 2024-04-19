import json
import serial
import pyautogui
import time
import re

# Fichier de configuration pré-defini
config_file_path = 'config.json'

# Load the configuration from the file
with open(config_file_path) as file:
    config = json.load(file)

# Extract configuration values
port = config.get('port')
baud_rate = config.get('baud_rate')
timeout = config.get('timeout')
eol = config.get('eol')

# Validate configuration values
if not port or not baud_rate:
    raise ValueError('Invalid configuration. Please check the configuration file.')

# Attempt to open the serial port
ser = None
while ser is None:
    try:
        ser = serial.Serial(port, baud_rate)
        print(f"Connected to COM port {port}")

        # Read data from the serial port
        while True:
            # Read a line from the serial port
            line = ser.readline().decode().strip()

            # Process the line and convert it to weight data
            if line.startswith('Net:'):
                # Extract weight value from the line
                weight_str = re.sub('[\[\]]', '', line.split()[1])

                # Simulate keyboard input
                pyautogui.typewrite(weight_str + eol)

        # Close the serial port
        ser.close()
    except serial.SerialException:
        ser = None
        print(f"COM port {port} is not available. Retrying in {timeout} seconds...")
        time.sleep(timeout)
