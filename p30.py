# -*- coding: utf-8 -*-

#第4章: 形態素解析
#夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
#なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．


import re
from pprint import pprint


def load_text(filename = "neko.txt.mecab"):
	with open(filename) as f:
		text = f.readlines()
	return text

def make_MorphemeDict(line_split):
	dic = {}
	dic["surface"] = line_split[0]
	dic["base"] = line_split[7]
	dic["pos"] = line_split[1]
	dic["pos1"] = line_split[2]
	return dic

def make_DictList(text):
	sentence_all = []
	sentence = []
	for line in text:
		if line != "EOS\n":
			line_split = re.split(r"[\t,\n]", line)[:-1]
			sentence.append(make_MorphemeDict(line_split))
		elif line == "EOS\n":
			sentence_all.append(sentence)
			sentence = []
	return sentence_all


if __name__ == "__main__":
	pprint(make_DictList(load_text()[:18]))

