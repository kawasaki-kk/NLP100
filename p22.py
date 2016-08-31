# -*- coding: utf-8 -*-

# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
import json

# open json file
with open("jawiki-country_England.json", "r", encoding='utf-8') as f:
	data = json.load(f)

data_text = data["text"]
pattern = r"\[\[Category:.+\]\]"
iterator = re.finditer(pattern, data_text)

names = []
for match in iterator:
	name = match.group()
	print(name)
	name = re.sub(r'\[\[Category:', "", name)
	name = re.sub(r'\]\]', "", name)
	names.append(name)

print(names)
