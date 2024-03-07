#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
#import tkinter   #python GUI
from tkinter import *   #python GUI

print('Hello ',sys.argv[0])

class ListPage:
	def __init__(self):
		top = Tk()
		#top.geometry("300x300")
		#top.geometry("150x100+550+100")
		top.geometry("150x100+0+0")
		print(top)

		lstBox = Listbox(top, selectbackground="orange")

		def onselected(event):
			print("onselected....",event.widget.curselection()[0])
			index = event.widget.curselection()[0]
			print("onselected....",event.widget.get(index))
			
			top.destroy() #window close

		lstBox.bind("<<ListboxSelect>>",onselected)

		lst = ["seong-ho Yang","python Lee","android Kim","linux Choi"]
		for item in lst:
			lstBox.insert(0,item)

		lstBox.pack()  #grid,place
		mainloop()
#ListPage()

class InsertPage:
	def __init__(self):
		top = Tk()
		top.geometry("250x100+0+0")
		
		fnameLabel = Label(top,text="fname:")
		lnameLabel = Label(top,text="lname:")
		fnameLabel.grid()
		lnameLabel.grid()
		
		fnameEntry = Entry(top)
		lnameEntry = Entry(top)
		
		fnameEntry.insert(0,"Seong-ho")
		lnameEntry.insert(0,"Yang")
		
		fnameEntry.grid(row=0,column=1)
		lnameEntry.grid(row=1,column=1)
		
		def onclick():
			print("onclick",fnameEntry.get(),lnameEntry.get())
			top.destroy() #window close
			ListPage()
		
		okButton = Button(top,text="OK",command=onclick)
		okButton.grid(row=2,column=1)
		
		mainloop()
		
InsertPage()	
		
##################
#tkinter process kill
#pi@raspberrypi:~/pythonPro $ ps axu | grep tk
#pi  21987  0.0  0.8  35404 17412 pts/0    Tl   03:33   0:00 python3 test31tkinter.py
#pi  21989  0.0  0.7  35132 15596 pts/0    Tl   03:34   0:01 python3 test31tkinter.py
#pi@raspberrypi:~/pythonPro $ kill -9 21987
#pi@raspberrypi:~/pythonPro $ kill -9 21989
