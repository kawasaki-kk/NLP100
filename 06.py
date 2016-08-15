#from 05 import make_word_ngram, make_char_ngram
md = __import__("05")

n = 2
string_X = "paraparaparadise"
string_Y = "paragraph"

X = set(md.make_char_ngram(string_X, n))
#X = md.make_char_ngram(string_X, n)
Y = set(md.make_char_ngram(string_Y, n))

print("X",X)
print("Y",Y)
print(X|Y)
print(X&Y)
print(X-Y)

print("se" in X)
print("se" in Y)
