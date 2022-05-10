'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Sequencia'''

lim = int(input())
soma = 1

for i in range(0,lim):
	if soma * 2 > lim:
		break
	print(soma)
	soma = soma * 2
	
