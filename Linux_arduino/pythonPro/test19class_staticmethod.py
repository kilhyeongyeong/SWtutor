#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

#@staticmethod : self less method(function,def)
class Person:
	def __init__(self):
		print("Person : __init__()")
	
	@staticmethod
	def sum():
		print("Person : sum()")
	
p = Person()
p.sum()
