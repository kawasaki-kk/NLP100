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
	# print(sorted(words_counter.values()))
	# print(Counter(list(words_counter.values())))
	# x-axis
	freq = list(sorted(words_counter.values()))
	# print(freq)
	plt.xlabel("Counts of words appearance")
	plt.ylabel("Frequency of counts")
	# plot
	plt.hist(freq, bins = 20, normed = True)
	# save as png
	plt.savefig("Histgram_of_Appearance_Frequency.png")


if __name__ == "__main__":
	# make list of dictionaries of norpheme
	dictlist = make_DictList(load_text())
	
	words_counter = count_ApearedWords(dictlist)

	plot_Histgram(words_counter)

	plt.show()
