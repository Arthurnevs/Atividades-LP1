import math

lado = float(input())

raio = (lado/2)**2 + (lado/2) **2 

perimetro = 2 * math.pi * (raio ** 0.5)

area = math.pi * ((raio ** 0.5)**2)

print('Perímetro: {:.5f}'.format(perimetro))
print('Área: {:.5f}'.format(area)) 

