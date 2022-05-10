'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Categoria
'''
nome = input()
idade = int(input())

if(idade < 5):
	print('{}, {} anos, Não pode competir.'.format(nome,idade))
elif(idade >= 5 and idade <= 7):
	print('{}, {} anos, Infantil A.'.format(nome,idade))
elif(idade >= 7 and idade <= 10):
	print('{}, {} anos, Infantil B.'.format(nome,idade))
elif(idade >= 10 and idade <= 13):
	print('{}, {} anos, Juvenil A.'.format(nome,idade))
elif(idade >= 13 and idade <= 17):
	print('{}, {} anos, Juvenil B.'.format(nome,idade))
else:
	print('{}, {} anos, Senior.'.format(nome,idade))
