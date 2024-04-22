import json
import serial
import re
from time import sleep
from pyautogui import press

# Fichier de configuration pré-defini
config_file_path = 'config.json'

# Load the configuration from the file
with open(config_file_path) as file:
    config = json.load(file)

# Extract configuration values
port = config.get('port')
baud_rate = config.get('baud_rate')
bytesize = config.get('bytesize')
parity = config.get('parity')
stopbits = config.get('stopbits')
timeout = config.get('timeout')
eol = config.get('eol')

# Validate configuration values
if not port or not baud_rate:
    raise ValueError('Invalid configuration. Please check the configuration file.')

# Attempt to open the serial port
ser = None
while ser is None:
    try:
        ser = serial.Serial(port, baud_rate, bytesize, parity, stopbits)
        print(f"Connected to COM port {port}")

        # Read data from the serial port
        while True:
            # Read a line from the serial port
            line = ser.readline().decode().strip()
            weight_match = re.search(r'\b(\d+\.\d+)\b', line)

            # Process the line and convert it to weight data
            if weight_match:
                weight_str = weight_match.group(1)
                # keyboard.write(weight_str)
            
            else:
                # Handle case where no match is found
                weight_str = "ERREUR"  # or any default value you prefer
                # keyboard.write(weight_str)

            for c in (weight_str + eol):
                press(c)
            

        # Close the serial port
        ser.close()
    except serial.SerialException:
        ser = None
        print(f"COM port {port} is not available. Retrying in {timeout} seconds...")
        time.sleep(timeout)
