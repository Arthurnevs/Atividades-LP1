'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Limpeza'''

tipo = input()
if tipo == '1':
	tamanho = int(input())
	preco = tamanho * 80.0
	print('R$ {:.0f},00'.format(preco))
	if preco >= 200:
		print('Brinde!')
elif tipo == '2':
	tamanho = int(input())
	preco = tamanho * 50.0
	print('R$ {:.0f},00'.format(preco))
	if preco >= 200:
		print('Brinde!')
else:
	print('R$ 50,00')
