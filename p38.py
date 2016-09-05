# -*- coding: utf-8 -*-

# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．


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

def plot_Histgram(words_counter):
	# num of all apeared words
	num_words = sum(words_counter.values())

	# x-axis
	# freq = np.array([words_counter.values()[i] / num_words for i in range(len(words_counter))])
	freq = list(sorted(words_counter.values()))
	# print(freq)
	plt.xlabel("Appearance frequency")
	plt.ylabel("Frequency of appearance frequency")
	# plot
	# plt.hist(freq, bins = 50, normed = True)
	plt.hist(freq, normed = True)
	# save as png
	plt.savefig("Histgram_of_Appearance_Frequency.png")


if __name__ == "__main__":
	# make list of dictionaries of norpheme
	dictlist = make_DictList(load_text())
	
	words_counter = count_ApearedWords(dictlist)

	plot_Histgram(words_counter)

	plt.show()
