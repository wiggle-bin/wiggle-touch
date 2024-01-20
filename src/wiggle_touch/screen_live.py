from pathlib import Path
from wiggle_touch import screen_menu
from wiggle_touch.data_images import Images
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from wiggle_touch.display import Display

BASE_FOLDER = Path.home() / "WiggleR"
IMG_FOLDER = BASE_FOLDER / "Pictures"


class WatchImagesHandler(FileSystemEventHandler):
    def __init__(self, display):
        super().__init__()
        self.display = display

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file created: {event.src_path}")
        self.display.show_image(event.src_path)


def watch_folder(folder_path, btn, display):
    event_handler = WatchImagesHandler(display)
    observer = Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()
    try:
        while True:
            if btn.is_pressed:
                print("Stopping observer...")
                observer.stop()
                break
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    return observer


def show(btn, rotor, display):
    def show_menu():
        screen_menu.show(btn, rotor, display)

    images = Images()

    # Show most recent image on startup
    display.show_image(images.last)

    watch_folder(IMG_FOLDER, btn, display)

    btn.when_released = show_menu


if __name__ == "__main__":
    watch_folder(IMG_FOLDER, Display())
