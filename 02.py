# -*- coding: utf-8 -*-

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

string1 = "パトカー"

string2 = "タクシー"


st=""
for (st1, st2) in zip(string1, string2):
	st += st1 + st2

print(st)
