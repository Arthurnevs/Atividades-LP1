'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
B2 para B10'''

num = input()
dec = 0
cont = len(num)-1
for i in range(len(num)):
	dec += int(num[i]) * (2 ** cont)
	print('{} * {} = {}'.format(int(num[i]), 2 ** cont,int(num[i]) * (2 ** cont)))
	cont -=1
	
print('{}(2) = {}(10)'.format(num,dec))
