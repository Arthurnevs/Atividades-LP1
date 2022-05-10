'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
MORANGOS
'''
t = int(input())

msg = t // 400 

print('Serão necessárias {} caixa(s) para embalar os morangos.'.format(msg))

porcent = ((t%400) * 100)/t

print('{:.1f}% dos morangos serão perdidos.'.format(porcent))
