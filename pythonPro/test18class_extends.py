#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

# java : class Person extends Object{ }
# python : class Person(object):
class Person:
	pname = "aaa"
	def __init__(self):
		print("Person : __init__()")
		self.pname = "kim"

	def setPname(self,pname):
		self.pname = pname
	
	def getPname(self):
		return self.pname
	

p = Person()
print("p.pname:",p.pname)
#p.setPname("yangssem") and p.getPname()
p.setPname("yangssem")
print(vars(p))
print(p.getPname())
######################################
print("=====================")

class Students(Person):
	def __init__(self):
		print("Students : __init__()")

st = Students()
print(vars(st))
print("st.pname:",st.pname)
st.setPname("python")
print("st.getPname():",st.getPname())

print(Person.__bases__) #return super class name:(<class 'object'>,)

print(Students.__bases__) #(<class '__main__.Person'>,)

print(issubclass(Person,object)) #True
print(issubclass(Students,Person)) #True
		
		
		
		
		
		
