'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Seleção Projeto
'''

cre = float(input())
experiencia = int(input())
nota = int(input())

if(cre < 7 and experiencia < 6):
	print('Candidato eliminado. CRE e experiência abaixo do limite.')
elif(cre < 7 and experiencia >= 6):
	print('Candidato eliminado. CRE abaixo do limite.')
elif(cre >= 7 and experiencia < 6):
	print('Candidato eliminado. Experiência abaixo do limite.')
else:
	if(nota <= 3):
		print('Candidato classificado.')
	else:
		print('Candidato aprovado.')
		
