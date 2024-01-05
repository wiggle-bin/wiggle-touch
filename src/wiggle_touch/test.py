#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import logging
from wiggle_touch.lib import LCD_2inch
from PIL import Image, ImageDraw

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.DEBUG)


def main():
    try:
        disp = LCD_2inch.LCD_2inch()
        disp.Init()
        disp.clear()

        # Create blank image for drawing.
        image = Image.new("RGB", (disp.height, disp.width), "WHITE")
        draw = ImageDraw.Draw(image)

        logging.info("draw rectangle")
        draw.rectangle([(20, 10), (70, 60)], fill="WHITE", outline="BLUE")
        draw.rectangle([(85, 10), (130, 60)], fill="BLUE")

        logging.info("draw circle")
        draw.arc((150, 15, 190, 55), 0, 360, fill=(0, 255, 0))
        draw.ellipse((150, 65, 190, 105), fill=(0, 255, 0))

        disp.ShowImage(image)

        time.sleep(3)
        disp.module_exit()
        logging.info("quit:")
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        disp.module_exit()
        logging.info("quit:")
        exit()


if __name__ == "__main__":
    main()
