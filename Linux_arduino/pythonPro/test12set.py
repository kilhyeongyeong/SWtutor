#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

# set >> unique, index Not
#s={} # **dict**
s = {1,2,3,1,2,3}
print(s)
print(type(s))
print(len(s))

print("====list to set======================")

# list to set
s = set([1,2,3,1,2,3])
print(s)
print(type(s))
print(len(s))

print("====tuple to set====================")

# tuple to set
s = set((1,2,3,1,2,3))
print(s)
print(type(s))
print(len(s))

print("====add(), remove()====================")
s = {11,22,33,11,22,33}
s.add(11)
s.add(11)
s.add(44)
print(s)

s.remove(33)
print(s)

print("=======================")
for item in s:
	print(item)
	
print("=======================")
lst = [11,22,33]	
lst = lst + [22,33,44]	
print(lst)

print("=======================")
tp = (11,22,33)	
tp = tp + (22,33,44)	
print(tp)

print("=======================")
s = {11,22,33}
#s = s + {22,33,44}	# + error >> |
s = s | {22,33,44}	#union
print(s)

print("=======================")
s = {11,22,33}
s = s & {22,33,44}	#intersection
print(s)

print("=======================")
s = {11,22,33}
s = s - {22,33,44}	#difference
print(s)

print("=======================")

s1 = {11,22,33}
s2 = {22,33,44}
print("union(or):",s1.union(s2))
print("intersection(and):",s1.intersection(s2))
print("difference(minus):",s1.difference(s2))




