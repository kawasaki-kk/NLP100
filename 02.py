# -*- coding: utf-8 -*-

string1 = "パトカー"

string2 = "タクシー"


st=""
for (st1, st2) in zip(string1, string2):
	st += st1 + st2

print(st)
