#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1


#test09member_main.py
#insert(id,pw,name,tel),update(num,id,pw,name,tel),delete(num) : return int type
def insert(id,pw,name,tel):
	print("insert(id,pw,name,tel):",id,pw,name,tel)
	return 1
def update(num,id,pw,name,tel):
	print("update(num,id,pw,name,tel):",num,id,pw,name,tel)
	return 1
def delete(num):
	print("delete(num):",num)
	return 1


#selectAll() : [ "", "", ""]
def selectAll():
	print("selectAll()")
	return [ "1,'aaa','aa1234','kima','010'", "2,'bbb','bb1234','kimb','020'", "3,'ccc','cc1234','kimc','030'"]

#selectOne(num) : str 
def selectOne(num):
	print("selectOne(num):",num)
	return "1,'aaa','aa1234','kima','010'"

#searchList(searchKey,searchWord): [ "", "", ""]
def searchList(searchKey,searchWord):
	print("selectAll():",searchKey,searchWord)
	return [ "2,'bbb','bb1234','kimb','020'", "3,'ccc','cc1234','kimc','030'"]

