#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import chardet
import sys
from threading import Event
from gpiozero import RotaryEncoder

sys.path.append("..")
from wiggle_touch.images import Images
from wiggle_touch.display import Display
import logging
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.CRITICAL)

max_steps = 20


def main():
    try:
        display = Display()

        # Listen to rotary
        rotor = RotaryEncoder(17, 23, wrap=True, max_steps=max_steps)
        done = Event()

        def change_menu():
            index = max_steps + rotor.steps if rotor.steps < 0 else rotor.steps
            display.show_menu_item(f"Item {index}")
            print("menu item", index)

        print("Select a menu item by turning the knob")
        rotor.when_rotated = change_menu

        done.wait()

        # Display clean up
        display.clean_up()
        display.exit()
    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        display.exit()


if __name__ == "__main__":
    main()
