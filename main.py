import pyautogui
import time
import keyboard

USER_IMAGE = 'User.PNG' # Image of the username of the user
DISCONNECT_IMAGE = 'Disconnect.PNG' # Image of the disconnect button

# Set confidence level
# 0.8 for usernames 
# 0.5 for images

user_to_delete = pyautogui.locateOnScreen(USER_IMAGE, grayscale=True, confidence=.8)

while not keyboard.is_pressed('q'):
    try:
        user_to_delete = pyautogui.center(user_to_delete)
        x_coordinate, y_coordinate = user_to_delete
        pyautogui.click(button='right',x=x_coordinate,y=y_coordinate)
        pyautogui.click(DISCONNECT_IMAGE)
    except (IndexError, TypeError) as exception:
        print("Missing user, exception: ", exception)
    
    time.sleep(0.1)
    pyautogui.press('esc')
    user_to_delete = pyautogui.locateOnScreen(USER_IMAGE, grayscale=True, confidence=.8)