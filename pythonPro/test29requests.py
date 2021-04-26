#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import requests

print('Hello ',sys.argv[0])

#http://192.168.133.1:8080/TestController/test2.txt
'''
{
  "name":"kim",
  "vo":{
        "id":"admin"
       },
  "arr":[11,22,33]
}
'''
###########################

response = requests.get("http://192.168.133.1:8080/TestController/test2.txt")
print("====response==========================")
print(response)
print("====response.status_code==========================")
print(response.status_code) #200
print("====response.headers==========================")
print(response.headers) #header info
print("====response.content==========================")
print(response.content) #page source code
###########################

response = requests.get("http://192.168.133.1:8080/TestController/yad_curl.jsp?name=kim11&tel=01011")
print("====response.content==========================")
print(response.content) #page source code
###########################
bytes_text = response.content
print(bytes_text.decode("utf-8"))
