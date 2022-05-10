'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Cálculo de Seguro'''

def calcula_seguro(valor, l):
	soma = 0
	r = []
	perfil = ''
	valor_final = 0
	if l[0] <= 21:
		soma += 20
	elif l[0] >= 22 and l[0] <= 30:
		soma += 15
	elif l[0] >= 31 and l[0] <= 40:
		soma += 12
	elif l[0] >= 41 and l[0] <= 60:
		soma += 10
	elif l[0] > 60:
		soma += 20
	
	if l[1]:
		soma += 10
	else:
		soma += 20
		
	if l[2]:
		soma += 20
	else:
		soma += 10
	
	if l[3]:
		soma += 20
	else:
		soma += 10
	
	if l[4]:
		soma += 20
	else:
		soma += 10
	
	if l[5]:
		soma += 10
	else:
		soma += 20
	
	if l[6] == 'Lazer':
		soma += 20
	elif l[6] == 'Trabalho':
		soma += 10 
	else:
		soma += 20
	
	if soma <= 80:
		perfil = 'Risco Baixo'
		valor_final = valor * 0.1
	elif soma > 80 and soma <= 100:
		perfil = 'Risco Medio'
		valor_final = valor * 0.2
	else:
		perfil = 'Risco Alto'
		valor_final = valor * 0.3
	
	r.append(soma)
	r.append(perfil)
	r.append(valor_final)
	
	return r

assert calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto']) == [120, "Risco Alto", 600.0]
