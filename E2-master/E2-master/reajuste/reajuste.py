'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
REAJUSTE SALARIO MINIMO
'''
valor = float(input('Valor atual? '))
novo = float(input('Novo valor? '))

delta = novo - valor

reajuste = (delta * 100)/valor


print('Reajuste de {:.1f}%'.format(reajuste))
