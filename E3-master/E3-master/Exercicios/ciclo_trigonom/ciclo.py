'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Ciclo trigonométrico
'''

a = int(input())

ang = 0

num_voltas = (a // 360) 
ang = a - (num_voltas * 360)

if ang == 0 or ang == 90 or ang == 180 or ang == 270 or ang == 360:
	print("Sobre eixos")
elif ang < 90:
	print("Quadrante 1")
elif ang > 90 and ang < 180:
	print('Quadrante 2')
elif ang > 180 and ang < 270:
	print('Quadrante 3')
else:
	print('Quadrante 4')
