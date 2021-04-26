#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import test09member as member

print('Hello ',sys.argv[0])

result_insert = member.insert("admin","hi1234","lee","02")
print("result_insert:",result_insert)

result_update = member.update(2,"adminup","hi1234up","leeup","02up")
print("result_update:",result_update)

result_delete = member.delete(3)
print("result_delete:",result_delete)


result_selectOne = member.selectOne(1)
print("result_selectOne:",result_selectOne)

result_selectAll = member.selectAll()
print("result_selectAll:",result_selectAll)
for item in result_selectAll:
	print(item)
	
result_searchList = member.searchList("name","ki")
print("result_searchList:",result_searchList)
for item in result_searchList:
	print(item)


