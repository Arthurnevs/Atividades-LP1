'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Telefonia
'''

a = int(input())

preco = 0

if a <= 3:
	preco = a * 0.5 + 1
elif a > 3:
	taxa = a // 5
	resto = a % 5
	preco = taxa * 3 + resto * 0.7 + 1   	

print('R$ {:.2f}'.format(preco))
