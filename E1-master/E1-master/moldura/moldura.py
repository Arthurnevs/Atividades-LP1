'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
CALCULA MOLDURA

'''

comp = float(input())
larg = float(input())

valor_mold = ((2 * comp + 2 * larg)/100)*120
print('R$ {:.1f}'.format(valor_mold))
