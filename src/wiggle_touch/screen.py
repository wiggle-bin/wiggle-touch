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

logging.basicConfig(level=logging.CRITICAL)


def main():
    try:
        images = Images()
        display = Display()

        # Show most recent image on startup
        display.show_image(images.last)

        # Listen to rotary
        rotor = RotaryEncoder(17, 23, wrap=True, max_steps=images.count)
        done = Event()

        def change_image():
            index = images.count + rotor.steps if rotor.steps < 0 else rotor.steps
            display.show_image(images[index])

        print("Select a image by turning the knob")
        rotor.when_rotated = change_image

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
