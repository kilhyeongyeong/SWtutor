#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

#@classmethod : class name access method(function,def)
#               All arguments is static variable
class Person:
	def __init__(self):
		print("Person : __init__()")
	
	@classmethod
	def sum(cls):
		print("Person : sum()")
		
	@classmethod
	def create_classmethod(cls):
		print("Person : create_classmethod()")
		cls.name = "kim"
		
	@classmethod
	def create_classmethod2(cls,name):
		print("Person : create_classmethod2()")
		cls.name = name
		
		
	
Person.sum()
Person.create_classmethod()
print(Person.name)
Person.create_classmethod2("yangssem")
print(Person.name)
