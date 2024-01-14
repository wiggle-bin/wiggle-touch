import os
from wiggle_touch import screen_images
from wiggle_touch.data_menu import Menu, MenuAction, MenuParent


def show(btn, rotor, display):
    def reset_listeners():
        rotor.when_rotated_clockwise = None
        rotor.when_rotated_counter_clockwise = None
        btn.when_released = None

    def show_images():
        reset_listeners()
        screen_images.show(btn, rotor, display)

    menu = Menu(
        [
            MenuParent(
                "Record",
                [
                    MenuAction("On", lambda: os.system("wiggler --recording start")),
                    MenuAction("Off", lambda: os.system("wiggler --recording stop")),
                ],
            ),
            MenuParent(
                "Experiment",
                [
                    MenuAction("Start", lambda: os.system("wiggler --experiment start")),
                    MenuAction("Stop", lambda: os.system("wiggler --experiment stop")),
                ],
            ),
            MenuParent(
                "Light",
                [
                    MenuAction("On", lambda: os.system("sudo wiggler --light")),
                    MenuAction("Off", lambda: os.system("sudo wiggler --light-off")),
                ],
            ),
            MenuAction("Images", lambda: show_images()),
        ],
        display,
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
