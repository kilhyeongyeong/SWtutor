#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import os

print('Hello ',sys.argv[0])

x,y = (11,22)
print(x,y)

tp = os.pipe()  #tuple type
print("os.pipe():",tp)
receive,transmit = tp

print("receive:",receive)
print("transmit:",transmit)

data = "yangssem12345"

print("data_length:",os.write(transmit,data.encode()))


re_data = os.read(receive,1024)
print(re_data)
print(re_data.decode("utf-8"))


