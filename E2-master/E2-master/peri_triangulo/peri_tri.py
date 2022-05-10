'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
PERIMETRO TRIANGULO

'''

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

d1 = ((x1 - x2)**2) + ((y1 - y2)**2)
aux1 = d1 ** 0.5


d2 = ((x1 - x3)**2) + ((y1 - y3)**2)
aux2 = d2 ** 0.5
 
d3 = ((x2 - x3)**2) + ((y2 - y3)**2)
aux3 = d3 ** 0.5

print('O perímetro é de {:.2f}'.format(aux1 + aux2 + aux3))
