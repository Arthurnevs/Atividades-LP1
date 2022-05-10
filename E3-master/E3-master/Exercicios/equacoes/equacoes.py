'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Equações
'''
import math

a = int(input())
b = int(input())
c = int(input())

delta = (b ** 2) - (4 * a * c)

if(delta > 0):
	x1 = (-b + math.sqrt(delta)) / (2 *a)
	x2 = (-b - math.sqrt(delta)) / (2 * a)
	print('x1 = {:.2f}'.format(x1))
	print('x2 = {:.2f}'.format(x2)) 
elif(delta < 0):
	print('sem raizes reais')
else:
	x = -b / (2 * a)
	print('x = {:.2f}'.format(x))	
