# -*- coding: utf-8 -*-

# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def print_string(x,y,z):
	# print("{0}時の{1}は{2}".format(x,y,z))
	print("{}時の{}は{}".format(x,y,z))

if __name__=='__main__':
	x = 12
	y = "気温"
	z = 22.4
	print_string(x, y, z)
