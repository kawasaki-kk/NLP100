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


def plot_Histgram(words_counter):
	# num of all apeared words
	num_words = sum(words_counter.values())

	# x-axis
	# freq = np.array([words_counter.values()[i] / num_words for i in range(len(words_counter))])
	freq = list(sorted(words_counter.values()))
	# print(freq)
	plt.xlabel("Appearance frequency!!!")
	plt.ylabel("Frequency of appearance frequency")
	# plot
	# plt.hist(freq, bins = 50, normed = True)
	plt.hist(freq, bins = 1000, range=(0,100))
	# save as png
	plt.savefig("Histgram_of_Appearance_Frequency.png")


if __name__ == "__main__":
	# make list of dictionaries of norpheme
	dictlist = make_DictList(load_text())
	
	words_counter = count_ApearedWords(dictlist)

	plot_Histgram(words_counter)

	plt.show()
