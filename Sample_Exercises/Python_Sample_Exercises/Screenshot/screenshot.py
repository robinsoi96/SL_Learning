import os
import pyautogui
from PIL import Image

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

Screenshot_image = os.path.join(FILE_PATH, "screenshot.png")

# Take a screenshot of the current screen and save it as "screenshot.png" in the same directory as the script
pyautogui.screenshot(Screenshot_image)

# Open the snapshot for preview
with Image.open(Screenshot_image) as img:
    img.show()