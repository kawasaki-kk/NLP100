# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# # make word n-gram by string
# def make_word_ngram(string, n):
# 	string = string.split()

# 	data = []
# 	for i in range(len(string)-n+1):
# 		data.append(string[i:i+n])

# 	return data


# # make character n-gram by string
# def make_char_ngram(string, n):
# 	data = []
# 	for i in range(len(string)-n+1):
# 		data.append(string[i:i+n])

# 	return data


# make n-gram by inputed list.
# method 1
def make_ngram(string, n):
	data = []
	for i in range(len(string)-n+1):
		data.append(string[i:i+n])

	return data

# method 2
def make_ngram2(string, n):
	return [string[i:i+n] for i in range(len(string)-n+1)]


# method 3
def make_ngram3(string, n):
	return list(map(lambda i:string[i:i+n] , range(len(string)-n+1)))

# mothod 4
make_ngram4 = lambda string, i:[string[i:i+n] for i in range(len(string)-n+1)]


if __name__ == '__main__':
	n = 2

	# if string is as "character", make character base
	string = "I am an NLPer"
	print(make_ngram(string, n))
	print(make_ngram2(string, n))
	print(make_ngram3(string, n))
	print(make_ngram4(string, n))

	# if string is as "words list".
	string = string.split()
	print(make_ngram(string, n))
	print(make_ngram2(string, n))
	print(make_ngram3(string, n))
	print(make_ngram4(string, n))
