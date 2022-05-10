'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Controle de Qualidade
'''

antes = float(input())
depois = float(input())

porc = antes - depois
x = (porc * 100)/antes

print('{:.1f}% do peso do produto é de água congelada.'.format(x))

if x < 5:
	print('Produto qualis A.')
elif x < 10:
	print('Produto em conformidade.')
else:
	print('Produto não conforme.')

