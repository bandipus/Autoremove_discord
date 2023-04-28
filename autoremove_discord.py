import pyautogui
import time
import keyboard
from colorama import Fore, Style
import os

user_images = ['user1.PNG', 'user2.PNG', 'user3.PNG', 'user4.PNG', 'user5.PNG', 'user6.PNG', 'user7.PNG', 'user8.PNG', 'user9.PNG'] # List of the images of the usernames
DISCONNECT_IMAGE = 'disconnect.PNG' # Image of the disconnect button
CHANNEL_ICON = 'channelicon.PNG' # Image of the icon of a discord channel
REMOVE_CHANNEL = 'remove.PNG' # Image of the remove channel button
REMOVE_CHANNEL_2 = 'remove2.PNG' # Image 2 of the remove channel button
LIVE_SCREEN = 'livescreen.PNG' # Image of the live screen button
CHANNEL_IMAGE = 'channelimage.PNG' # Image of the name of the channel

# Set confidence level
# 0.8 for usernames 
# 0.5 for images

def delete_user(user):
    user_to_delete = pyautogui.locateOnScreen(user_images[user - 1], grayscale=True, confidence=.8)

    while not keyboard.is_pressed('q'):
        try:
            user_to_delete = pyautogui.center(user_to_delete)
            x_coordinate, y_coordinate = user_to_delete
            pyautogui.click(button='right',x=x_coordinate,y=y_coordinate)
            user_to_delete = pyautogui.locateOnScreen(DISCONNECT_IMAGE, grayscale=True, confidence=.8)
            user_to_delete = pyautogui.center(user_to_delete)
            x_coordinate, y_coordinate = user_to_delete
            pyautogui.click(x=x_coordinate,y=y_coordinate)
        except (IndexError, TypeError) as exception:
            print("Missing user, exception: ", exception)
        
        time.sleep(0.1)
        pyautogui.press('esc')
        user_to_delete = pyautogui.locateOnScreen(user_images[user - 1], grayscale=True, confidence=.8)

def crazy_mode(max_users):
    i = 0
    user_to_delete = pyautogui.locateOnScreen(user_images[i], grayscale=True, confidence=.8)

    while not keyboard.is_pressed('q'):
        try:
            user_to_delete = pyautogui.center(user_to_delete)
            x_coordinate, y_coordinate = user_to_delete
            pyautogui.click(button='right',x=x_coordinate,y=y_coordinate)
            user_to_delete = pyautogui.locateOnScreen(DISCONNECT_IMAGE, grayscale=True, confidence=.8)
            user_to_delete = pyautogui.center(user_to_delete)
            x_coordinate, y_coordinate = user_to_delete
            pyautogui.click(x=x_coordinate,y=y_coordinate)
        except (IndexError, TypeError) as exception:
            print("Missing users, exception: ", exception)
        
        i += 1
        if i == max_users:
            i = 0

        # time.sleep(0.1)
        pyautogui.press('esc')
        user_to_delete = pyautogui.locateOnScreen(user_images[i], grayscale=True, confidence=.8)

def delete_channels():
    channel_to_remove = pyautogui.locateOnScreen(CHANNEL_ICON, grayscale=True, confidence=.8)

    while channel_to_remove != None:
        try:
            channel_to_remove = pyautogui.center(channel_to_remove)
            x_coordinate, y_coordinate = channel_to_remove
            pyautogui.click(button='right',x=x_coordinate,y=y_coordinate)
            remove_channel = pyautogui.locateOnScreen(REMOVE_CHANNEL, grayscale=True, confidence=.8)
            remove_channel = pyautogui.center(remove_channel)
            x_coordinate, y_coordinate = remove_channel
            pyautogui.click(x=x_coordinate,y=y_coordinate)
            time.sleep(0.15)
            remove_channel = pyautogui.locateOnScreen(REMOVE_CHANNEL_2, grayscale=True, confidence=.8)
            remove_channel = pyautogui.center(remove_channel)
            x_coordinate, y_coordinate = remove_channel
            pyautogui.click(x=x_coordinate,y=y_coordinate)
            time.sleep(0.15)
            channel_to_remove = pyautogui.locateOnScreen(CHANNEL_ICON, grayscale=True, confidence=.8)
        except (IndexError, TypeError) as exception:
            print("Missing channels, exception: ", exception)

def remove_sharescreen():
    user_sharingscreen = pyautogui.locateOnScreen(LIVE_SCREEN, grayscale=True, confidence=.8)

    while user_sharingscreen != None:
        try:
            user_sharingscreen = pyautogui.center(user_sharingscreen)
            x_coordinate, y_coordinate = user_sharingscreen
            pyautogui.click(button='right',x=x_coordinate,y=y_coordinate)
            user_to_delete = pyautogui.locateOnScreen(DISCONNECT_IMAGE, grayscale=True, confidence=.8)
            user_to_delete = pyautogui.center(user_to_delete)
            x_coordinate, y_coordinate = user_to_delete
            pyautogui.click(x=x_coordinate,y=y_coordinate)
            user_sharingscreen = pyautogui.locateOnScreen(LIVE_SCREEN, grayscale=True, confidence=.8)
        except (IndexError, TypeError) as exception:
            print("Missing users who are sharing screen , exception: ", exception)

