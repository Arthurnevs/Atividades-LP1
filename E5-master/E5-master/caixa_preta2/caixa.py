'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Caixa Preta (descartando leituras)'''

peso = 0
comb = 0
alt = 0
while True:
	dados = input()
	l = dados.split()
	if int(l[0]) < 0:
		print('dado inconsistente. peso negativo.')
		break
	else:
		peso += 1
	
	if int(l[1]) < 0:
		print('dado inconsistente. combustível negativo.')
		break
	else:
		comb += 1
	
	if int(l[2]) < 0:
		print('dado inconsistente. altitude negativa.')
		break
	else:
		alt += 1
print('peso: {}'.format(peso))
print('combustível: {}'.format(comb))
print('altitude: {}'.format(alt))
