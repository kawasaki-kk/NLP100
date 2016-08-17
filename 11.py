#!/usr/bin/python
# coding: UTF-8

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

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

	

