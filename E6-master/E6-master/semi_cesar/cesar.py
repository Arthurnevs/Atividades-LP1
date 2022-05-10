# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Semi Cesar
'''

def cesar(l, d):
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	n = ''
	for i in range(len(l)):
		letra_valida = False
		for j in range(len(alfabeto)):
			if l[i] == alfabeto[j]:
				letra_valida = True
				if j + d > len(alfabeto)-1:
					n += alfabeto[j + d - 26]
					break
				else:
					n += alfabeto[j + d]
					break
		if letra_valida == False:
			n += l[i]
	
	return n	

