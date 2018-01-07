#!/usr/bin/env python

import colorsys
import time

import blinkt
import signal, sys

spacing = 360.0 / 16.0
hue = 0
running = True

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

def sigterm_handler(signal, frame):
    print "Signal caught, killing gracefully"
    global running
    running = False
signal.signal(signal.SIGTERM, sigterm_handler)

while running:
    hue = int(time.time() * 100) % 360
    for x in range(blinkt.NUM_PIXELS):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        blinkt.set_pixel(x, r, g, b)

    blinkt.show()
    time.sleep(0.03)
