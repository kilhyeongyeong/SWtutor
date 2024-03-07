#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

#{key:value}
#dic = {"name":"yangssem","tel":"010"}
dic = {'name':'yangssem','tel':'010','age':33}
print(dic)
print(type(dic))
print(len(dic))
print("=======================")

print(dic['name'],dic['tel'],dic['age'])
print(dic.get('name'),dic.get('tel'),dic.get('age'))
print("=======================")

dic = {}
print(dic)
print(type(dic))  #class 'dict
print("=======================")

dic = {0:'aaa',1:'bbb',2:'ccc',100:'zzz'}
print(dic)
print(type(dic))
print(dic[0],dic[1],dic[2],dic[100])
print("=======================")
dic['tel'] = "010"
dic['lst'] = [11,22,33]
dic['tp'] = (11,22,33)
dic['dt'] = {'email':'aaa@aaa.com'}
print(dic)
print('tel' in dic) #True
print('tel2' in dic) #False

print("dic.keys():",dic.keys())
print("dic.values():",dic.values())
print("dic.items():",dic.items())
for key in dic:
	print(key,dic[key],dic.get(key))

dic.clear() #dic = {}
print(dic)

###########################
stat = {'Strength': 20, 'Agility': 24, 'Stamina': 500, 'Wisdom': 33}
print(stat)

stat = dict({'Strength': 20, 'Agility': 24, 'Stamina': 500, 'Wisdom': 33})
print(stat)

stat = dict(Strength=20,Agility=24,Stamina=500,Widom=33)
print(stat)

stat = dict([('Strength', 20), ('Agility', 24), ('Stamina', 500), ('Wisdom', 33)])
print(stat)

stat = ['Strength','Agility','Stamina','Wisdom']
values = [20,24,500,33]

print(list(zip(stat,values)))
print(dict(list(zip(stat,values))))




