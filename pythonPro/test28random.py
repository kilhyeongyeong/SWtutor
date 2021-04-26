#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import random

print('Hello ',sys.argv[0])

for i in range(6):
	print(random.random())  #0.0 ~ 1.0
	print(random.random()*10)  #1.0 ~ 10.0
	print(int(random.random()*10))  #1 ~ 10
	print(random.randrange(1,6))  # 1 ~ 6
	print("--------------------")

lst = [i for i in range(10)]
lst = [chr(i) for i in range(65,65+26)]
print("before shuffle:",lst)
random.shuffle(lst)
print("after shuffle:",lst)
print("--------------------")
print(random.choice(lst),random.choice(lst),random.choice(lst))


