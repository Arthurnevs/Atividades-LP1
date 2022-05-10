'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Calculando a Hipotenusa
'''
import math

c1 = float(input('Medida do Cateto 1? '))
c2 = float(input('Medida do Cateto 2? '))

h = math.sqrt(c1 ** 2 + c2 ** 2)


print('Medida da Hipotenusa: {:.2f}'.format(h))
