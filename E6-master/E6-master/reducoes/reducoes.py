'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Reducoes'''

def reducoes(seq):
	nova = []
	dif = 0
	for i in range(len(seq)-1):
		dif = seq[i] - seq[i+1]
		if dif < 0:
			dif = 0
			nova.append(dif)
		else:
			nova.append(dif)
	
	return nova
	
assert reducoes([4, 2, 0, 6, 3, 4]) == [2, 2, 0, 3, 0]
assert reducoes([3, 0, 3, 6, 1]) == [3, 0, 0, 5]

