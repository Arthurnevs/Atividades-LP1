""" 
UFCG
Prog 1 
Jose Arthur Neves de Brito - 119210204 
Caixa Preta
"""

n = int(input())
cont = 0
eh_valido = True

for i in range(n):
	peso, combustivel, altitude = input().split()
	
	if int(peso) >= 0 and eh_valido:
		cont += 1
	elif eh_valido:
		eh_valido = False
		print('dado inconsistente. peso negativo.')
	
	if int(combustivel) >= 0 and eh_valido:
		cont += 1
	elif eh_valido:
		eh_valido = False
		print('dado inconsistente. combustível negativo.')
	
	if int(altitude) >= 0 and eh_valido:
		cont += 1
	elif eh_valido:
		eh_valido = False
		print('dado inconsistente. altitude negativa.')

print('{} dados válidos.'.format(cont))
	
	
	
