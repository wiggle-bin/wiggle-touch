from wiggle_touch import screen_menu
from wiggle_touch.data_images import Images


def show(btn, rotor, display):
    def reset_listeners():
        rotor.when_rotated_clockwise = None
        rotor.when_rotated_counter_clockwise = None
        btn.when_released = None

    def show_menu():
        reset_listeners()
        screen_menu.show(btn, rotor, display)

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
    btn.when_released = show_menu
