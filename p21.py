# -*- coding: utf-8 -*-

# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
import json

# open json file
with open("jawiki-country_England.json", "r", encoding='utf-8') as f:
	data = json.load(f)

data_text = data["text"]
#pattern = "^\[\[Category:.+\]\]"
pattern = "\[\[Category:.+\]\]"
iterator = re.finditer(pattern, data_text)

for match in iterator:
	print(match.group())

# output data
# with open('jawiki-country_England.json', 'w') as f:
#	map(f.write, output) # 書き込まれない。謎。   
#	[f.write(line) for line in output] 

