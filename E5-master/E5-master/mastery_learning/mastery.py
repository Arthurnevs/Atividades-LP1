'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Mastery Learning'''

print('Mastery Learning')
print('Cálculo da nota na unidade')
print('')

cont = 0
n1 = float(input('Nota? '))
n2 = float(input('Nota? '))
media = (n1 + n2) / 2

if media > 6:
	print('Média: {} (aprovado)'.format(media))
	print('Penalização: {:.1f}'.format(cont))
else:	
	print('Média: {} (cursando)'.format(media))
	print('Penalização: {:.1f}'.format(cont))
print('')

pri = 0
seg = 0
if n1 > n2:
	pri = n1
	seg = n2
else:
	pri = n2 
	seg = n1

while True:
	if media > 6:
		break
	media = 0
	cont += 0.5
	n = float(input('Nota? '))
	if n > pri:
		seg = pri
		pri = n
		
	elif n > seg:
		seg = n
		
	media = (pri + seg) / 2
	if media > 6:
		print('Média: {} (aprovado)'.format(media))
		print('Penalização: {:.1f}'.format(cont))
		print('')
	else:	
		print('Média: {} (cursando)'.format(media))
		print('Penalização: {:.1f}'.format(cont))
		print('')
print('===')
print('Notas válidas: {} e {}'.format(pri,seg))
print('Média parcial na unidade: {}'.format(media))
print('Penalizações: {:.1f}'.format(cont))
print('Média final na unidade: {}'.format(media - cont))
