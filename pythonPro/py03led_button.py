#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

BUTTON = 27
LED = 4
prev = 0

def main(args):
    print("Hello python")
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED,GPIO.OUT)
    
    try:
        while True:
            if GPIO.input(BUTTON)==1:
                if prev == 0:
                    prev = 1
                    print("push")
                GPIO.output(LED, True)
                time.sleep(0.05)
            else:
                prev = 0
                GPIO.output(LED, False)
                time.sleep(0.05)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("cleanup")
    print("end main")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
