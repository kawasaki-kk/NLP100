#!/usr/bin/python
# coding: UTF-8

import re


with open("hightemp.txt") as f:
	data = f.read()

#print(len(data))
#print(data)
print("tab count:",data.count("\t"))
print("space count:",data.count(" "))


data = data.replace('\t', ' ')
#data = data.expandtabs(1)

#print(len(data))
print(data)
print("tab count:",data.count("\t"))
print("space count:",data.count(" "))

with open("hightemp_t2s.txt", "w") as f:
	f.write(data)

	

