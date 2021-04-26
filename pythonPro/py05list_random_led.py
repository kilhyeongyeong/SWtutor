#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import random

YELLOW = 17
GREEN = 4
RED = 22

def main(args):
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(YELLOW,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(GREEN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(RED,GPIO.OUT,initial=GPIO.LOW)
    print()
    
    #http://192.168.?.?:8090/web01/color.do
    lst = ["red", "green", "yellow"]
    try:
        while True:
            random.shuffle(lst)
            color = random.choice(lst)
            print(color)
            if color == "yellow":
                GPIO.output(YELLOW, True)
                GPIO.output(GREEN, False)
                GPIO.output(RED, False)
            elif color == "green":
                GPIO.output(YELLOW, False)
                GPIO.output(GREEN, True)
                GPIO.output(RED, False)
            elif color == "red":
                GPIO.output(YELLOW, False)
                GPIO.output(GREEN, False)
                GPIO.output(RED, True)
            time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
        print("cleanup")
    finally:
        GPIO.output(YELLOW, False)
        GPIO.output(GREEN, False)
        GPIO.output(RED, False)
        GPIO.cleanup()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
