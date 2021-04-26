#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import subprocess

print('Hello ',sys.argv[0])

#subprocess.call("ls -al | more",shell=True)



subprocess.call("sh ./test25.sh",shell=True)
print("==============================")

subprocess.call("echo hello subprocess",shell=True)
print("==============================")

msg = "hello python"
subprocess.call("echo {}".format(msg),shell=True)
print("==============================")

lst = [11,22,33]
subprocess.call("echo {}".format(lst[0]),shell=True)
print("==============================")

tp = ("test25.sh","test26.sh")
value = "cat {}".format(tp[0])
print(value)
subprocess.call(value,shell=True)
print("==============================")
