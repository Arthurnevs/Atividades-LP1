'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Analytics Assembleia '''

def conta_votos(votacoes,idd):
	sim = 0
	nao = 0
	n = []
	for i in range(len(votacoes)):
		l = votacoes[i].split(',')
		if int(l[2]) == idd:
			if l[1] == 'sim':
				sim += 1
			else:
				nao += 1
	
	n.append(sim)
	n.append(nao)
	return n
			

	
