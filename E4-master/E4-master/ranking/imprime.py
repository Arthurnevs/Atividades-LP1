'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Imprime ranking'''

n = int(input())

times = []
pontos = []

#For para gerar inputs
for i in range(n):
	time = input()
	times.append(time)
	ponto = int(input())
	pontos.append(ponto)


print('1. {} ({})'.format(times[0],pontos[0]))

cont = 0

for j in range(1,n):
	if pontos[j] != pontos[j-1]:
		print('{}. {} ({})'.format(j +1, times[j],pontos[j]))
	else:
		for k in range(j,0,-1):
			if pontos[k] == pontos[k-1]:
				cont += 1
			else:
				break
				
		print('{}. {} ({})'.format(j - cont +1, times[j],pontos[j]))
	cont = 0
