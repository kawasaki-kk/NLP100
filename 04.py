string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

string_split = string.split()
#print(string_split)

top_char_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
sec_char_num = list(set(range(len(string_split))) - set(top_char_num))
#print(sec_char_num)

dic = {}
for i in top_char_num:
	dic.update({string_split[i][0]:i})
for i in sec_char_num:
	dic.update({string_split[i][0:2]:i})

print(dic)
