string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string_split = string.split()

len_list = []
for st in string_split:
	len_list.append(len(st))
print(len_list)

