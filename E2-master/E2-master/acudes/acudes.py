'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
AÇUDES
'''

capacidade = float(input('capacidade? '))
percentual = float(input('percentual hoje? '))
gasto = float(input('gasto diário? '))

volume = capacidade * (percentual/100)
dias = volume / gasto

print('volume: {:.2f}'.format(volume))
print('dias restantes: {}'.format(int(dias)))
