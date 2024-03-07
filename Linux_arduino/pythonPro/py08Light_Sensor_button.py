#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
light_sensor = 4
led = 17
button01 = 22
button02 = 27

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
    prev1 = 0
    prev2 = 0
    print("Hello Light Sensor")
    
    GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(button01,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button02,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while True:
            if GPIO.input(button01) == 1:
                print("start")
                prev1 = 1
                prev2 = 0
            
            if prev1 == 1:
                while True:
                    if GPIO.input(button02) == 1:
                        print("end")
                        prev2 = 1
                        prev1 = 0
                        break
                        
                    res = fn(light_sensor)
                    print(res)
                    
                    if res >= 4000:
                        GPIO.output(led,True)
                    else:
                        GPIO.output(led,False)
                    
    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("finally....GPIO.cleanup()")
        GPIO.cleanup()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
