'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Abaixo da Média'''

l = []
soma = 0

while True:
	n = input()
	if n == 'fim':
		break
	soma += int(n)
	l.append(n)
	
media = soma / len(l)
print('{:.2f}'.format(media))

for i in range(len(l)):	
	if int(l[i]) < media:
		print('{} {}'.format(i+1,l[i]))
