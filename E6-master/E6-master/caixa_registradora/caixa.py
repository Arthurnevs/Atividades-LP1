'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Caixa Registradora'''

def caixa_registradora(lista,meta):
	soma = 0
	com = 0
	situacao = ''
	l = []
	for e in lista:
		soma += e
		if e < 1000:
			com += 0.05 * e
		elif e >= 1000 and e < 5000:
			com += 0.1 * e
		elif e >= 5000:
			com += 0.15 * e
	if soma - com >= meta:
		situacao = 'Lucro'
	else:
		situacao = 'Prejuizo'
	
	l.append(soma)
	l.append(com)
	l.append(situacao)
	
	return l 

assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']	
