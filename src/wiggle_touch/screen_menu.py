import os
from wiggle_touch import screen_images, screen_live, screen_picture
from wiggle_touch.data_menu import Menu, MenuAction, MenuParent
from wiggle_settings.main import monitor_settings_file, read_settings, update_setting

def show(btn, rotor, display):
    def reset_listeners():
        rotor.when_rotated_clockwise = None
        rotor.when_rotated_counter_clockwise = None
        btn.when_released = None

    def show_images():
        reset_listeners()
        screen_images.show(btn, rotor, display)

    def show_live():
        reset_listeners()
        screen_live.show(btn, rotor, display)

    def show_picture():
        reset_listeners()
        screen_picture.show(btn, rotor, display)

    def toggle_light():
        settings = read_settings()
        print("Toggle light", settings)
        if settings["light"] == "off":
            update_setting('light', 'on')
        else:
            update_setting('light', 'off')

    def toggle_recording():
        settings = read_settings()
        if settings["recording"] == "off":
            print("Start recording")
            update_setting('recording', 'on')
        else:
            print("Stop recording")
            update_setting('recording', 'off')

    def action_list():
        settings = read_settings()
        return [
            MenuAction("Record", toggle_recording, settings['recording']),
            MenuAction("Picture", show_picture),
            MenuAction("Tag", lambda: os.system("wiggle --tag")),
            MenuAction("Light", toggle_light, settings['light']),
            MenuAction("Images", lambda: show_images()),
            MenuAction("Live", lambda: show_live()),
            MenuParent(
                "Settings",
                [
                    MenuAction("Light color", lambda: print("... to be implemented")),
                    MenuAction("Image mode", lambda: print("... to be implemented")),
                ],
            )
        ]
    
    menu_list = action_list()

    menu = Menu(
        menu_list,
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

    def update_menu_settings():
        print("Settings changed, updating menu")
        menu_list = action_list()
        menu.update_options(menu_list)
        menu.render()

    print("Select a menu item by turning the knob")
    rotor.when_rotated_clockwise = change_menu_down
    rotor.when_rotated_counter_clockwise = change_menu_up
    btn.when_released = select_menu_item

    # listen to setting changes and update the menu
    monitor_settings_file(update_menu_settings)