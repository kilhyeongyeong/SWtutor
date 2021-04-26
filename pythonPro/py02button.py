#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

BUTTON = 27

def main(args):
    print("Hello python")
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while True:
            bt = GPIO.input(BUTTON)
            print("bt :", bt)
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("cleanup")
        
    print("end main")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
