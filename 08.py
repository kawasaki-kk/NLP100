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
