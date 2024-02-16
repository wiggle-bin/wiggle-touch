import time
import board
import busio
import digitalio
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display import color565
from PIL import Image, ImageDraw
# Create the SPI bus
spi = busio.SPI(clock=board.SCLK, MOSI=board.MOSI, MISO=board.MISO)

# Create the CS (Chip Select), DC (Data/Command), Reset, and BL (Backlight) pins
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)

# Create the display object
display = st7789.ST7789(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, width=240, height=320, rotation=90, baudrate=24000000)

image = Image.new("RGB", (320, 240))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, 320, 240), outline=0, fill=(0, 0, 0))
display.image(image)

# Load an image file
image_path = "./LCD_2inch.jpg"
image = Image.open(image_path).resize((320, 240), Image.BICUBIC)

# Display the image
display.image(image)

time.sleep(2)
display.image(image)

time.sleep(2)
display.fill(color565(0, 0, 255))

time.sleep(2)
display.image(image)

time.sleep(2)
display.fill(color565(0, 0, 255))

time.sleep(5)