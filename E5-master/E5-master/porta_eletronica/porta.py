'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Porta Eletronica
'''
cont = 0
l = []
while True:
	a = input()
	if a == 'S':
		break
	elif a[0] == 'R':
		l.append(a)
	else:
		cont = 0
		for i in range(len(l)):
			if l[i][2] == a[2]:
				cont += 1
		print(cont)
				
	

