'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
IPTU
'''
area = float(input())
valor = float(input())
opcao = input()

iptu = area * valor

vista = iptu - (iptu * 0.2)
duas = iptu - (iptu * 0.1)
tres = iptu - (iptu * 0.05)


if(opcao == 'vista'):
	print('Total: R$ {:.2f}'.format(vista))
elif(opcao == '2x'):
	print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(duas,duas/2))
else:
	print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(tres,tres/3))
	
