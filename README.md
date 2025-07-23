# MinecraftAutofisher-Subtitle-
## Utilizing subtitle to acheive automatic fishing in minecraft
### Installing dependencies
Open cmd and type:
```bash
pip install pyautogui cv2 easyocr numpy winsound
```
### Options.py
```python
GUI_SCALE = 1
GUI_TO_RESIZE = [-1, 0.85, 0.7, 0.4, 0.35]
RESIZE = GUI_TO_RESIZE[GUI_SCALE]
NOTIFICATION_TIME = 1
BEEP_WHEN_CAUGHT = False
USE_GPU = False # True is recommended
CAPTURE_THE_SCREENSHOT = False
CAPTURE_THE_OCRIMAGE = False
TIMER = False
VERBOSE = False
```
#### Set up the correct constants for your script
- GUI_SCALE means GUI scale (1-4) of your minecraft (Do not input Auto)
- RESIZE means the resolution of the processed screenshot. Preset to GUI_TO_RESIZE = [-1, 0.85, 0.7, 0.4, 0.35], or choose your own(1 is largest 0 is smallest)
- NOTIFICATION_TIME means the Notification time in your Minecraft setting
- BEEP_WHEN_CAUGHT means will there be a beep sound when a fish is caught
- USE_GPU if CUDA or MPS are available then set it to True, else leave it as False
- CAPTURE_THE_SCREENSHOT means saving the screenshot
- CAPTURE_THE_OCRIMAGE means saving the processed image
- TIMER means having a timer to record every reader.readtext() function time spent
- VERBOSE means printing out the reader.readtext() result


### script.py
To run the script make sure all the dependencies are downloaded and navigate to this folder then type;
```bash
python script.py
```
- Press Ctrl+C to stop the program
- USE FULLSCREEN FOR MINECRAFT AS THE PROGRAM IS RUNNING


