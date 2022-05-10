'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Status'''

a = float(input())
b = float(input())
c = float(input())

faltas = int(input())

media = (a + b + c) / 3

if media >= 7 and faltas < 23:
	print('aprovado por media')
elif faltas >= 23:
	print('reprovado por faltas')
elif media >= 4 and media < 7:
	print('prova final')
else:
	print('reprovado por nota')
