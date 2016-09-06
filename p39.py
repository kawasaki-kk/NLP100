# -*- coding: utf-8 -*-

# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．


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
	plt.xlabel("Word appearance")
	plt.ylabel("Number of times of word appearance")
	# plot
	# plt.hist(freq, bins = 20, normed = True)
	plt.hist(freq, bins = 20, range = (0, 100))
	# save as png
	plt.savefig("Histgram_of_Appearance_Frequency.png")

def plot_DoubleLog(words_counter):
	# print(sorted(words_counter.values()))
	# print(Counter(list(words_counter.values())))
	counts_of_times_of_word_appearance = sorted(Counter(list(words_counter.values())).keys(), reverse = True)
	# print(counts_of_times_of_word_appearance)
	plt.plot(counts_of_times_of_word_appearance, range(len(counts_of_times_of_word_appearance)))
	plt.xlabel("Ranking")
	plt.ylabel("Appearance fraquency")
	plt.xscale("log")
	plt.yscale("log")
	plt.savefig("Zipf_lows.png")

if __name__ == "__main__":
	# make list of dictionaries of norpheme
	dictlist = make_DictList(load_text())
	
	words_counter = count_ApearedWords(dictlist)

#	plot_Histgram(words_counter)
	plot_DoubleLog(words_counter)	

	plt.show()
