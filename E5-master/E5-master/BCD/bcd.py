'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
BCD'''

while True:
	num1 = ''
	num2 = ''
	bit = input()
	if bit == 'fim':
		break
	
	for i in range(len(bit)):
		if i < 4:
			num1 += str(bit[i])
		else:
			num2 += str(bit[i])	
		
	if len(bit) != 8:
		print('Tente novamente.')
				
	elif int(num1,2) > 9 or int(num2,2) > 9:
		print('BCD inválido.')
	else:
		bcd1 = int(num1,2)
		bcd2 = int(num2,2)
		print('{}{}'.format(bcd1,bcd2))
