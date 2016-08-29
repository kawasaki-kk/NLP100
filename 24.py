# -*- coding: utf-8 -*-

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．


import re
import json
import types

# open json file
with open("jawiki-country_England.json", "r", encoding='utf-8') as f:
	data_dict = json.load(f)

data_text = data_dict["text"]
pattern = r"\[\[File:[^\]]+\]\]"
medias = re.findall(pattern, data_text)

media_info = {}
for media in medias:
	print(media)
	media_name = re.search(".+\.[^\|]+", media[7:]).group()

	print(media_name)
