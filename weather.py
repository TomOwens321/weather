#!/usr/bin/env python3
from windvane.bb_windvane import BBWindvane as BBW
from time import sleep

def run():
    bbw = BBW()
    bbw.setup()
    while (1):
        dir = bbw.direction_text(bbw.read())
        print("Current Wind Direction: {}").format(dir)
        sleep(5)

if __name__ == '__main__':
    run()