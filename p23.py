# -*- coding: utf-8 -*-

# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．


import re
import json
import types

# open json file
with open("jawiki-country_England.json", "r", encoding='utf-8') as f:
	data_dict = json.load(f)

data_text = data_dict["text"]
pattern = r"\n[=]+[^=]+[=]+"
sections = re.findall(pattern, data_text)

section_info = {}
for section in sections:
	section = section[1:]
	print(section)
	section_level = len(re.match("=+", section).group())
	section_name = re.search("[^=]+", section).group()
	section_info[section_name] = section_level
	print("{}:{}".format(section_name, section_level))

print(section_info)
