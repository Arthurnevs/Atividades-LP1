'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
DESPESA CINEMA

'''
orcamento = float(input("Orçamento? R$ "))
num_adultos = int(input("Número de adultos? "))
num_criancas = int(input("Número de crianças? "))
pizza = float(input("Preço da pizza? R$ "))
refrigerante = float(input("Preço do refrigerante? R$ "))
estacionamento = float(input("Preço do estacionamento? R$ "))
ingresso = float(input("Preço do ingresso do cinema? R$ "))

alimentacao = pizza + refrigerante
cinema = (num_adultos * ingresso + 2 * num_adultos) + (num_criancas * (ingresso/2) + num_criancas * 2)
por_pessoa = (cinema + alimentacao + estacionamento) / (num_adultos + num_criancas)
total = alimentacao + cinema + estacionamento
saldo = orcamento - total

print('========== Despesas do cinema ==========')
print("Alimentacao: R$ {:.2f}".format(alimentacao))
print("Cinema: R$ {:.2f}".format(cinema))
print("Custo médio por pessoa: R$ {:.2f}".format(por_pessoa))
print("Total: {:.2f}".format(total))
print("Saldo após passeio: {:.2f}".format(saldo))
