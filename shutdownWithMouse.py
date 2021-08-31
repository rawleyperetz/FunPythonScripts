'''
This code works perfectly for those with screen dimensions width=1920 and height=1080
and also those using windows 10 home edition.
Try and adjust to suit your screen size
To find screen size use, pyautogui.size()
Enjoy :)
'''
import pyautogui
pyautogui.click(30, 1038, duration=1.0) # clicks on the start menu button
pyautogui.click(30, 1000, duration=1.0) # clicks on the power button
pyautogui.doubleClick(60, 860, duration=1.0) # clicks on the shutdown button

# This will cause the program to pause every 1.5s so you can control the mouse in case of incasity
pyautogui.PAUSE=1.5

'''fail-safe feature will stop the program
 if you quickly move the mouse as far up and left as you can (thus top-left corner)'''
pyautogui.FAILSAFE=True 
