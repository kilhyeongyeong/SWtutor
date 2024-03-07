#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

class ScoreVO:
	def __init__(self):
		print("ScoreVO : __init__(self)...")
		self.name = "kim"
		self.kor = 99
		self.eng = 88
		self.math = 77
	def getTotal(self):
		return self.kor+self.eng+self.math
	
s = ScoreVO()
print(vars(s))
print(s.name,s.kor+s.eng+s.math)
print(s.name,s.getTotal())
################################

class Person:
	def __init__(self,name,email,tel):
		print("Person : __init__(self)...")
		self.name = name
		self.email = email
		self.tel = tel
	
	def getName(self):
		return self.name	
	def setName(self,name):
		self.name = name

p = Person("kim","bbb@bbb.com","02")
print(vars(p))
p.name = "yangssem"
p.setName("python")
print("p.name:",p.name)
print("p.getName():",p.getName())
print(p.email)
print(p.tel)


