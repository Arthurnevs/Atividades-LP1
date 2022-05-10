'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Embarque Organizado'''

seq = input().split()
epar = False
msg = 'ok'
l = [1,2,4,6]
for x in seq:
	if int(x) % 2 == 1 and epar:
		msg = 'erro'
		break
	elif int(x) % 2 == 0 and epar == False:
		epar = True
	elif int(x) % 2 == 1:
		continue

print(msg)
		

