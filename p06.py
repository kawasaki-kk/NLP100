# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

#from 05 import make_ngram
module05 = __import__("05")

n = 2
string_X = "paraparaparadise"
string_Y = "paragraph"

X = set(module05.make_ngram(string_X, n))
Y = set(module05.make_ngram(string_Y, n))

# show X and Y
print("X {}-gram: ".format(n),X)
print("Y {}-gram: ".format(n),Y)
# union set
print("union set: ", X|Y)
# product set
print("product set: ", X&Y)
# difference set
print("difference set X-Y: ", X-Y)
print("difference set Y-X: ", Y-X)

print('if "se" in ...')
print("X: ", "se" in X)
print("Y: ", "se" in Y)

