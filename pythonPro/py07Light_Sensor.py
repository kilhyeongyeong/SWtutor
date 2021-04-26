#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
light_sensor = 4
led_red = 17

def fn(light_sensor):
    count = 0
    
    #initial : output 0
    GPIO.setup(light_sensor, GPIO.OUT)
    GPIO.output(light_sensor, GPIO.LOW)
    time.sleep(0.1)
    
    #change input
    GPIO.setup(light_sensor, GPIO.IN)
    
    while(GPIO.input(light_sensor)==GPIO.LOW):
        count += 1
    
    
    return count
    
def main(args):
    print("Hello Light Sensor")
    
    GPIO.setup(led_red,GPIO.OUT,initial=GPIO.LOW)
    try:
        while True:
            
            res = fn(light_sensor)
            print(res)
            
            if res >= 4000:
                GPIO.output(led_red,True)
            else:
                GPIO.output(led_red,False)
            
    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("finally....GPIO.cleanup()")
        GPIO.cleanup()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
