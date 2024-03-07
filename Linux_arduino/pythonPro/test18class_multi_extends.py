#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])


class Person:
	pname = "aaa"
	def __init__(self):
		print("Person : __init__()")
		self.pname = "kim"

	def setPname(self,pname):
		self.pname = pname
	
	def getPname(self):
		return self.pname

class Korean:
	ssn = "881212-1234567"
	def __init__(self):
		print("Korean : __init__()")
		
	def getLocation(self):
		return "South Korea"

class Students(Person,Korean):
	def __init__(self):
		print("Students : __init__()")

st = Students()
print(st.pname)
print(st.ssn)
st.setPname("lee")
print(st.getPname())
print(st.getLocation())

print(Students.__bases__)
print(issubclass(Students,Korean))
print(issubclass(Students,Person))





