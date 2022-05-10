'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Meu Join'''

def meu_join(delimitador, sequencia_de_string):
	nova = ''
	for i in range(len(sequencia_de_string)):
		if i == len(sequencia_de_string) - 1:
			nova += sequencia_de_string[i]
		else:
			nova += sequencia_de_string[i]
			nova += delimitador
	return nova

