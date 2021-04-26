#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

#sudo apt install libsqlite3-dev
#sudo apt install sqlite3
import sys
import sqlite3

print('Hello ',sys.argv[0])

con = sqlite3.connect("test15.db")
cs = con.cursor()
sql = '''
create table if not exists test(
num integer primary key autoincrement,
name text,
age integer)
'''
cs.execute(sql)
#pi@raspberrypi:~/pythonPro $ python3 test15sqlite3.py 
#Hello  test15sqlite3.py
#pi@raspberrypi:~/pythonPro $ sqlite3 test15.db ".tables"
#test

#############1.insert
sql = '''
insert into test(name,age) values(?,?)
'''
#values = ("kim",33)
#cs.execute(sql,values)
#con.commit()
#pi@raspberrypi:~/pythonPro $ sqlite3 test15.db "select * from test"
#1|kim|33
#2|kim|33

#############1-1.insert many
sql = '''
insert into test(name,age) values(?,?)
'''
#values_list = [("han1",221),("han2",222),("han3",223),("han4",224)]
#cs.executemany(sql,values_list)
#con.commit()


#############2.update
sql = '''
update test set name=?, age=? where num=?
'''
#values = ("lee",44,2)
#cs.execute(sql,values)
#con.commit()

#############3.delete
sql = '''
delete from test where num=?
'''
#values = (5,)  #one comma
#cs.execute(sql,values)
#con.commit()


#############4.selectOne >> cs.fetchone()
sql = '''
select * from test where num=?
'''
values = (9,)  #one comma
cs.execute(sql,values)
print(cs.fetchone())
print("============================")


#############5.selectAll >> for ~in~
sql = '''
select * from test
'''

for row in cs.execute(sql):
	print(row)

print("=======6.searchList=====================")
#############6.searchList >> for ~in~
#searchKey = "name"
#searchWord = "ki"
searchKey = "age"
searchWord = "2"

searchWord = "%"+searchWord+"%"
values = (searchWord,)
if searchKey == "name":
	sql = '''
	select * from test where name like ?
	'''
elif searchKey == "age":
	sql = '''
	select * from test where age like ?
'''
for row in cs.execute(sql,values):
	print(row)

print("============================")



con.close()
