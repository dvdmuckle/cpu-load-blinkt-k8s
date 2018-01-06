#!/usr/bin/env python

import time
from sys import exit

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

import blinkt

running = True

blinkt.set_clear_on_exit()

def sigterm_handler(signal, frame):
    print "Signal caught, killing gracefully"
    global running
    running = False
signal.signal(signal.SIGTERM, sigterm_handler)

def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1

    blinkt.show()

blinkt.set_brightness(0.1)

while running:
    v = psutil.cpu_percent() / 100.0
    show_graph(v, 255, 255, 255)
    time.sleep(1)
