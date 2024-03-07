#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

#list >> read, insert, update,delete OK
#tuple >> read-only

tp = ()
#tp = (11) #int
tp = (11,) #comma tuple
#tp = (11,22,33)
#tp = (0 for _ in range(10))
#tp = range(10)

print(tp)
print(type(tp))
print(type(range(10)))
print(type((0 for _ in range(10))))
print(len(tp))
print("==========================")
tp = tuple()
tp = tuple((11,22,33))
tp = tuple([11,22,33])
print(tp)


print("==========================")

tp = (11,22,33,44)
print(tp)
print(tp[1])
print(tp[1:3])
#tp[1:3] = []  #error : read-only
#del tp[2]   #error : read-only
#tp.append(55)  #error
#tp.remove(22)  #error

lst = list(tp)
print(lst)
print(type(lst))
lst.append(55)
tp = tuple(lst)
print(tp)
