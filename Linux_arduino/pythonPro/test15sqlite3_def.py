#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

#sudo apt install libsqlite3-dev
#sudo apt install sqlite3
import sys
import sqlite3

print('Hello ',sys.argv[0])

con = sqlite3.connect("test15.db")
cs = con.cursor()

def createTable():
	sql = '''
	create table if not exists test(
	num integer primary key autoincrement,
	name text,
	age integer)
	'''
	cs.execute(sql)

createTable()

def insert(name,age):
	sql = '''
	insert into test(name,age) values(?,?)
	'''
	values = (name,age)
	cs.execute(sql,values)
	con.commit()
	print("=====insert successed=====");

def update(name,age,num):
	sql = '''
	update test set name=?, age=? where num=?
	'''
	values = (name,age,num)
	cs.execute(sql,values)
	con.commit()
	print("=====update successed=====");

def delete(num):
	sql = '''
	delete from test where num=?
	'''
	values = (num,)  #one comma
	cs.execute(sql,values)
	con.commit()
	print("=====delete successed=====");

def selectOne(num):
	sql = '''
	select * from test where num=?
	'''
	values = (num,)  #one comma
	cs.execute(sql,values)
	print(cs.fetchone())
	print("=====selectOne successed=====");

def selectAll():
	sql = '''
	select * from test
	'''
	for row in cs.execute(sql):
		print(row)
	print("=====selectAll successed=====");

def searchList(searchKey,searchWord):
	searchWord = "%"+searchWord+"%"
	values = (searchWord,)
	if searchKey == "name":
		sql = '''
		select * from test where name like ?
		'''
	elif searchKey == "age":
		sql = '''
		select * from test where age like ?
	'''
	for row in cs.execute(sql,values):
		print(row)

	print("=====searchList successed=====");

print("=====function define successed=====");
while True:
	print("=====input menu number=========================");
	print('''[1.insert, 2.update, 3.delete 
	4.selectOne, 5.selectAll, 6.searchList, other key(exit)]''');
	print("==============================================");
	menu = input()
	if menu == "1":
		print("1.insert Page================")
		print("insert name:")
		name = input()
		print("insert age:")
		age = input()
		insert(name,age)
	elif menu == "2":
		print("2.update Page================")
		print("update num:")
		num = input()
		print("update name:")
		name = input()
		print("update age:")
		age = input()
		update(name,age,num)
	elif menu == "3":
		print("3.delete Page================")
		print("delete num:")
		num = input()
		delete(num)
	elif menu == "4":
		print("4.selectOne Page================")
		print("selectOne num:")
		num = input()
		selectOne(num)
	elif menu == "5":
		print("5.selectAll Page================")
		selectAll()
	elif menu == "6":
		print("6.searchList Page================")
		print("searchKey:")
		searchKey = input()
		print("searchWord:")
		searchWord = input()
		searchList(searchKey,searchWord)
	else:
		break
con.close()
