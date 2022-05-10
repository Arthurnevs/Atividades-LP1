'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
É TRIANGULO
'''
a = int(input())
b = int(input())
c = int(input())

if(a > abs(b - c) and a < (b + c) and b > abs(a - c) and b < (a + c) and c > abs(a - b) and c < (a + b)):
	print('triangulo valido. {}'.format(a + b + c)) 
else:
	print('triangulo invalido.')
