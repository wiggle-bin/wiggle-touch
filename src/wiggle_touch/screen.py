#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import chardet
import os
import sys
import spidev as SPI
from pathlib import Path
from threading import Event
from gpiozero import RotaryEncoder

sys.path.append("..")
from wiggle_touch.display import Display
import logging

logging.basicConfig(level=logging.CRITICAL)

# Paths
BASE_FOLDER = Path.home() / "WiggleR"
IMG_FOLDER = BASE_FOLDER / "Pictures"


def main():
    try:
        files = sorted(os.listdir(IMG_FOLDER))
        imageCount = len(files) - 1
        display = Display()

        # Show most recent image on startup
        display.show_image(IMG_FOLDER / files[imageCount])

        # Listen to rotary
        rotor = RotaryEncoder(17, 23, wrap=True, max_steps=imageCount)
        done = Event()

        def change_image():
            index = imageCount + rotor.steps if rotor.steps < 0 else rotor.steps
            display.show_image(IMG_FOLDER / files[index])

        print("Select a image by turning the knob")
        rotor.when_rotated = change_image

        done.wait()
        display.clean_up()
        display.exit()
    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        display.exit()


if __name__ == "__main__":
    main()
