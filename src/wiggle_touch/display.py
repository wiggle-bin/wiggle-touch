from wiggle_touch.lib import LCD_2inch
from PIL import Image
from pathlib import Path
from RPi import GPIO
import logging

logging.basicConfig(level=logging.CRITICAL)

# Pin configuration for LCD screen
# RST = 27
# DC = 25
# BL = 18
# bus = 0
# device = 0


class Display:
    """Handle display interactions."""

    def __init__(self, files):
        disp = LCD_2inch.LCD_2inch()
        disp.Init()
        disp.clear()

        self.disp = disp
        self.files = files
        self.imageCount = len(files) - 1

    def show_image(self, path):
        print(f"Show image {path}")
        try:
            with Image.open(path) as image:
                self.disp.ShowImage(image.resize((320, 240)).rotate(180))
        except Exception as e:
            print(f"Unable to open image {path}.")
            print(f"Error details: {str(e)}")

    def clean_up(self):
        GPIO.cleanup()

    def exit(self):
        self.disp.module_exit()
