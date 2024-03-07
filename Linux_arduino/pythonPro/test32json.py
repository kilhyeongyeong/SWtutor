#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import json
import requests
print('Hello ',sys.argv[0])
'''
f = open("test32.json","r")
while True:
	data = f.readline()
	if not data:
		break
	print(data,end="")
'''
f_data = open("test32.json","r").read()
print(f_data)
print(type(f_data))
print()

#import json
json_data = json.loads(f_data)
print(json_data)
print(type(json_data))

print(json_data["name"])
print(json_data["vo"]["id"])
print(json_data["arr"][0])

print("====requests==========================")
#mission~~~!! test29requests.py + json parse
#import requests
response = requests.get("http://192.168.133.1:8080/TestController/test2.txt")
res_text = response.content
print("====bytes text==========================")
print(res_text) #bytes text
print("====decode('utf-8')==================")
res_text = res_text.decode('utf-8')
print(res_text) 
print(type(res_text)) 

print("====json.loads to dict==============")
json_data = json.loads(res_text)
print(json_data)
print(type(json_data)) #dict

print(json_data["name"])
print(json_data["vo"]["id"])
print(json_data["arr"][0])
