# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

from string import ascii_lowercase

def cipher(string):
	string_list = list(string)
	for (i,c) in enumerate(string_list):
		if c in ascii_lowercase:
			string_list[i] = chr(219 - ord(c))
	
	string = "".join(string_list)
	return string

def uncipher(string):
	string_list = list(string)
	for (i,c) in enumerate(string_list):
		if chr(219 - ord(c)) in ascii_lowercase:
			string_list[i] = chr(219 - ord(c))
	
	string = "".join(string_list)
	return string

if __name__=='__main__':
	string = "aiueOkakikukeKOOO"

	print(cipher(string))
	print(uncipher(cipher(string)))
