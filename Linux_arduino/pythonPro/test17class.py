#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

class MemberVO:
	#userName = "yangssem"   
	
	def __init__(self):
		print("__init__(self)...")
		userName = "kim"   #local variable
		print("__init__(self)...",userName)
		#print("__init__(self)...",self.userName)
		self.userName = "kim"   #self variable
		print("__init__(self)...",self.userName)

m = MemberVO()  #call __init__()
print("m.userName:",m.userName)
print("type(m):",type(m))  #<class '__main__.MemberVO'>
print("vars(m):",vars(m))  #{'userName': 'kim'}
print("type(vars(m)):",type(vars(m)))  #class dict





