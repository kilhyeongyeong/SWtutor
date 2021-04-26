#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import threading

print('Hello ',sys.argv[0])

class Messenger(threading.Thread):
	def run(self):
		for i in range(10):
			print("threading..:",threading.currentThread().getName())

send = Messenger(name='Send message : Hello yangssem')
receive = Messenger()
receive.setName('Receive message : Hello kim')


send.start()
#send.join()
receive.start()


print("send.isAlive():",send.isAlive())
print("receive.isAlive():",receive.isAlive())

print(threading.enumerate())  #thread list
print(threading.activeCount())  #thread list




print("end main....")






