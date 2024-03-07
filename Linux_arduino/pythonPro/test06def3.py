#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys

print('Hello ',sys.argv[0])

# 1 class function : argument value,return value, init value

print("==1.argument value============")
def printName():
	print("printName()...kim")

def test(fn):
	fn()

test(printName)
###############################

print("==2.return value============")
def sleep():
	def sleep_01():
		print("sleep : sleep_01()..")
	return sleep_01

fn = sleep()
print(fn)
fn()

###############################

print("==3.init value============")

def run():
	print("run()...")

rFn = run
rFn




