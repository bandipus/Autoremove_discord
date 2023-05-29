# Autoremove-discord

This repository contains a Python script that uses the PyAutoGUI library to automatically disconnect users and more annoying

### Dependencies
This script requires the following dependencies to be installed:

- PyAutoGUI
- keyboard
- colorama

You can install these dependencies using pip. Run the following command in your terminal:

`pip install pyautogui keyboard colorama`

### Usage
Before running the bot, make sure to configure the following images to match the ones you see on your Discord app:

- USER_IMAGE: List of the images of the usernames
- DISCONNECT_IMAGE: Image of the disconnect button
- CHANNEL_ICON: Image of the icon of a discord channel
- REMOVE_CHANNEL: Image of the remove channel button
- REMOVE_CHANNEL_2: Image 2 of the remove channel button
- LIVE_SCREEN: Image of the live screen button
- CHANNEL_IMAGE: Image of the name of the channel
You can adjust the confidence level of the image recognition algorithm. The current confidence level is set to 0.8 for the username and 0.5 for the images.

To run the script, navigate to the directory where you have saved the script and run the following command:

`python autoremove_discord.py`

In many modes, the script will keep running until you press the q key.
