'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Multiplica Lista'''

def multiplica_lista(n,lista):
	
	nova = []
	cont = 0
	
	while True:
		if cont >= n:
			break
		for e in lista:
			nova.append(e)
		cont += 1
	return nova
