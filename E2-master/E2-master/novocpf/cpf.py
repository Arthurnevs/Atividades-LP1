'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
NOVO CPF
'''

p1 = int(input())
p2 =  int(input())
p3 =  int(input())

soma = 0
for x in str(p3):
	soma = int(x) + soma

print('{:03}.{:03}.{:03}-{:02}'.format(p1,p2,p3,soma))
