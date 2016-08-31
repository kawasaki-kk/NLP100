# -*- coding: utf-8 -*-

# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．


import re
# from compiler.ast import flatten
from pprint import pprint
from p30 import load_text, make_MorphemeDict, make_DictList


def find_NounPhrase(sentence):
	list_nounphrase = []
	for i in range(len(sentence)-2):
		if sentence[i]["pos"] == "名詞" and sentence[i+1]["pos"] == "助詞" and sentence[i+1]["surface"] == "の" and sentence[i+2]["pos"] == "名詞" :
			list_nounphrase.append(sentence[i]["surface"] + sentence[i+1]["surface"] + sentence[i+2]["surface"]) 
	return list_nounphrase	

if __name__ == "__main__":
	dictlist = make_DictList(load_text()[:1000])

	print(sum([find_NounPhrase(sentence) for sentence in dictlist], []))

	
