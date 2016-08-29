# -*- coding: utf-8 -*-

# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．


import re
import json
import types

# open json file
with open("jawiki-country_England.json", "r", encoding='utf-8') as f:
	data_dict = json.load(f)

data_text = data_dict["text"]
pattern = r"基礎情報.+ = .+\n\}\}"
info = re.findall(pattern, data_text, re.DOTALL)
#print(info)

info = info[0]
entry = info.split("\n|")
#print(info.split("\n|"))

data_dict = {}
for data in entry[1:]:
	print(data)
	data = data.split(" = ")
	data_dict[data[0]] = data[1]

print(data_dict)

#pattern_entity = "^\|.+ = .+"
#entities = re.findall(pattern_entity, *info, re.MULTILINE)
#pattern_entity = r"\n\|[^=]+ = [^(\n\|)]+"
#entities = re.findall(pattern_entity, *info, re.DOTALL)
#print(entities)

#pattern_value = r" = [^\\n]"
#values = re.findall(pattern_value, info)
#print([name[1:] for name in fields])
#print(values)
