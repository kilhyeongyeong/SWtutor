#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

class Score:
	def __init__(self,name,kor,eng,math):
		print("Score : __init__()")
		self.__name = name
		self.__kor = kor
		self.__eng = eng
		self.__math = math
	
	@property   #def >> like attribute >> getter
	def name(self):
		return self.__name	
	
	@name.setter  #def >> like attribute >> setter
	def name(self,name):
		self.__name = name
		
	#kor,eng,math create getters and setters
	

s = Score("kim",11,22,33)
print(vars(s))
#print(s.__name) #error
s._Score__name = "yangssem"
print(s._Score__name)
print(s.name)
s.name = "lee"
print(s.name)


