def make_word_ngram(string, n):
	string = string.split()

	data = []
	for i in range(len(string)-n+1):
		data.append(string[i:i+n])

	return data


def make_char_ngram(string, n):
	data = []
	for i in range(len(string)-n+1):
		data.append(string[i:i+n])

	return data


if __name__ == '__main__':
	string = "I am an NLPer"
	n = 2

	print(make_word_ngram(string, n))
	print(make_char_ngram(string, n))

