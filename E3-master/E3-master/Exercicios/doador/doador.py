'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Doador
'''

recep = input()
recepRH = input()

doador = input()
doadorRH = input()

if(recep == 'AB'):
	if(recepRH == '-' and doadorRH == '+'):
		print('incompatível')
	else:
		print('compatível')
elif(recep == 'A'):
	if(doador == 'B' or doador == 'AB'):
		print('incompatível')
	elif(recepRH == '-' and doadorRH == '+'):
		print('incompatível')
	else:
		print('compatível')
elif(recep == 'B'):
	if(doador == 'A' or doador == 'AB'):
		print('incompatível')
	elif(recepRH == '-' and doadorRH == '+'):
		print('incompatível')
	else:
		print('compatível')
else:
	if(doador != 'O'):
		print('incompatível')
	elif(recepRH == '-' and doadorRH == '+'):
		print('incompatível')
	else:
		print('compatível')
