'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Mais Velhos Primeiro'''

def idosos_inicio(fila):
	for i in range(len(fila)):
		if fila[i] >= 60:
			for j in range(len(fila)):
				if fila[j] < 60:
					fila[j],fila[i] = fila[i],fila[j]
					break
	print(fila)
	

