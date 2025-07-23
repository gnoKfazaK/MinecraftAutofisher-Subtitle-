import pyautogui
import cv2
import easyocr
import time 
import winsound
import numpy as np
import os


def regionCalculation(GUI_SCALE):
    height_ratio, width_ratio = 0.37 / 3 * GUI_SCALE, 0.25 / 3 * GUI_SCALE
    original_width, original_height = pyautogui.size()
    width_side, height_side = int(original_width * width_ratio), int(original_height * height_ratio)
    width, height = original_width - width_side, original_height - height_side
    return (width, height, width_side, height_side)


def screenCapAndProcess(CAPTURE_THE_SCREENSHOT, CAPTURE_THE_OCRIMAGE, RESIZE, region, USE_GPU):
    screenCapture = pyautogui.screenshot(region=region)
    if CAPTURE_THE_SCREENSHOT:
        screenCapture.save("image.png")
    if not USE_GPU:
        img = screenCapture.resize((int(screenCapture.size[0] * RESIZE), int(screenCapture.size[1] * RESIZE)))

    ocrImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV
    if CAPTURE_THE_OCRIMAGE:
        cv2.imwrite("ocrimage.png", ocrImage)
    
    return ocrImage


def main():
    GUI_SCALE = 3
    RESIZE = 1
    region = regionCalculation(GUI_SCALE)
    time.sleep(5)
    image = screenCapAndProcess(True, True, RESIZE, region)
    winsound.Beep(500, 500)

    

if __name__ == "__main__":
    print('Screenshot mode')
    main()