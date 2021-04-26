#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO


def main(args):
    print("Hello buzzer..")
    
    try:
        GPIO.setmode(GPIO.BCM)

        pin_buzzer = 17

        #initial : output 0
        GPIO.setup(pin_buzzer,GPIO.OUT,initial=GPIO.LOW)
        pwm = GPIO.PWM(pin_buzzer,100)
        
        scale = [261,294,329,349,392,440,493,523]
        lst = [4,4,5,5,4,4,2, 4,4,2,2,1, 4,4,5,5,4,4,2, 4,2,1,2,0]
        
        for i,item in enumerate(lst):
            print(scale[item])
            pwm.start(100)
            pwm.ChangeDutyCycle(90)
            pwm.ChangeFrequency(scale[item])
            if i==6 or i==11 or i==18 or i==23:
                time.sleep(1)
            else :
                time.sleep(0.5)
            pwm.stop()
            
            
        
    except KeyboardInterrupt as e:
        print(e)
    finally:
        pwm.stop()
        print("finally....GPIO.cleanup()")
        GPIO.cleanup()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
