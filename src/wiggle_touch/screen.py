#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import chardet
import os
import sys
import logging
import spidev as SPI
from pathlib import Path
from threading import Event
from gpiozero import RotaryEncoder
sys.path.append("..")
from wiggle_touch.lib import LCD_2inch
from PIL import Image
from RPi import GPIO

# Pin configuration for LCD screen
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.ERROR)

# Collect images
BASE_FOLDER = Path.home() / 'WiggleR'
IMG_FOLDER = BASE_FOLDER / "Pictures"

def list_files(folder):
    return sorted(os.listdir(folder))

files = list_files(IMG_FOLDER)

imageCount = len(files) - 1

# Setup display
disp = LCD_2inch.LCD_2inch()
disp.Init()
disp.clear()

def show_image(index):
    print(f'Show image at index {index} with name {files[index]}')
    try:
        with Image.open(IMG_FOLDER / files[index]) as image:
            disp.ShowImage(image.resize((320, 240)).rotate(180))
    except Exception as e:
        print(f"Unable to open image {files[index]}.")
        print(f"Error details: {str(e)}")

# Show most recent image on startup
show_image(imageCount)

# Listen to rotary
rotor = RotaryEncoder(17, 23, wrap=True, max_steps=imageCount)
done = Event()

def change_image():
    index = imageCount + rotor.steps if rotor.steps < 0 else rotor.steps
    show_image(index)

print('Select a image by turning the knob')
rotor.when_rotated = change_image

done.wait()

GPIO.cleanup()
disp.module_exit()