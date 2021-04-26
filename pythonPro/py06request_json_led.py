#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import random
import json
import requests

led_green = 4
led_red = 22
led_yellow = 17

def main(args):

    GPIO.setmode(GPIO.BCM) #GPIO.BOARD:40pin NO
    GPIO.setup(led_red,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(led_green,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(led_yellow,GPIO.OUT,initial=GPIO.LOW)

    '''
    https://tomcat.apache.org/download-90.cgi
    download >> apache-tomcat-9.0.45.tar.gz
    tar -zxvf apache-tomcat-9.0.45.tar.gz
    ls >> sudo mv apache-tomcat-9.0.45 tomcat9
    sudo mv tomcat9 /usr/local
    cd ~
    ln -s /usr/local/tomcat9 tomcat9
    ls -l
    tomcat9 -> /usr/local/tomcat9
    sudo apt install openjdk-11-jdk
    javac
    which javac 
    >>> /usr/bin/javac
    readlink -f /usr/bin/javac
    >>>/usr/lib/jvm/java-11-openjdk-armhf/bin/javac

    sudo vim /etc/profile
    end line >>> insert
    export JAVA_HOME = /usr/lib/jvm/java-11-openjdk-armhf

    cd ~
    sudo tomat9/bin/shutdown.sh
    sudo tomat9/bin/startup.sh
    http://localhost:8080 

    vim test.txt
    ["red","green","yellow"]
    http://192.168.1.3:8080/test.txt

    *****raspberry ftp server setup
    sudo apt install proftpd
    sudo vim /etc/proftpd/proftpd.conf  
    port check 21 OK?
    sudo service proftpd reload
    ifconfig
    192.168.1.2

    windows FTP app download:FileZilla
    host: 192.168.1.3
    user:pi
    pw:hi123456
    port:21
    speed connect click

    '''
    #http://192.168.159.1:8090/web01/color.do
    #http://192.168.1.2:8080/test.txt
    #http://192.168.1.2:8080/web01/test.txt
    #import requests
    try:
        response = requests.get("http://192.168.1.2:8080/web01/test.txt")
    except:
        print("Check Server Start")
    else:
        txt_response = response.content
        lst = txt_response.decode("utf-8")
        #lst = '["red","green","yellow"]'
        #import json
        
        lst = json.loads(lst)
        print(lst)
        print(type(lst))    

        try:
            while True:
                random.shuffle(lst)
                color = random.choice(lst)
                
                if color == "red":
                    print("RED")
                    GPIO.output(led_red,True)
                    GPIO.output(led_green,False)
                    GPIO.output(led_yellow,False)                
                elif color == "green":
                    print("GREEN")
                    GPIO.output(led_red,False)
                    GPIO.output(led_green,True)
                    GPIO.output(led_yellow,False)
                elif color == "yellow":
                    print("YELLOW")
                    GPIO.output(led_red,False)
                    GPIO.output(led_green,False)
                    GPIO.output(led_yellow,True)
                time.sleep(0.5)

        except KeyboardInterrupt as e:
            print(e)
    finally:
            GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
