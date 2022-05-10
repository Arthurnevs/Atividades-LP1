adult = int(input())
crian = int(input())
preco = float(input())

preco_final = (crian * (preco/2)) + (adult * preco)

print('Total: R$ {:.2f}'.format(preco_final))
