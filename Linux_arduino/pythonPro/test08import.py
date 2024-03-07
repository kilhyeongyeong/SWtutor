#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import test08AAA
import test08AAA as aaa
import test08Test as test

print('Hello ',sys.argv[0])

test08AAA.aaa()
aaa.aaa()

print("sum:",aaa.testArgs(11,22,33,22))

#test08Test.py
#insert(name,age),update(num,name,age),delete(num) : return int type
#selectAll() : [ "", "", ""]
#selectOne(num) : str 
#searchList(searchKey,searchWord): [ "", "", ""]
print("insert result:",test.insert("lee",33))
print("update result:",test.update(5,"lee5",55))
print("delete result:",test.delete(7))

print("selectOne result:",test.selectOne(1))
print("selectAll result:",test.selectAll())
for item in test.selectAll():
	print(item)

print("searchList result:",test.searchList("name","ki"))
for item in test.searchList("name","ki"):
	print(item)
