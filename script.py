import pyautogui
import cv2
import easyocr
import time 
import winsound
import numpy as np
import os
from Options import *
from screenshot import regionCalculation, screenCapAndProcess
from fishing import retreive_and_throw


# My pc won't work, the readtext function is too slow for me :( 
# GUI_SCALE  RESIZE
# 1          0.85 (slight loss for me)
# 2          0.7  
# 3          0.4 
# 4          0.35

os.environ["PYTHONIOENCODING"] = "utf-8"
caught_count = 0

spell = 'fishin' # Magic words

region = regionCalculation(GUI_SCALE) # Calculate the screenshot region

reader = easyocr.Reader(['en'], gpu=True)

print('Start...')
CAUGHT = False
while True:
    if TIMER:
        start = time.perf_counter()

    image = screenCapAndProcess(CAPTURE_THE_SCREENSHOT, CAPTURE_THE_OCRIMAGE, RESIZE, region, USE_GPU)
    
    results = reader.readtext(image)
    if VERBOSE: 
        print('------------------------------\n')
    for result in results:
        if VERBOSE:
            print(result[1].lower())
        if spell in result[1].lower():
            caught_count = retreive_and_throw(BEEP_WHEN_CAUGHT, caught_count)
            CAUGHT = True
     
    if TIMER:
        end = time.perf_counter()
        print(f'time = {end - start} s')
        print('------------------------------\n')

    if CAUGHT:
        time.sleep(NOTIFICATION_TIME * 3 - 2 if NOTIFICATION_TIME > 2.5 else 5)
        CAUGHT = False
    
