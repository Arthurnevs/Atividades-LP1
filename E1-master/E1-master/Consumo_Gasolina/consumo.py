'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Consumo Gasolina

'''

pos_inicial = float(input())
litros_inicial = float(input())

pos_final = float(input())
litros_final = float(input())

dist = pos_final - pos_inicial
cons = litros_inicial - litros_final

print('{:.1f}'.format(dist/cons))
