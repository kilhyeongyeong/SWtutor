#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

class Member:
	def __init__(self):
		print("Member : __init__(self)")
		self.__id = "admin"  #private __(under bar *2)
		self.__pw = "hi123456"

m = Member()
print(vars(m))
#print(m.__id) #error : has no attribute
print(m._Member__id) #  OK

m.__id = "tester"  #new create __id
print(vars(m))

print(dir(Member))
print(dir(m))
