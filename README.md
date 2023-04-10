# Autoremover-discord

This repository contains a Python script that uses the PyAutoGUI library to automatically disconnect users from discord. The script searches for a specific user image and disconnects it using a pre-defined disconnect button image.

### Dependencies
This script requires the following dependencies to be installed:

PyAutoGUI
keyboard

You can install these dependencies using pip. Run the following command in your terminal:

`pip install pyautogui keyboard`

### Usage
To use this script, you need to provide two images: one for the user and one for the disconnect button.

Images:
USER_IMAGE: Image of the username of the user
DISCONNECT_IMAGE: Image of the disconnect button
You can adjust the confidence level of the image recognition algorithm. The current confidence level is set to 0.8 for the username and 0.5 for the images.

To run the script, navigate to the directory where you have saved the script and run the following command:

`python autoremove-discord.py`

Once you run the script, it will start searching for the user image on the screen. If it finds the user image, it will click on it and then click on the disconnect button. The script will keep running until you press the q key.
