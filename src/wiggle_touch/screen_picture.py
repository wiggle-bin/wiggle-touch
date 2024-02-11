import os
from pathlib import Path
import time
from wiggle_touch import screen_menu

from wiggle_touch.data_images import Images
from wiggle_touch.display import Display

BASE_FOLDER = Path.home() / "WiggleR"
IMG_FOLDER = BASE_FOLDER / "Pictures"

def picture(display):
    display.clear()
    
    os.system("wiggle-camera --picture")

    images = Images()
    display.show_image(images.last)
    time.sleep(5)

def show(btn, rotor, display):
    picture(display)
    screen_menu.show(btn, rotor, display)

if __name__ == "__main__":
    picture(Display())
