# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

string_split = string.split()
#print(string_split)

top_char_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
sec_char_num = list(set(range(len(string_split))) - set(top_char_num))
#print(sec_char_num)

# method 1 
dic = {}
for i in top_char_num:
	dic.update({string_split[i][0]:i})
for i in sec_char_num:
	dic.update({string_split[i][0:2]:i})

print(dic)

# method 2
# dic.update with 1 element is not usual.
dic2 = {}
for i in top_char_num:
	dic2[string_split[i][0]] = i
for i in sec_char_num:
	dic2[string_split[i][0:2]] = i

print(dic2)