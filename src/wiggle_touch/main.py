#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import chardet

from threading import Event
from gpiozero import RotaryEncoder, Button
from wiggle_touch import screen_menu
from wiggle_touch.display import Display

def main():
    try:
        btn = Button(2)
        rotor = RotaryEncoder(17, 23)
        display = Display()
        
        done = Event()
        screen_menu.show(btn, rotor, display)
        done.wait()

        display.clean_up()
        display.exit()
    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        display.exit()


if __name__ == "__main__":
    main()
