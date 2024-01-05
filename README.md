# WiggleTouch

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