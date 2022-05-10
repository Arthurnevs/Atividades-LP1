base = float(input())
dias = int(input())
transporte = float(input())

liquido = base

custo_transporte = dias * transporte

custo_empregado = 0.08 * base + 0.12 * base + base

if(custo_transporte > 0.06 * base):
	liquido -= 0.06 * base
	custo_empregado += custo_transporte - 0.06 * base

if(base < 1317.07):
	liquido -= 0.08 * base
elif(base > 1317.08 and base < 2195.12):
	liquido -= 0.09 * base
else:
	liquido -= 0.11 * base

print('O salário base é R$ {:.2f}'.format(base))
print('O custo mensal para o empregador é de R$ {:.2f}'.format(custo_empregado))
print('O salário líquido que o trabalhador irá receber no mês é R$ {:.2f}'.format(liquido))	
