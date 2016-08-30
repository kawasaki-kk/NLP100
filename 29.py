# -*- coding: utf-8 -*-

# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）


import re
import json
import types
import requests

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

def remove_Markup_Tag(data):
	# Remove markup-lang of "< any >"
	pattern = r"<.+?>"
	return re.sub(pattern, "", data)	

def remove_Markup_OuterLink(data):
	# Remove markup-lang of "[ url ]"
	pattern = r"\[.+?\]"
	return re.sub(pattern, "", data)	

def remove_Markup_MultiLang(data):
	# Remove markup-lang of "{{lang|any|England-name}}"
	pattern = r"\{{2}lang\|.+?\|(.+?)\}{2}"
	return re.sub(pattern, r"\1", data)	

def make_FieldValueDict(info):
	entry = info.split("\n|")

	data_dict = {}
	for data in entry[1:]:
		data = remove_Markup_Emphasis(data)
		data = remove_Markup_InternalLink(data)
		data = remove_Markup_Tag(data)
		data = remove_Markup_OuterLink(data)
		data = remove_Markup_MultiLang(data)
		data = data.split(" = ")
		data_dict[data[0]] = data[1]
	
	return data_dict


class Mediawiki(object):

	def __init__(self):
		# basic URL
		self._url = "http://ja.wikipedia.org/w/api.php"

	# get response
	def get_response(self, parameters):
		# response = requests.get(self._url, params).json()
		response = requests.get(self._url, params = parameters).json()
		return response


if __name__ == "__main__":
	# load text of England from "jawiki-country_England.json"
	text = load_text()
	# get text of foundation infomation
	foundation_info = get_FoundationInfo(text)
	# make a Field-Value dictionary through foundation_info
	data_dict = make_FieldValueDict(foundation_info)

	# parameters for request.
	parameters = {
			"action": "query", 
			"format": "json", 
			"prop": "imageinfo", 
			"iiprop": "url",
			"titles": "File:{}".format(data_dict["国旗画像"]), 
		}

	# make instance
	mediawiki = Mediawiki()

	# get response
	response = mediawiki.get_response(parameters)
	
	# show 
	print(response["query"]["pages"]["-1"]["imageinfo"][0]["url"])
	# import pprint
	# pprint.pprint(response)
