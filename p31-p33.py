# -*- coding: utf-8 -*-

# 31. 動詞
# 動詞の表層形をすべて抽出せよ．
# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．
# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

import re
from pprint import pprint
from p30 import load_text, make_MorphemeDict, make_DictList


if __name__ == "__main__":
	dictlist = make_DictList(load_text()[:1000])

	# surface of verb
	#from functools import reduce
	#print( [[word["surface"] for word in sentence if word["pos"]=="動詞"] for sentence in dictlist] )
	#print( reduce(lambda x,y: x+y, [[word["surface"] for word in sentence if word["pos"]=="動詞"] for sentence in dictlist] ))
	print( [word["surface"] for sentence in dictlist for word in sentence if word["pos"]=="動詞"]  )

	# base of verb
	print( [word["base"] for sentence in dictlist for word in sentence if word["pos"]=="動詞"]  )

	# surface of noun with サ変接続
	print( [word["surface"] for sentence in dictlist for word in sentence if word["pos1"]=="サ変接続"]  )


