'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Acima da Média'''

media = float(input())
soma = 0
while True:
	valores = input()
	if valores == 'fim':
		break
	else:
		soma = 0
		l = valores.split()
		for i in range(len(l)):
			soma += int(l[i])
		sem = soma / len(l)
		if sem < media/2:
			break
		elif sem > media:
			print(valores)
		
		
		 
			
			
	
