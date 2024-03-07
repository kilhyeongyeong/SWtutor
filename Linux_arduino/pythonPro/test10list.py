#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

lst = []
lst = [0,0,0,0]
lst = [1,2,3,4]

#fill 0: [0 for _ in range()]
lst = [0 for _ in range(10)]
print(lst)

lst = [1 for _ in range(10)]
print(lst)

#fill i: [i for i in range()]
lst = [i for i in range(10)]
print(lst)

#10~19
lst = [i for i in range(10,20)]
print(lst)

#0~90
lst = [i*10 for i in range(10)]
print(lst)

#n**2
lst = [i**2 for i in range(10)]
print(lst)

print(type(lst))
print(len(lst))

print(lst[-1],lst[0],lst[1],lst[2])

lst[0] = 100;
lst[1] = 1000;

lst.append(777)
lst.append(7777)
print("len(lst):",len(lst))

for item in lst:
	print(item, end=" ")
print()
##############################
lst.pop()
lst.pop()
print("len(lst):",len(lst))

for item in lst:
	print(item, end=" ")
print()
##############################
lst.insert(0,555)
lst.insert(0,555)
lst.insert(0,555)
lst.insert(8,5555)
print("len(lst):",len(lst))

for item in lst:
	print(item, end=" ")
print()

##############################
lst.remove(555) #first find item remove
lst.remove(81)
print("len(lst):",len(lst))

for item in lst:
	print(item, end=" ")
print()

##############################
del lst[3] #index delete
print("len(lst):",len(lst))

for item in lst:
	print(item, end=" ")
print()

##############################
lst.reverse()
print(lst)

##############################
lst.sort()
print(lst)
##############################
lst.reverse()
print(lst)

##############################
lst = [11,22,33] + [44,55,66]
lst = lst + [77,88,99]
print(lst)

##############################
lst = lst *2
print(lst)

##############################
#lst = lst + 1 #error
lst = lst + [1] 
print(lst)

print("=================")

txt='''aaaa 
bbb 
ccc'''
print(txt)
print(type(txt)) #<class 'str'>


#### list()
#lst = list()
#lst = list([0,0,0,0]) #list to list
lst = list((0,0,0,0)) #tuple to list
print(lst)
print(type(lst))
print(len(lst))

##### enumerate()
lst = ["kim","lee","yang","han"]
for tp in enumerate(lst):
	print(tp)

for index,value in enumerate(lst):
	print(index,value)


lst=[11,22,33,44,55,66]
print(lst[1])
print(lst[3])
print(lst[1:3])
lst[1:3] = [0,0,0]
print(lst)

print(lst[1:3])
lst[1:3] = []
print(lst)

#0~30, even value >> create list
#index 5~10,remove
#index last >> 100 change
lst = [i*2 for i in range(16)]
lst = [i for i in range(0,31,2)]
lst = [i for i in range(31) if i%2==0]
lst = [i for i in range(31) if bin(i)[-1]=="0"]
lst = [i for i in range(31) if i&1==0]
print(lst)
print("==========================")
lst[5:11] = []
print(lst)
lst[-1] = 100
print(lst)
#print("==========================")
#print(0,0&1,0&1==0) #0000 & 0001 : 0
#print(1,1&1,1&1==0) #0001 & 0001 : 1
#print(2,2&1,2&1==0) #0010 & 0001 : 0
#print(3,3&1,3&1==0) #0011 & 0001 : 1
#print("==========================")
#print(0,bin(0),bin(0)[-1],bin(0)[-1]=="0")
#print(1,bin(1),bin(1)[-1],bin(1)[-1]=="0")
#print(2,bin(2),bin(2)[-1],bin(2)[-1]=="0")
#print(3,bin(3),bin(3)[-1],bin(3)[-1]=="0")

#print([11,22,33][-1])
#print("kim"[-1])
#print("==========================")
#for i in range(20):
#	print(i,oct(i))
#print("==========================")
#for i in range(20):
#	print(i,hex(i))

print("==========================")
lst = [1,2,3,4,5]
print(lst)
lst.append(11)
print(lst)
lst.append([22,33,44])
print(lst)
lst.extend([100])
print(lst)
lst.extend([55,66,77])
print(lst)
