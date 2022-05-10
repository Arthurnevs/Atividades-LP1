'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Plif Plof'''

a = int(input())
b = int(input())
c = int(input())

soma = a + b + c

if soma % 3 == 0 and soma % 5 == 0:
	print('plifplof')
elif soma % 3 == 0 and soma % 5 != 0:
	print('plif')
else:
	print('plof')
