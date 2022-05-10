'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Concurso
'''

a1 = float(input())
a2 = float(input())
a3 = float(input())
a_idade = int(input())

b1 = float(input())
b2 = float(input())
b3 = float(input())
b_idade = int(input())

na = (a1 * 30 + a2 * 40 + a3 * 30)/(30 + 40 + 30)
nb = (b1 * 30 + b2 * 40 + b3 * 30)/(30 + 40 + 30)

if na == nb:
	if a_idade > b_idade:
		print('O primeiro candidato foi aprovado com média {:.1f}.'.format(na))
	elif b_idade > a_idade:
		print('O segundo candidato foi aprovado com média {:.1f}.'.format(nb))
	else:
		print('Empate.')
elif na > nb:
	print('O primeiro candidato foi aprovado com média {:.1f}.'.format(na))
else:
	print('O segundo candidato foi aprovado com média {:.1f}.'.format(nb))
