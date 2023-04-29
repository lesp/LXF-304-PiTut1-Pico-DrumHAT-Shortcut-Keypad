import board
from adafruit_cap1188.i2c import CAP1188_I2C
import busio
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl


i2c = busio.I2C(board.GP17, board.GP16)
cap = CAP1188_I2C(i2c, 0x2c)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
consumer = ConsumerControl(usb_hid.devices)

while True:
    if cap[1].value:
        keyboard.send(Keycode.B)
        print("B pressed")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[2].value:
        keyboard.send(Keycode.RIGHT_ARROW)
        print("Right arrow pressed")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[3].value:
        consumer.send(ConsumerControlCode.MUTE)
        print("MUTED")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[4].value:
        keyboard.send(Keycode.UP_ARROW)
        print("Up arrow pressed")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[5].value:
        keyboard.send(227)
        print("Super / Windows key pressed")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[6].value:
        keyboard.send(Keycode.LEFT_ARROW)
        print("Left arrow pressed")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[7].value:
        keyboard.send(Keycode.A)
        print("A pressed")
        keyboard.release_all()
        time.sleep(0.3)
    if cap[8].value:
        keyboard.send(Keycode.DOWN_ARROW)
        print("Down arrow pressed")
        keyboard.release_all()
        time.sleep(0.3)
