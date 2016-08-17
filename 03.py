# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string_split = string.split()

# method 1
len_list = []
for st in string_split:
	len_list.append(len(st))
print(len_list)

# method 2 with map func
print(list(map(len, string.split())))

# method 3 with list comprehension
print([len(t) for t in string.split()])