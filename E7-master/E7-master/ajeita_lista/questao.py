def ajeita_lista(lista):
	cont1 = 0
	for i in range(len(lista)):
		if lista[i] % 2 == 0:
			lista[i],lista[cont1] = lista[cont1], lista[i]
			cont1 += 1
	for a in range(cont1-1,0,-1):
		for j in range(cont1-1,0,-1):
			if lista[j] > lista[j-1]:
				lista[j],lista[j-1] = lista[j-1], lista[j]
				
	for b in range(cont1,len(lista)-1):
		for k in range(cont1,len(lista)-1):
			if lista[k] > lista[k+1]:
				lista[k],lista[k+1] = lista[k+1],lista[k]
	
	
l = [1,-8,3,2,0]
