#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comment #
# code block Not, ; Not 
# switch case Not
# i++,i-- Not >> i+=1,i-=1

import sys
import re  #regexp:Regular Expressions

print('Hello ',sys.argv[0])

#[] >> word
#. >> \n less all word
#(*) >= 0
#(+) >= 1
#{m,n} >> ea count

pattern = re.compile("(\d{6})[-](\d{7})")
txt_data = '''
kim 123456-1234567 010-1111-1111 
lee 222222-2222222 010-2222-2222 
2021-12-25
'''

#\g<0> : [\g<0>]
print(pattern.sub("[\g<0>]",txt_data))
print(re.sub("(\d{6})[-](\d{7})","[\g<0>]",txt_data))

#\g<1>-*******
print(pattern.sub("\g<1>-*******",txt_data))
print(re.sub("(\d{6})[-](\d{7})","\g<1>-*******",txt_data))

#?P<key> : \g<key>
print(re.sub("(?P<key1>\d{6})[-](?P<key2>\d{7})","******-\g<key2>",txt_data))
print(re.sub("(?P<key1>\d{6})[-](?P<key2>\d{7})","\g<key1>-*******",txt_data))
print(re.sub("(?P<yyyy>\d{4})[-](?P<mm>\d{2})[-](?P<dd>\d{2})","\g<yyyy>.\g<mm>.\g<dd>",txt_data))

#r"\1-\2-\3"
print(re.sub("(\d{3})[-](\d{4})[-](\d{4})",r"[\1]-[\2]-[\3]",txt_data))


