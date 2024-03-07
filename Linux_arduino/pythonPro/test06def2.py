#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1
print('Hello python')
print("Hello def2")

def sumXY(x,y):
	print("sum(x,y)....",x,y)
	print("sum(x,y)....{},{}".format(x,y))
sumXY(11,22)
print(sumXY(11,22)) #None

####################
def sumXY(x,y):
	print("sum(x,y)....",x,y)
	print("sum(x,y)....{},{}".format(x,y))
	return x+y
print(sumXY(11,22)) #33

####################
def testSus(a1,a2,a3,a4,a5):
	print("testSus(a1,a2,a3,a4,a5)....",a1,a2,a3,a4,a5)

testSus(11,12,13,14,15)


####################
def testSus2(*args):
	print("testSus2(*args)....",type(args))
	for item in args:
		print(item,end=" ")
	print()

testSus2(11,12,13,13,14,15)


####################
def testDatas(*args):
	print("testDatas(*args)....",type(args))
	for item in args:
		print(item,end=" ")
	print()

testDatas(11,12,13,"kim","lee")

####################
def testTuple(tp):
	print("testTuple(tp)....",type(tp))
	for item in tp:
		print(item,end=" ")
	print()

testTuple((11,12,13,"kim","lee")) #(,,,) tuple


####################
def testList(lst):
	print("testList(lst)....",type(lst))
	for item in lst:
		print(item,end=" ")
	print()

testList([11,12,13,"kim","lee"]) #[,,,] list
