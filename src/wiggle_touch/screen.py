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

# Raspberry Pi pin configuration for LCD:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.ERROR)

# Collect images
BASE_FOLDER = Path.home() / 'WiggleR'
IMG_FOLDER = BASE_FOLDER / "Pictures" / "small"

def list_files(folder):
    return sorted(os.listdir(folder))

files = list_files(IMG_FOLDER)

imageCount = len(files) - 1

# Show first image
disp = LCD_2inch.LCD_2inch()
disp.Init()
disp.clear()

image = Image.open(
    IMG_FOLDER / files[imageCount]
)
image = image.rotate(180)
disp.ShowImage(image)

# Listen to rotary
rotor = RotaryEncoder(17, 23, wrap=True, max_steps=imageCount)
done = Event()

def change_image():
    index = imageCount + rotor.steps if rotor.steps < 0 else rotor.steps
    print(f'Show image at index {index} with name {files[index]}')
    image = Image.open(IMG_FOLDER / files[index])
    image = image.rotate(180) # TODO: Check if this line can be removed
    disp.ShowImage(image)

print('Select a image by turning the knob')
rotor.when_rotated = change_image

done.wait()

GPIO.cleanup()
disp.module_exit()