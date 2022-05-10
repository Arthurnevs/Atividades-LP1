'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Questões para P1'''

total = 0
soma = 0
print('Relatório de novas questões:')
print('')
while True:
	total += soma
	nome = input()
	soma = 0
	if nome == '**':
		break
	while True:
		q = input()
		if q == '*':
			break
		soma += int(q)
	print('{}: {}'.format(nome,soma))

print('---')
print('Total de novas questões: {}'.format(total))		
