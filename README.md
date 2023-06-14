# Weight Reader

This Python script reads weight data from a serial port and sends it as keyboard input. It can be useful for integrating weighing scales with other applications.

## Prerequisites

- Python 3.6+
- PySerial
- PyAutoGUI
- pyinstaller

## Installation

1. Clone the repository or download the script file.

2. Install the required Python packages:

   ```shell
   pip install pyserial pyautogui
   ```
3. Update the JSON configuration file (`config.json`)

4. Convert the file to an executable:

   ```shell
   pyinstaller --onefile ReadWeightFromScale.py
   ```

5. You can now run the executable using the following command:

   ```shell
    dist/ReadWeightFromScale.exe -c config.json
   ```
