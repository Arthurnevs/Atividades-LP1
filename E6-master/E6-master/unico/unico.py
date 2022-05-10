'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Unico'''

def unico(a):
	n = ''
	for i in range(len(a)):
		if i == 0:
			n+= a[0]
		elif a[i] == a[i-1]:
			continue
		else:
			n += a[i]	
	return n

