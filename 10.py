#!/usr/bin/python
# coding: UTF-8

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

with open("hightemp.txt") as f:
	data = f.readlines()

print(len(data))

