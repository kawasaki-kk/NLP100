# -*- coding: utf-8 -*-

# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．


import re
from collections import Counter
from pprint import pprint
from p30 import load_text, make_MorphemeDict, make_DictList

def count_ApearedWords(dictlist):
	# get list of base-form of appeared words.
	base_word_list = [word["base"] for sentence in dictlist for word in sentence ] 
	# print( [word["base"] for sentence in dictlist for word in sentence ]  )
	# print(Counter(base_word_list))

	return Counter(base_word_list)

if __name__ == "__main__":
	# make list of dictionaries of norpheme
	dictlist = make_DictList(load_text()[:1000])

	print(count_ApearedWords(dictlist))

	
