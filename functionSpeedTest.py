import easyocr
import time
from PIL import Image
import cv2
import numpy as np

RESIZE = 0.35
IMAGES = 6
PRINT_THE_WORDS_OUT = True

reader = easyocr.Reader(['en'], gpu=True)
start = time.perf_counter()
for i in range(IMAGES):
    img = Image.open(f'./testimages/image{i}.png')
    img = img.resize((int(img.size[0] * RESIZE), int(img.size[1] * RESIZE)))
    ocrImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    results = reader.readtext(ocrImage)
    if PRINT_THE_WORDS_OUT:
        print(f"Image{i}:")
        for result in results:
            print(result[1].lower())
        print('--------------------------\n')
end = time.perf_counter()

print(f"IMAGES = {IMAGES}")
print(f"PRINT_THE_WORDS_OUT = {PRINT_THE_WORDS_OUT}")
print(f"Time: {end - start} s")
print(f"Avg time = {(end - start) / IMAGES} s/image")
