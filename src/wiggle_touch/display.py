import os
from wiggle_touch.lib import LCD_2inch
from PIL import Image
from RPi import GPIO
import logging
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.CRITICAL)

# Pin configuration for LCD screen
# RST = 27
# DC = 25
# BL = 18
# bus = 0
# device = 0


class Display:
    """Handle display interactions."""

    def __init__(self):
        disp = LCD_2inch.LCD_2inch()
        disp.Init()
        disp.clear()

        self.image = Image.new("RGB", (disp.height, disp.width), "BLACK")
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(
            os.path.dirname(__file__) + "/font/pixel_arial_11.ttf", 14
        )

        self.disp = disp

    def blank(self):
        self.draw.rectangle(
            (-1, -1, self.disp.height + 1, self.disp.width + 1), outline=0, fill="BLACK"
        )

    def show_image(self, path):
        print(f"Show image {path}")
        try:
            with Image.open(path) as image:
                self.disp.ShowImage(image.resize((320, 240)).rotate(180))
        except Exception as e:
            print(f"Unable to open image {path}.")
            print(f"Error details: {str(e)}")

    def show_menu_item(self, display_text):
        print(f"Show menu item")
        try:
            self.blank()
            self.draw.text((3, 10), display_text, font=self.font, fill="WHITE")
            self.disp.ShowImage(self.image)
        except Exception as e:
            print(f"Unable to show menu item.")
            print(f"Error details: {str(e)}")

    def clean_up(self):
        GPIO.cleanup()

    def exit(self):
        self.disp.module_exit()
