# -*- coding: utf-8 -*-

# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．


import re
import json
import types

# open json file
def load_text():
	with open("jawiki-country_England.json", "r", encoding='utf-8') as f:
		return json.load(f)["text"]

def get_FoundationInfo(text):
	pattern = r"基礎情報.+ = .+\n\}\}"
	info = re.findall(pattern, text, re.DOTALL)
	#print(info)
	return info[0]

def remove_Markup_Emphasis(data):
	# Remove markup-lang of emphasis "'''"
	return re.sub(r"''+", "", data)

def remove_Markup_InternalLink(data):
	# Remove markup-lang of internal link "[[ ]]".
	pattern = r"\[{2}([^|\]]+?\|)*(.+?)\]{2}"	
	return re.sub(pattern, r"\2", data)	

def make_FieldValueDict(info):
	entry = info.split("\n|")
	#print(info.split("\n|"))

	data_dict = {}
	for data in entry[1:]:
		#print("before", data)
		data = remove_Markup_Emphasis(data)
		data = remove_Markup_InternalLink(data)
		#print("after", data)
		data = data.split(" = ")
		data_dict[data[0]] = data[1]
	
	return data_dict

def print_dict(data_dict):
	print(data_dict)
	#print(data_dict["確立形態4"])


if __name__ == "__main__":
	text = load_text()
	foundation_info = get_FoundationInfo(text)
	print(foundation_info)
	data_dict = make_FieldValueDict(foundation_info)
	print_dict(data_dict)
