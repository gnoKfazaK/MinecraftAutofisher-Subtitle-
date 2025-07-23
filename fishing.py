import pyautogui
import time 
import winsound


def retreive_and_throw(BEEP_WHEN_CAUGHT, caught_count):
    if BEEP_WHEN_CAUGHT:
        winsound.Beep(500, 500)
    pyautogui.click(button = 'right')
    time.sleep(1)
    pyautogui.click(button='right')
    caught_count += 1
    print('Count:', caught_count)
    return caught_count
    