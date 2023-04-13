import pyautogui
import time
import keyboard

USER_IMAGE = 'User.PNG' # Image of the username of the user
DISCONNECT_IMAGE = 'Disconnect.PNG' # Image of the disconnect button
CHANNEL_ICON = 'Channel.PNG' # Image of the icon of a discord channel
REMOVE_CHANNEL = 'Remove.PNG' # Image of the remove channel button
REMOVE_CHANNEL_2 = 'Remove2.PNG' # Image 2 of the remove channel button

# Set confidence level
# 0.8 for usernames 
# 0.5 for images

def delete_user():
    user_to_delete = pyautogui.locateOnScreen(USER_IMAGE, grayscale=True, confidence=.8)

    while not keyboard.is_pressed('q'):
        try:
            user_to_delete = pyautogui.center(user_to_delete)
            x_coordinate, y_coordinate = user_to_delete
            pyautogui.click(button='right',x=x_coordinate,y=y_coordinate)
            pyautogui.click(DISCONNECT_IMAGE)
            disconnect_user = pyautogui.locateOnScreen(REMOVE_CHANNEL, grayscale=True, confidence=.8)
            disconnect_user = pyautogui.center(disconnect_user)
            x_coordinate, y_coordinate = disconnect_user
            pyautogui.click(x=x_coordinate,y=y_coordinate)
        except (IndexError, TypeError) as exception:
            print("Missing user, exception: ", exception)
        
        time.sleep(0.1)
        pyautogui.press('esc')
        user_to_delete = pyautogui.locateOnScreen(USER_IMAGE, grayscale=True, confidence=.8)

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

def main():
    print("Which option do you want to execute?\n1 - Delete a specific user\n2 - Delete all channels on the server\n")
    option = int(input())

    if option == 1:
        delete_user()
    else:
        delete_channels()

if __name__ == '__main__':
    main()