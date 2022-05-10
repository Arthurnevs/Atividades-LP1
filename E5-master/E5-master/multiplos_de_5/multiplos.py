'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Múltiplos de 5 '''

lim = int(input())
cont = 0
while cont < lim:
	if cont % 5 == 0 and cont % 2 == 0 and cont > 0:
		print(cont)
	cont += 1
		 
