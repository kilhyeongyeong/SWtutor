#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

YELLOW = 17
GREEN = 4
RED = 22

def main(args):
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(YELLOW,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(GREEN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(RED,GPIO.OUT,initial=GPIO.LOW)
    print()
    
    try:
        while True:
            print("input color(red, yellow, green, exit)")
            color = input()
            
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
            elif color == "exit":
                GPIO.output(YELLOW, False)
                GPIO.output(GREEN, False)
                break
            else:
                print("Not color")
                GPIO.output(YELLOW, False)
                GPIO.output(GREEN, False)
                GPIO.output(RED, False)
    except KeyboardInterrupt as e:
        print(e)
        print("cleanup")
    finally:
        GPIO.cleanup()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
