#!/usr/bin/python
# coding: UTF-8

with open("col1.txt") as f:
	col1 = f.read()

with open("col2.txt") as f:
	col2 = f.read()

data = ""
col1 = col1.split("\n")[:-1]
col2 = col2.split("\n")[:-1]
print(col1)
print(col2)

data = []
for (c1, c2) in zip(col1, col2):
	data.append("\t".join([c1,c2]))


print("dataaa",data)

with open("col12.txt", "w") as f:
	for i in data:
		f.write(i+"\n")

#import csv
#with open("col1.txt", "w") as f:
#	a = csv.writer(f)
#	a.writerow(col1)
#
#with open("col2.txt", "w") as f:
#	a = csv.writer(f)
#	a.writerow(col2)

