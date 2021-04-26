#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

#open(filename,option) : option(r:read,w:write)

#file input  : readline()
f = open("test14.txt","r")
while True:
	data = f.readline()
	if not data:
		break
	print(data,end="")
	
###########################

x = 10
y = "kim"
#data = x + y  #error  : int + str
data = str(x) + y  #OK  : str + str
print("data:",data)
data = str(x) +" "+ y+"\n"  #OK  : str + str
print("data:",data)
data = "{} {}\n".format(x,y)  #OK  : format(x,y)
print("data:",data)
data = "%d %s\n" %(x,y) #OK  : %(x,y)
print("data:",data)
###########################

names = ["kim","lee","yang","han"]
print(names)

#file write : output : write()
fw = open("test14fw.txt","w")
for i,item in enumerate(names):
	print(i,item)
	fw.write("%d %s\n" %(i,item))

###########################

fr = open("test14.txt","r")
lst = []
##1.readline()
#while True:
#	data = fr.readline()
#	if not data:
#		break
#	data = data.replace("\n","")
#	lst.append(data)

##2.readlines()
lst = fr.readlines()
print(lst)

f.close()
fr.close()
fw.close()


 
