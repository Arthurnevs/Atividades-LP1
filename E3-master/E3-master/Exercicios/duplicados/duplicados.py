'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Duplicados
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a == b or a == c or a == d or a == e:
	print('com duplicados')
elif b == a or b == c or b == d or b == d:
	print('com duplicados')
elif c == a or c == b or c == d or c == e:
	print('com duplicados')
elif d == a or d == b or d == c or d == e:
	print('com duplicados')
else:
	print('sem duplicados')
