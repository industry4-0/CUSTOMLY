import logging
import time
from collections import namedtuple

import colorutils
import digitalio

try:
    import board
except NotImplementedError:
    logging.error("Board is not implemented")
    pass

import neopixel

Color = namedtuple('Color', 'r g b')

color_leds = 14


class ColoredLed:

    def __init__(self, pixels, index):
        self.pixels = pixels
        self.index = index
        self.color = Color(0, 0, 0)

    def turn_off(self):
        self.pixels[self.index] = (0, 0, 0)

    def set_color(self, color):
        self.pixels[self.index] = (color.g, color.r, color.b)
        self.color = color
        logging.info("Setting color for led: {} to {}".format(self.index, self.color))
        time.sleep(1)

    def add_color(self, color):
        current_color = colorutils.Color((self.color.r, self.color.g, self.color.b))
        new_color = colorutils.Color((color.r, color.g, color.b))
        color = current_color + new_color
        color = Color(color.red, color.green, color.blue)
        self.set_color(color)


class Led:

    def __init__(self, pin):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.OUTPUT
        self.turn_off()

    def turn_off(self):
        self.pin.value = False

    def turn_on(self):
        self.pin.value = True

    def toogle(self):
        self.pin.value = not self.pin.value


class LedController:

    def __init__(self):
        self.pixels = neopixel.NeoPixel_SPI(board.SPI(), color_leds, brightness=0.5, pixel_order=neopixel.RGB)
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        time.sleep(1)
        self.colored_leds = list()
        for i in range(color_leds):
            self.colored_leds.append(ColoredLed(self.pixels, i))

        self.leds = list()
        self.leds.append(Led(board.D6))
        self.leds.append(Led(board.D13))
        self.leds.append(Led(board.D19))
        self.leds.append(Led(board.D26))

    def get_colored_led(self, index):
        return self.colored_leds[index]

    def get_led(self, index):
        return self.leds[index]


controller = LedController()
i = 0
j = 0
for i in range(color_leds):
    controller.get_colored_led(i).set_color(Color(255, 255, 255))
for i in reversed(range(color_leds)):
    controller.get_colored_led(i).set_color(Color(0, 0, 0))
