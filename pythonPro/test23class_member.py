#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

class MemberVO:
	def __init__(self):
		self.__num = 1
		self.__id = "admin"
		self.__pw = "hi1212"
		self.__name = "kim"
		self.__tel = "02"
	@property
	def num(self):
		return self.__num
	@num.setter
	def num(self,user_num):
		self.__num = user_num
		
	@property
	def id(self):
		return self.__id
	@id.setter
	def id(self,user_id):
		self.__id = user_id
	
	@property
	def pw(self):
		return self.__pw
	@pw.setter
	def pw(self,user_pw):
		self.__pw = user_pw
	
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,user_name):
		self.__name = user_name
		
	@property
	def tel(self):
		return self.__tel
	@tel.setter
	def tel(self,user_tel):
		self.__tel = user_tel
	
class MemberDAO:
	@staticmethod
	def insert(vo):
		print(vars(vo))
		return 1;
		
	@staticmethod
	def update(vo):
		print(vars(vo))
		return 1;
		
	@staticmethod
	def delete(vo):
		print(vars(vo))
		return 1;
		
	@staticmethod
	def selectOne(vo):
		print(vars(vo))
		vo = MemberVO()
		vo.num = 44
		vo.id = "tester 44"
		vo.pw = "hi3434 44"
		vo.name = "lee 44"
		vo.tel = "031 44"
		return vo;
		
	@staticmethod
	def selectAll():
		lst = []
		for i in range(5):
			vo = MemberVO()
			vo.num = i
			vo.id = "tester "+str(i)
			vo.pw = "hi3434 "+str(i)
			vo.name = "lee "+str(i)
			vo.tel = "031 "+str(i)
			lst.append(vo)
		return lst;
		
	@staticmethod
	def searchList(searchKey,searchWord):
		print("searchKey:",searchKey)
		print("searchWord:",searchWord)
		lst = []
		for i in range(10,15):
			vo = MemberVO()
			vo.num = i
			vo.id = "search id"+str(i)
			vo.pw = "search pw"+str(i)
			vo.name = "search name"+str(i)
			vo.tel = "search tel"+str(i)
			lst.append(vo)
		return lst;

dao = MemberDAO()
vo = MemberVO()
vo.id = "tester"
vo.pw = "hi3434"
vo.name = "lee"
vo.tel = "031"
result = dao.insert(vo)
print("insert result:",result)
print("=========================")

vo = MemberVO()
vo.num = 99
vo.id = "tester up"
vo.pw = "hi3434 up"
vo.name = "lee up"
vo.tel = "031 up"
result = dao.update(vo)
print("update result:",result)
print("=========================")
vo = MemberVO()
vo.num = 33
result = dao.delete(vo)
print("delete result:",result)
print("=========================")
vo = MemberVO()
vo.num = 44
vo2 = dao.selectOne(vo)
print("selectOne vo2:",vars(vo2))
print("=========================")

lst = dao.selectAll()
print("selectAll lst:",lst)
for vo in lst:
	print(vars(vo))
print("=========================")

lst = dao.searchList("id","se")
print("searchList lst:",lst)
for vo in lst:
	print(vars(vo))
