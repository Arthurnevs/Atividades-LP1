'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Grep'''

palavra = input()

n = int(input())

for i in range(n):
	frase = input()
	for j in range(len(frase)-2):
		if frase[j]+frase[j+1]+frase[j+2] == palavra:
			print(frase)
		
