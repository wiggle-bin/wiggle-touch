import os
from pathlib import Path

BOOTH_FILE = 'wiggle_touch_boot.sh'
SERVICE_FILE = 'wiggle_touch.service'

def install():
    scriptFile = Path(__file__).parent / f"service/{BOOTH_FILE}"
    serviceFile = Path(__file__).parent / f"service/{SERVICE_FILE}"
    os.system(f'sudo cp {scriptFile} /usr/bin/{BOOTH_FILE}')
    os.system(f'sudo cp {serviceFile} /etc/systemd/user/{SERVICE_FILE}')
    os.system('systemctl --user enable {SERVICE_FILE}')
    os.system('systemctl --user start {SERVICE_FILE}')