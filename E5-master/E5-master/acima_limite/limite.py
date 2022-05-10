'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Acima do Limite'''

lim = int(input())
soma = 0
p = ''
while True:
	val = input()
	soma = 0
	p = ''
	if val == '-':
		break
	l = val.split()
	for i in range(len(l)):
		soma += int(l[i])
		if p != '':
			p += ' + '
		p += l[i]
	if soma >= lim:
		p += ' = {}'.format(str(soma))	
		print(p)
	else:
		pass
	if soma > 5 * lim:
		break
