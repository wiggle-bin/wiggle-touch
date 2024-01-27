# WiggleTouch


## Start WiggleTouch on boot of RPI

In the terminal run `wiggle_touch_install`. This will install and start a service which runs `wiggle_touch` on boot.

```
wiggle_touch_install
```


You can check the status with:

```
systemctl --user status wiggle_touch.service
```

To stop the service run:

```
systemctl --user stop wiggle_touch.service
```

To start the service run:

```
systemctl --user start wiggle_touch.service
```

## Installation for development

Updating packages on Raspberry Pi
```
pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
apt-get install libjpeg-dev zlib1g-dev
```

Installing package
```
pip3 install -e .
```

For installation without dev dependencies
```
pip install --no-dev -r requirements.txt
```