peso = float(input())
altura = float(input())

imc = peso / altura**2
peso2 = 24.9 * altura**2
print('IMC atual = {:.2f}'.format(imc))
print('Peso a ser ganho/perdido = {:.2f}'.format(peso2-peso))
