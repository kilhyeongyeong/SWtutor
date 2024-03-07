#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

LED = 4

def main(args):
    print("Hello python")
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(LED,GPIO.OUT)
    try:
        while True:
            GPIO.output(LED, True)
            time.sleep(1)
            GPIO.output(LED, False)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("cleanup")
        
    print("end main")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
