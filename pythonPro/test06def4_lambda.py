#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

def fn1(x):
	return x + 10

print(fn1)   #<function fn1 at 0xf795e77c>
print(fn1(100))  #110

print(lambda x: x + 10) #<function <lambda> at 0xf78a02b4>
print((lambda x: x + 10)(33)) #43

print("=====================")

def fn2(x,y):
	return x * y

print(fn2)
print(fn2(10,20))

print(lambda x,y: x*y)
print((lambda x,y: x*y)(3,9))

print("=====================")
def test01(fn):
	print(fn(10,40)) #400

test01(fn2)
test01(lambda x,y: x*y)

print("=====================")
def test02():
	#return fn2
	return lambda x,y: x*y
	
print(test02()(5,9))	#45

print("=====================")
	
testFn = fn2
testFn = lambda x,y: x*y
print(testFn(25,25))  #625
