#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 

import sys

print('Hello sys')
print("Hello if")

#import sys


print("list length:",len([11,22,33]))
print("str length:",len("yangssem"))
print("sys.argv length:",len(sys.argv))
#python3 test03sys_if.py 11 22 33
if len(sys.argv)==4:
	print("message:",sys.argv[0]) #test03sys_if.py
	print("message:",sys.argv[1]) #11
	print("message:",sys.argv[2]) #22
	print("message:",sys.argv[3]) #33

#sys.stdin.readline()
print("input your name:")
name = sys.stdin.readline()
print("sys.stdin.readline()>>name:",name)

#input() : scanf(), read, br.readLine()
print("input your name:")
name = input()
print("input()>>name:",name)
print("name:{},{}".format(name,"hi"))

if True:
	print("name:{},{}".format(name,"hi11"))
else:
	print("name:{},{}".format(name,"hi22"))
	
a = 3
print(a)
print("type(a):",type(a))
print(float(a))
print("type(float(a)):",type(float(a)))

b = 33.33
print(b)
print("type(b):",type(b))
print(int(b))
print("type(int(b):",type(int(b)))

c = "99"
#print(c + 100) #typeError
print(c)
print("type(c):",type(c))
print(int(c))
print("type(int(c):",type(int(c)))
print(int(c) + 100)

d = "99"
if int(d)==99:
	print("AAA")
elif int(d)==90:
	print("BBB")
elif int(d)==80:
	print("CCC")
else:	
	print("DDD")
	
#switch case Not
