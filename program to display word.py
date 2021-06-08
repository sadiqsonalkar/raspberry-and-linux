import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
msg = "Hello"
print(msg)
show_message(device, msg, fill="white", font=proportional(CP437_FONT))
time.sleep(1)
