#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sqlite3

con = sqlite3.connect("minipro.db")
cs = con.cursor()

def insert(sn,username, phone):
	sql = '''
	insert into bluetooth(sn,username,phone) values(?,?,?)
	'''
	values = (sn, username, phone)
	cs.execute(sql,values)
	con.commit()
    
def delete(phone, sn):
	sql = '''
	delete from bluetooth where phone=? and sn=?
	'''
	values = (phone, sn)
	cs.execute(sql,values)
	con.commit()
    
def createTable():
	sql = '''
	create table if not exists bluetooth(
	phone text,
	sn text,
	username text)
	'''
	cs.execute(sql)
    
def selectAll():
    count = 0
    sql="select * from bluetooth"
    for row in cs.execute(sql):
        count += 1
        print("\t\t{}. {}".format(count, row[2]))

def selectAllnotp():
    count = 0
    lst = []
    sql="select * from bluetooth"
    for row in cs.execute(sql):
        count += 1
        lst.append(row)
    return lst, count

def main(args):
    #createTable()
    res = 0
    check = 0
    response = requests.get("http://192.168.46.151:8090/miniproject2/index.do")
    res_text = response.content
    json_data = json.loads(res_text.decode('utf-8'))
    print("==============={}=================".format(json_data["car"]["model"]))
    
    while True:
        if res == 0:
            print("\ta.insert \tb.delete")
            selectAll()
            print(">>",end=" ")
            res = input()
        elif res == "a":
            lst, count = selectAllnotp()
            for item in lst:
                if item[1] == json_data["car"]["sn"] and item[0] == json_data["person"]["phone"]:
                    print("already exist.")
                    check = 1
                    res = 0
                    break
            if check == 0:
                if count == 10:
                    print("full, Please delete and insert.")
                    res = 0
                else:
                    insert(json_data["car"]["sn"], json_data["person"]["username"], json_data["person"]["phone"])
                    res = 0
        elif res == "b":
	    print("\t\tdelete")
            selectAll()
            print(">>",end=" ")
            res = input()
            lst,_ = selectAllnotp()
            #delete(lst[res-1][0],lst[res-1][1])
            res = 0
            
      
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



