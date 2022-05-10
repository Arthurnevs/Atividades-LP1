'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
QUADRADO NA CIRCUNFERENCIA

'''

import math

raio = float(input())

x = raio ** 2 + raio ** 2
lado = x ** 0.5

area = (math.pi * (raio ** 2)) - (lado * lado)

print('Área não comum: {:.5f}'.format(area))
