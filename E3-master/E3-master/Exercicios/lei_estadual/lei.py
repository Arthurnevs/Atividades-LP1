'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Lei Estadual
'''
idade = int(input("Idade? "))

if(idade < 12):
	print('criança (meia entrada)')
elif(idade >= 65):
	print('idoso (meia entrada)')
else:
	estudante = input('Estudante? ')
	if(estudante == 's'):
		rp = input('Rede Pública? ')
		if(rp == 's'):
			print('estudante da rede pública (isento)')
		else:
			print('estudante (meia entrada)')
	else:
		print('adulto (inteira)')
