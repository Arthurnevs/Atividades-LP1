'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Coincidentes'''

a = input()
b = input()

tam = 0
soma = 0
total = len(a) + len(b)

if len(a)> len(b):
	tam = len(b)
else:
	tam = len(a)
print('Letras coincidentes')
for i in range(tam):
	if a[i] == b[i]:
		soma += 1
		print("'{}' na posição {}".format(a[i],i+1))

print('Total de letras coincidentes: {} ({:.0f}%)'.format(soma,(soma * 100)/total)) 

