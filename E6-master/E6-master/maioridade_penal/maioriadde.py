'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Maioridade Penal'''

def maioridade_penal(nome,idade):
	a = nome.split()
	b = idade.split()
	s = ''
	for i in range(len(b)):
		if int(b[i]) >= 18:
			if i == len(b)-1:
				s += a[i]
			else:
				s += a[i]
				s += ' '
				 
	return s 
