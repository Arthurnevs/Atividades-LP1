""" 
UFCG
Prog 1 
Jose Arthur Neves de Brito - 119210204 
Tabela Quadrados
"""

x = int(input())
y = int(input())

if x > y:
	print("---")

for i in range(x,y+1):
	print('{} {}'.format(i,i**2))
