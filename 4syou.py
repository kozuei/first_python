def cha1(x):
	"""
	数字を入力値として受け取ります
	戻り値はその数字を二乗したものです
	"""
	return x**2

print(cha1(3))

def text(mojimoji):
	"""
	文字列が引数です
	文字列を出力します
	"""
	print(mojimoji)

text("challenge2")

def g(o,y,t,u=100,h=20):
	"""
	必須引数は数値です
	四則演算の結果を表示します
	"""
	return o+y-u+h
	
result=g(3,4,5)
print(result)

def seisu(x):
	"""
	引数は全て数値です
	xを2で割った数が次の関数の引数になります
	"""
	return x/2

def seisu2(x):
	return x*4

i=seisu(8)
o=seisu2(i)

print(o)

def henkan(moji):
	"""
	引数は文字列です
	文字列を変換し浮動小数点数にします
	例外処理もあります
	"""
	try:
		return float(moji)
	except ValueError:
		print("henkan dekimasen")
d=henkan("moji")
print(d)
