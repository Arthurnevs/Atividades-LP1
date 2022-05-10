'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Get Items'''

def get_items(valores, indices):
	l = []
	
	for i in indices:
		if i > len(valores)-1:
			l.append(None)
		else:
			l.append(valores[i])
	return l

