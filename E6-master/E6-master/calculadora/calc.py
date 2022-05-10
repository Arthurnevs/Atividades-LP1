def adicao(a,b):
	print(a + b) 

def subtracao(a,b):
	print(a - b) 

def mult(a,b):
	print(a * b) 

def div(a,b):
	print(a // b)
	
while True:
	seq = input().split()
	if seq[0] == '5':
		break
	elif seq[0] == '1':
		adicao(int(seq[1]),int(seq[2]))
	elif seq[0] == '2':
		subtracao(int(seq[1]),int(seq[2]))
	elif seq[0] == '3':
		mult(int(seq[1]),int(seq[2]))
	elif seq[0] == '4':
		if int(seq[2]) == 0:
			print('Erro: Divisão por 0')
			break 
		else:
			div(int(seq[1]),int(seq[2]))
	
	
