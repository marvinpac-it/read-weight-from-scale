import argparse
import json
import serial
import pyautogui
import time
import re

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Read weight data from serial port and send it as keyboard input.')
parser.add_argument('-c', '--config', type=str, help='Path to the configuration file')
args = parser.parse_args()

# Validate command-line arguments
if not args.config:
    parser.error('Please provide the path to the configuration file.')

# Load the configuration from the file
with open(args.config, 'r') as file:
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
