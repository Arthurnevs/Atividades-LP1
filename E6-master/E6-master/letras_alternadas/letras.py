'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Letras Alternadas'''

def letras_alternadas(string):
	s = ''
	for i in range(0,len(string),2):
		s += string[i] 
	
	return s
	
assert letras_alternadas("casa") == 'cs'
assert letras_alternadas("exemplo") == "eepo"
