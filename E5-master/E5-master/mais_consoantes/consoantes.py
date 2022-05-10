'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Mais Consoantes '''

vogais = ['a','e','i','o','u','A','E','I','O','U']
qtd_palavras = 0
while True:
	palavra = input()
	qtd_palavras += 1
	cons = 0
	vog = 0
	for i in range(len(palavra)):
		if palavra[i] in vogais:
			vog += 1	
		else:
			cons += 1
	if cons > vog:
		break

print(qtd_palavras)
