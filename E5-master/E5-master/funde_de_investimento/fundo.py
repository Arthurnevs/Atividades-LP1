'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Fundo de investimento'''

media = 0
acm = 0
cont = 0
while True:
	valor = float(input())
	if media > valor:
		break
	acm += valor 
	cont += 1
	media = acm / cont
print('Saldo total do FIS: R${:.2f}.'.format(acm))
print('Média das contribuições: R${:.2f}.'.format(media))