def move_to_a_channel(user):
    # Doesnt work properly :(
    user_to_move = pyautogui.locateOnScreen(user_images[user - 1], grayscale=True, confidence=.8)

    while not keyboard.is_pressed('q'):
        try:
            user_to_move = pyautogui.center(user_to_move)
            x_coordinate, y_coordinate = user_to_move
            pyautogui.moveTo(x=x_coordinate,y=y_coordinate)
            pyautogui.mouseDown(button='left')
            channel_name = pyautogui.locateOnScreen(CHANNEL_IMAGE, grayscale=True, confidence=.8)
            channel_name = pyautogui.center(channel_name)
            x2_coordinate, y2_coordinate = channel_name
            pyautogui.moveTo(x=x2_coordinate,y=y2_coordinate,duration=0.15)
            pyautogui.mouseUp(button='left')
        except (IndexError, TypeError) as exception:
            print("Missing user, exception: ", exception)
        
        time.sleep(0.1)
        pyautogui.press('esc')
        user_to_move = pyautogui.locateOnScreen(user_images[user - 1], grayscale=True, confidence=.8)

def help_pannel():
    print(Fore.GREEN + "Made by Bandipus :D" + Style.RESET_ALL + "\n")
    print(Fore.CYAN + "[!] Files required, they have to be in the same folder as the executable:" + Style.RESET_ALL)
    print("1 -> " + Fore.YELLOW + "user[number].png" + Style.RESET_ALL + ", " + Fore.YELLOW + "disconnect.png" + Style.RESET_ALL)
    print("2 -> " + Fore.YELLOW + "channelicon.png" + Style.RESET_ALL + ", " + Fore.YELLOW + "remove.png" + Style.RESET_ALL + ", " + Fore.YELLOW + "remove2.png" + Style.RESET_ALL)
    print("3 -> " + Fore.YELLOW + "user[number].png" + Style.RESET_ALL + ", " + Fore.YELLOW + "livescreen.png" + Style.RESET_ALL + ", " + Fore.YELLOW + "disconnect.png" + Style.RESET_ALL)
    print("4 -> " + Fore.YELLOW + "user[number].png" + Style.RESET_ALL + ", " + Fore.YELLOW + "disconnect.png" + Style.RESET_ALL)
    print("5 -> " + Fore.YELLOW + "user[number].png" + Style.RESET_ALL + ", " + Fore.YELLOW + "channelimage.png" + Style.RESET_ALL)
    print(Fore.CYAN + "You have examples in the github repository!" + Style.RESET_ALL + "\n")

def print_title():

    print(Fore.CYAN + """
                _                                               _ _                       _ 
     /\        | |                                             | (_)                     | |
    /  \  _   _| |_ ___  _ __ ___ _ __ ___   _____   _____   __| |_ ___  ___ ___  _ __ __| |
   / /\ \| | | | __/ _ \| '__/ _ \ '_ ` _ \ / _ \ \ / / _ \ / _` | / __|/ __/ _ \| '__/ _` |
  / ____ \ |_| | || (_) | | |  __/ | | | | | (_) \ V /  __/| (_| | \__ \ (_| (_) | | | (_| |
 /_/    \_\__,_|\__\___/|_|  \___|_| |_| |_|\___/ \_/ \___| \__,_|_|___/\___\___/|_|  \__,_|
                                                        ______                              
                                                       |______|                             
""" + Fore.RESET)
    print(Fore.GREEN + "Which option do you want to execute?\n"
      + Fore.YELLOW + "1 - Delete a specific user\n"
      + "2 - Delete all channels on the server\n"
      + "3 - Delete all users sharing screen\n"
      + "4 - Remove all users in the server (which you have stored)\n"
      + "5 - Move a user forever to a channel " + Fore.RED + "[!] Doesnt work properly\n"
      + Fore.CYAN + "6 - [!] Help button (very useful)\n"
      + "Any other number - Exit\n")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    clear_terminal()
    time.sleep(0.1)
    print_title()
    option = int(input())

    while option > 0 and option < 7:

        if option == 1:
            print("Which user do you want to remove?\n1 - 9\n")
            user = int(input())
            
            while user > 9 or user < 1:
                print("User out of range, insert a number between 1 and 9\n")
                user = int(input())
            
            delete_user(user)

        elif option == 2:
            delete_channels()

        elif option == 3:
            remove_sharescreen()
        
        elif option == 4:
            print("How many user images do you have stored?\n")
            n = int(input())
            crazy_mode(n)

        elif option == 5:
            print("Which user do you want to drag to the channel?\n1 - 9\n")
            user = int(input())
            
            while user > 9 or user < 1:
                print("User out of range, insert a number between 1 and 9\n")
                user = int(input())
            
            move_to_a_channel(user)

        elif option == 6:
            help_pannel()

        print("Press enter to continue...")
        input()
        clear_terminal()
        print_title()
        option = int(input())

    print("Exiting...\n")
    time.sleep(1)
