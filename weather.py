#!/usr/bin/env python3
from windvane.bb_windvane import BBWindvane as BBW
from time import sleep

def run():
    bbw = BBW()
    bbw.setup()
    while (1):
        raw = bbw.read()
        dir = bbw.direction_text(raw)
        print("Current Wind Direction: %s  (%f)" % (dir, raw))
        sleep(5)

if __name__ == '__main__':
    run()
