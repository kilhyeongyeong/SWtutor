#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

#test08Test.py
#insert(name,age),update(num,name,age),delete(num) : return int type
def insert(name,age):
	print("insert(name,age) : ",name,age)
	return 1

def update(num,name,age):
	print("update(num,name,age) : ",num,name,age)
	return 1
	
def delete(num):
	print("delete(num) : ",num)
	return 1

#selectAll() : [ "", "", ""]
def selectAll():
	print("selectAll()...")
	return ["1:'kim1':11","2:'kim2':22","3:'kim3':33"]

#selectOne(num) : str
def selectOne(num):
	print("selectOne()...",num)
	return "1:'kim1':11"
 
#searchList(searchKey,searchWord): [ "", "", ""]
def searchList(searchKey,searchWord):
	print("searchList()...",searchKey,searchWord)
	return ["2:'kim2':22","3:'kim3':33"]
