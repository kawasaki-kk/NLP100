# coding: utf-8

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

# 1行に1記事の情報がJSON形式で格納される
# 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
# ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import types
import pprint
import json

#with open("jawiki-country.json", "rt", encoding='utf-8') as f:
#with open("jawiki-country.json", "r") as f:
with open("jawiki-country.json", "r", encoding='utf-8') as f:
	reader = f.readlines()

#for i, data in enumerate(reader):
#	print(data)

for i, data in enumerate(reader):
#for i, data in enumerate(reader):
	if json.loads(data)["title"]=="イギリス":
		pprint.pprint(json.dumps(data, ensure_ascii=False))
		#print(json.dumps(data))
#if data["title"]=="イギリス":
	#	print(data)
	#	print(i)
