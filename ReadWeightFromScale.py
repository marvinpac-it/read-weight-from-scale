import argparse
import serial
import pyautogui
import re

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Read weight data from serial port and send it as keyboard input.')
parser.add_argument('-p', '--port', type=str, help='Serial port')
parser.add_argument('-b', '--baud', type=int, help='Baud rate')
args = parser.parse_args()

# Validate command-line arguments
if not args.port or not args.baud:
    parser.error('Please provide both serial port and baud rate.')

# Open the serial port
ser = serial.Serial(args.port, args.baud)

# Read data from the serial port
while True:
    # Read a line from the serial port
    line = ser.readline().decode().strip()

    # Process the line and convert it to weight data
    if line.startswith('Net:'):
        # Extract weight value from the line
        weight_str = re.sub('[\[\]]', '', line.split()[1])
        print(weight_str)
        # Simulate keyboard input
        pyautogui.typewrite(weight_str)

# Close the serial port
ser.close()


