# -*- coding: utf-8 -*-

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

# open json file
#with open("jawiki-country.json", "rt", encoding='utf-8') as f:
with open("jawiki-country.json", "r") as f:
#with open("jawiki-country.json", "r", encoding='utf-8') as f:
	reader = f.readlines()

#for i, data in enumerate(reader):
#	print(data)

# show
outputs=[]
for i, data_json in enumerate(reader):
	data_dict = json.loads(data_json)
	# show and stack England data
	#if json.loads(data, encoding='utf-8')["title"]=="イギリス":
	if data_dict["title"]=="イギリス":
		print(data_dict["text"])
		# stack data
		outputs.append(data_dict)
# output data
with open('jawiki-country_England.json', 'w') as f:
	#map(f.write, output) # 書き込まれない。謎。   
	[json.dump(output, f, sort_keys=True, indent=4, ensure_ascii=False) for output in outputs]
	#[json.dumps(output, sort_keys=True, indent=4, ensure_ascii=False) for output in outputs]
# f.write(line) for line in output] 

