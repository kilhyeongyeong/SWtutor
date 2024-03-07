#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

def aaa():
	print("aaa()....")


def testArgs(*args):
	print("testArgs(*args)....")
	hap = 0
	for item in args:
		hap += item
	return hap
