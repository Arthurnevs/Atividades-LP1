import math 

print('Cálculo da Superfície de um Cilindro')
print('---')

diam = float(input('Medida do diâmetro? '))
alt = float(input('Medida da altura? '))

raio = diam / 2

ab = math.pi * raio ** 2

al = (2 * raio) * math.pi * alt

at = (2 * ab) + al

print('---')
print('Área calculada: {:.2f}'.format(at))
