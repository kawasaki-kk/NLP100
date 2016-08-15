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


