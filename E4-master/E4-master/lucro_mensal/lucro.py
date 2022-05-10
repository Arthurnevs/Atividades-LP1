""" 
UFCG
Prog 1 
Jose Arthur Neves de Brito - 119210204 
Lucro Mensal
"""

mes = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
lucro=[]
for i in range(12):
	valor = input()
	l = valor.split()
	
	lucro.append(float(l[0])-float(l[1]))
	print('{} {:4.1f}'.format(mes[i],lucro[i]))
	
