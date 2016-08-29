# -*- coding: utf-8 -*-

# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．


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
	data = re.sub(r"''+", "", data)
	data = data.split(" = ")
	data_dict[data[0]] = data[1]

print(data_dict)
print(data_dict["確立形態4"])

#pattern_entity = "^\|.+ = .+"
#entities = re.findall(pattern_entity, *info, re.MULTILINE)
#pattern_entity = r"\n\|[^=]+ = [^(\n\|)]+"
#entities = re.findall(pattern_entity, *info, re.DOTALL)
#print(entities)

#pattern_value = r" = [^\\n]"
#values = re.findall(pattern_value, info)
#print([name[1:] for name in fields])
#print(values)
