'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
CONSTRUCAO CONDOMINIO

'''
l1 = float(input())
l2 = float(input())

area = float(input())
area_terreno = l1 * l2

qtd_casas = area_terreno // area

print('{} casa(s) pode(m) ser construída(s) no terreno.'.format(int(qtd_casas)))
