'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
CNPJ

'''

numers = input()
lista = numers.split('.')

matriz = ''

for x in lista:
	matriz = matriz + str(x)
	
soma = 0

for x in matriz:
	soma = soma + int(x)

print('{}/0001-{:02d}'.format(numers,soma + 1))
