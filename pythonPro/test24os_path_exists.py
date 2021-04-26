#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import os

print('Hello ',sys.argv[0])

#os.system, os.path, os.path.exists

#linux shell command
os.system("pwd")
os.system("ls -l")

######################
print("===================")
print("os.path.exists:",os.path.exists("/home/pi/pythonPro"))
print("os.path.exists:",os.path.exists("/home/pi/pythonPro/test00temp.py"))


######################
print("===================")
print("os.path.dirname:",os.path.dirname("/home/pi/pythonPro"))
print("os.path.dirname:",os.path.dirname("/home/pi/pythonPro/test00temp.py"))


######################
print("=====isfile==============")
print("os.path.isfile:",os.path.isfile("/home/pi/pythonPro"))
print("os.path.isfile:",os.path.isfile("/home/pi/pythonPro/test00temp.py"))

######################
print("=====isdir==============")
print("os.path.isdir:",os.path.isdir("/home/pi/pythonPro"))
print("os.path.isdir:",os.path.isdir("/home/pi/pythonPro/test00temp.py"))


######################
print("========getsize===========")
print("os.path.getsize:",os.path.getsize("/home/pi/pythonPro"))
print("os.path.getsize:",os.path.getsize("/home/pi/pythonPro/test00temp.py"))


#https://docs.python.org/3/library/index.html
#https://docs.python.org/3/library/os.path.html


