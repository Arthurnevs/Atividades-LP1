import math
diam = int(input())

raio = diam / 2

area = math.pi * (raio**2)
perimetro = 2 * math.pi * raio

print('A: {:.5f}'.format(float(area)))
print('P: {:.5f}'.format(float(perimetro)))
