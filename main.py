from pynput.keyboard import Key, Controller
keyboard = Controller()

from pynput.mouse import Button, Controller
mouse = Controller()

import pyautogui
import random
import time
z = random.randint(2,6)
y = random.randint(18 , 32)
x = 0
while True:
    pyautogui.moveTo(489,1002)
    pyautogui.click(clicks=1)
    pyautogui.typewrite("owo hunt", interval=0.10)
    pyautogui.press("enter")
    time.sleep(z)
    time.sleep(11)
    x = x + 2
