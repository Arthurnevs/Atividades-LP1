'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Nota Fiscal

'''
valor_total = float(input())
data = input()
qtd_produtos = float(input())

media = valor_total/qtd_produtos

print('Data: {}'.format(data))
print('O valor total da compra foi de R$ {:.2f}. A média do preço dos produtos é de {:.1f}.'.format(valor_total,media))
