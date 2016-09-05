# -*- coding: utf-8 -*-

# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．


import re
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import numpy as np
from pprint import pprint
from p30 import load_text, make_MorphemeDict, make_DictList

from p36 import count_ApearedWords

def plot_BarGraph(words_counter):
	# num of all apeared words
	num_words = sum(words_counter.values())
	# top 10 words most apeared
	top10 = words_counter.most_common(10)

	# x-axis
	left = np.array(range(10))
	# y-axis
	height = np.array([top10[i][1] / num_words for i in range(10)])
	plt.xlabel("Words")
	plt.ylabel("Appearance frequency")
	# ticks of x-axis
	tick = [top10[i][0] for i in range(10)]
	fp = FontProperties(fname=r'/root/NLP100/IPAexfont00301/ipaexm.ttf', size=14)
	plt.xticks(left, tick, fontproperties = fp)
	# plot
	plt.bar(left, height, align="center")
	# save as png
	plt.savefig("Appearance_Frequency_of_words.png")

if __name__ == "__main__":
	# make list of dictionaries of norpheme
	dictlist = make_DictList(load_text())
	
	words_counter = count_ApearedWords(dictlist)

	plot_BarGraph(words_counter)

	plt.show()
