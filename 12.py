#!/usr/bin/python
# coding: UTF-8

import re


with open("hightemp.txt") as f:
	data = f.readlines()

col1 = []
for i in data:
	col1.append(i.split()[0])
print(col1)

col2 = []
for i in data:
	col2.append(i.split()[1])
print(col2)

import csv
with open("col1.txt", "w") as f:
	for i in col1:
		f.write(i+"\n")

with open("col2.txt", "w") as f:
	for i in col2:
		f.write(i+"\n")

