#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import chardet

from wiggle_touch.menu import Menu, MenuAction, MenuParent
from threading import Event
from gpiozero import RotaryEncoder, Button


def main():
    try:
        btn = Button(2)
        menu = Menu(
            [
                MenuAction("First line", lambda: print("First line")),
                MenuAction("A second menu option", lambda: print("Second line")),
                MenuParent(
                    "Now to the third",
                    [
                        MenuAction(
                            "First sub-option", lambda: print("First sub-option")
                        ),
                        MenuAction(
                            "Second sub-option", lambda: print("Second sub-option")
                        ),
                        MenuParent(
                            "Third sub-option",
                            [
                                MenuAction(
                                    "First sub-sub-option",
                                    lambda: print("First sub-sub-option"),
                                ),
                                MenuAction(
                                    "Second sub-sub-option",
                                    lambda: print("Second sub-sub-option"),
                                ),
                            ],
                        ),
                        MenuAction(
                            "Fourth sub-option", lambda: print("Fourth sub-option")
                        ),
                    ],
                ),
                MenuAction("On to the forth", lambda: print("Fourth option")),
                MenuAction("Follow the fifth", lambda: print("Fifth option")),
                MenuAction("Support the sixth", lambda: print("Sixth option")),
            ]
        )

        menu.render()

        rotor = RotaryEncoder(17, 23)
        done = Event()

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
        btn.when_pressed = select_menu_item

        done.wait()

        menu.display.clean_up()
        menu.display.exit()
    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        menu.display.exit()


if __name__ == "__main__":
    main()
