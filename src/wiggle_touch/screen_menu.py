#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import chardet

import os
from wiggle_touch.display import Display
from wiggle_touch.images import Images
from wiggle_touch.menu import Menu, MenuAction, MenuParent
from threading import Event
from gpiozero import RotaryEncoder, Button

def display_images(btn, rotor, display):
    def reset_listeners():
        rotor.when_rotated_clockwise = None
        rotor.when_rotated_counter_clockwise = None
        btn.when_released = None

    def back_to_menu():
        reset_listeners()
        display_menu(btn, rotor, display)

    images = Images()

    # Show most recent image on startup
    display.show_image(images.last)

    def next_image():
        display.show_image(images.next())

    def prev_image():
        display.show_image(images.prev())

    print("Select a image by turning the knob")
    rotor.when_rotated_clockwise = next_image
    rotor.when_rotated_counter_clockwise = prev_image
    btn.when_released = back_to_menu

def display_menu(btn, rotor, display):
    def reset_listeners():
        rotor.when_rotated_clockwise = None
        rotor.when_rotated_counter_clockwise = None
        btn.when_released = None

    def show_display():
        reset_listeners()
        display_images(btn, rotor, display)

    menu = Menu(
        [
            MenuParent(
                "Record",
                [
                    MenuAction(
                        "Start", lambda: os.system('wiggler --recording start')
                    ),
                    MenuAction(
                        "Stop", lambda: os.system('wiggler --recording stop')
                    )
                ],
            ),
            MenuAction("Images", lambda: show_display()),
        ],
        display
    )

    menu.render()

    def change_menu_down():
        menu.change_highlight(1)
        menu.render()

    def change_menu_up():
        menu.change_highlight(-1)
        menu.render()

    def select_menu_item():
        menu.perform_current_action()

    print("Select a menu item by turning the knob")
    rotor.when_rotated_clockwise = change_menu_down
    rotor.when_rotated_counter_clockwise = change_menu_up
    btn.when_released = select_menu_item

def main():
    try:
        btn = Button(2)
        rotor = RotaryEncoder(17, 23)
        display = Display()
        
        done = Event()
        display_menu(btn, rotor, display)
        done.wait()

        display.clean_up()
        display.exit()
    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        display.exit()


if __name__ == "__main__":
    main()
