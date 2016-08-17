# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random


def shuffle_string(string):
	string_split = string.split()
	print(string_split)

	result = []
	for word in string_split:
		print("----------------------------------------------")
		if len(word)<=4:
			print("word:", word)
			print("pass")
			result.append(word)
		else:
			print("word:", word)
			word_list = list(word)
			word_list2 = word_list[1:-1]
			#print("word_list:", word_list)
			#print("word_list2:", word_list2)
			random.shuffle(word_list2)
			#print("shuffled:", word_list2)
			word_list[1:-1] = word_list2
			word = "".join(word_list)
			print("word after:",word)
			result.append(word)
		print(result)

	return " ".join(result)

if __name__=='__main__':
	string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	print(shuffle_string(string))


