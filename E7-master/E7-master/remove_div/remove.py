# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Remove Divisores'''

def remove_divisores_k(l, k, n):
	cont = 0
	for i in range(len(l)-1,-1,-1):
		if cont >= n:
			break
		if k % l[i] == 0:
			cont += 1
			l.pop(i)
	return l
