# -*- coding: utf-8 -*-

# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


import re
from pprint import pprint
from p30 import load_text, make_MorphemeDict, make_DictList


def find_Nouns(sentence):
	noun_list = []
	noun = []
	for word in sentence:
		if word["pos"] == "名詞":
			noun.append(word["surface"])
		else:
			if len(noun) >= 2:
				noun_list.append("".join(noun))
			noun = []
	return noun_list

if __name__ == "__main__":
	dictlist = make_DictList(load_text()[:1000])

	# surface of verb
	#from functools import reduce
	#print( [[word["surface"] for word in sentence if word["pos"]=="動詞"] for sentence in dictlist] )
	#print( reduce(lambda x,y: x+y, [[word["surface"] for word in sentence if word["pos"]=="動詞"] for sentence in dictlist] ))
	#print( [word["surface"] for sentence in dictlist for word in sentence if word["pos"]=="動詞"]  )

	# base of verb
	#print( [word["base"] for sentence in dictlist for word in sentence if word["pos"]=="動詞"]  )

	# surface of noun with サ変接続
	#print( [word["surface"] for sentence in dictlist for word in sentence if word["pos1"]=="サ変接続"]  )

	print(sum([find_Nouns(sentence) for sentence in dictlist], []))

	
