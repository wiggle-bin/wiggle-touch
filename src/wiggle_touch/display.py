from wiggle_touch.lib import LCD_2inch
from PIL import Image
from RPi import GPIO
import logging
from PIL import Image

logging.basicConfig(level=logging.CRITICAL)

def is_grayscale(img):
    return img.mode in ('L', '1', 'I;16')

class Display:
    """Handle display interactions."""

    def __init__(self):
        disp = LCD_2inch.LCD_2inch()
        disp.Init()
        disp.clear()

        self.disp = disp
        self.height = disp.height
        self.width = disp.width

    def show_image(self, path):
        print(f"Show image {path}")
        try:
            with Image.open(path) as image:
                if is_grayscale(image):
                    image = image.convert('RGB')
                self.disp.ShowImage(image.resize((320, 240)).rotate(180))
        except Exception as e:
            print(f"Unable to open image {path}.")
            print(f"Error details: {str(e)}")

    def clear(self):
        empty_image = Image.new('RGB', (self.width, self.height))
        self.disp.ShowImage(empty_image)

    def clean_up(self):
        GPIO.cleanup()

    def exit(self):
        self.disp.module_exit()
