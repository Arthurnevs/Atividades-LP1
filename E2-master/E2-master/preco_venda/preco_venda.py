'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
PRECO DE VENDA
'''

custo = float(input())
desp_indireta = float(input())
lucro_desj = float(input())
impostos = float(input())
comissao = float(input()) 
desc = float(input())
encargos = float(input())

preco = ((custo + desp_indireta + lucro_desj)*100) / 100 - ((impostos - comissao - desc - encargos))

print(preco)
