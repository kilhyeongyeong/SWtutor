#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
print('Hello for')
print("Hello for")

print("===range(10)====",end=":")
for i in range(10) :
	print(i,end=" ")
print()

print("===range(10,20)====",end=":")
for i in range(10,20) :
	print(i,end=" ")
print()

print("===range(10,20)====",end=":")
for i in range(10,20) :
	print("{}*{}={}".format(i,10,i*10),end=" ")
print()

#9*9 dan
print("===9*9 dan====")
for x in range(2,10) :
	for i in range(1,10) :
		print("{}*{}={}".format(x,i,x*i),end=" ")
	print()	
		
#list >>array(java,c,js,c#) : [,,,,]
for item in [11,22,33]:
	print(item)



