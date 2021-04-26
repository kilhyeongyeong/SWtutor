#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

print(abs(-11))
print(abs(11))

#array : all
print("all([]):",all([])) #True
print("all([1,2,3]):",all([1,2,3])) #True
print("all([1,2,3,0]):",all([1,2,3,0])) #0 False
print("all([1,2,'kim']):",all([1,2,"kim"])) #True
print("all([1,2,'']):",all([1,2,""])) #"" False
print()

#array : any
print("any([]):",any([])) #False
print("any([1]):",any([1])) #True
print("any([1,0,0,0,0,0]):",any([1,0,0,0,0,0])) #True
print("any([1,2,'']):",any([1,2,''])) #True

#class info >> dir()
print(dir([]))
print()

print(dir((1,)))
print()

print(dir({}))
print()

print(dir("kim"))
print()

#cast
print(chr(97),chr(98),chr(99))
print()

print(int("97") + int("97"))
print()

print(float("97.99") + float("97.99"))
print()

#1/2 >>(0,1), 7/3 >>(2,1) tuple
print(divmod(1,2), divmod(7,3))
print()

#eval
print('kim'+'lee',eval("'kim'+'lee'"))
print('11 + 22 = ',eval('11 + 22'))
print(eval('11 + 22'))
print()

#id
print(id("a"))
print(id("b"))
print(id("abc"))
print()

#hex 16
print(id("abc"),hex(id("abc")))
print()

#vars(), isinstance()
class Person:
	pname = "yangssem"
	def __init__(self):
		self.id = 'admin'
	
p = Person()
print(vars(p))
print(p.pname)
print(p.id)

print(isinstance(p,Person))
############################################

print()
# item >=0 >>> list
lst = [0,1,-1,2,-2]
temp = list()

def fn(item):
	return item >=0

#lambda item: item>=0
	
for item in lst:
	if fn(item) : 
		temp.append(item)	
	
print(temp)


#filter(fn,list)
print(filter(fn,lst))
print(list(filter(fn,lst)))
print("====filter lambda===")
print(list(filter(lambda item: item>=0,lst)))
print(len(list(filter(lambda item: item>=0,[0,1,-1,2,-2]))))

print()
############################
# item * item >> item**2  >> fn2 create
lst = [1,2,3,4,-5]

def fn2(item):
	return item**2
temp = list()
for item in lst:
	temp.append(fn2(item))
print(temp)

#map(fn,list)
print(map(fn2,lst))
print(list(map(fn2,lst)))
print("====map lambda===")
print(list(map(lambda item:item**2,lst)))
print("====filter lambda item%2==0   ===")
print(list(filter(lambda item:item%2==0,list(map(lambda item:item**2,lst)))))

print()
############################
# [(lst1[0], lst2[0]),(lst1[1], lst2[1]),(lst1[2], lst2[2])]
# [(1, 4),(2, 5),(3, 6)]
lst1 = [1,2,3]
lst2 = [4,5,6]

temp = list()
#temp.append((lst1[0], lst2[0]))
#temp.append((lst1[1], lst2[1]))
#temp.append((lst1[2], lst2[2]))
for i in range(3):
	temp.append((lst1[i], lst2[i]))
print(temp)


#zip(list,list,....)   >>> list() >>> friend dict()
print(zip(lst1,lst2))
print(list(zip(lst1,lst2)))

stat = ['Strength','Agility','Stamina','Wisdom']
values = [20,24,500,33]

print(list(zip(stat,values)))
print(dict(list(zip(stat,values))))
