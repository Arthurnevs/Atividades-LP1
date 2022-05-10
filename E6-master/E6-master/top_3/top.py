'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Top 3 '''

def top_3(l):
	maior = 0
	cont = 0
	for j in range(3):
		for i in range(j,len(l)):
			if i == cont:
				maior = l[cont]
			if l[i] > maior:
				maior = l[i]
				l[cont],l[i] = l[i],l[cont]
		cont += 1
	return l
	


