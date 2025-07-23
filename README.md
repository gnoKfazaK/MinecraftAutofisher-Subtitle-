# MinecraftAutofisher-Subtitle-
## Utilizing subtitle to acheive automatic fishing in minecraft
### Installing dependencies
Open cmd and type:
```bash
pip install pyautogui cv2 easyocr numpy winsound
```
### Options.py
#### Set up the correct constants for your script
- GUI_SCALE means GUI scale (1-4) of your minecraft (Do not input Auto)
- RESIZE means the resolution of the processed screenshot. Preset to GUI_TO_RESIZE = [-1, 0.85, 0.7, 0.4, 0.35], or choose your own(1 is largest 0 is smallest)
- NOTIFICATION_TIME means the Notification time in your Minecraft setting
- BEEP_WHEN_CAUGHT means will there be a beep sound when a fish is caught
- USE_GPU if CUDA or MPS are available then set it to True, else leave it as False (no RESIZE to reduce the resolution if USE_GPU is selected)
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

### screenshot.py
Containing regionCalculation() and screenCapAndProcess() 2 functions
#### regionCalculation()
Calculate the region that will be caputured by using GUI_SCALE
#### screenCapAndProcess()
Capture the image then process it by RESIZE (no RESIZE to reduce the resolution if USE_GPU is selected)

### fishing.py
Contain a function retreive_and_throw()
#### retreive_and_throw()
Right click twice with 1 second in between

### functionSpeedTest.py
This function uses to test how fast your machine can run reader.readtext() by using 6 images in testimages folder
