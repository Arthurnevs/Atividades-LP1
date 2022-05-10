# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Email Perdido'''

def encontra_email_perdido(env,rec):
	email = False
	for i in range(len(env)):
		for j in range(len(rec)):
			if env[i] == rec[j]:
				email = True
				break
			else:
				email = False
		if email == False:
			return env[i] 


