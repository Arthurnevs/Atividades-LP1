'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Salario
'''

salario_bruto = float(input())
horas_de_trabalho = float(input())

ganhos_por_hora = salario_bruto / horas_de_trabalho



ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindc = 0.05 * salario_bruto

liquido = salario_bruto - (ir + inss + sindc)

hr_liquida = (ganhos_por_hora * liquido) / salario_bruto

print('Salário Bruto = {:.2f}'.format(salario_bruto))
print('Hora Bruta = {:.2f}'.format(ganhos_por_hora))
print('Desconto IR = {:.2f}'.format(ir))
print('Desconto INSS = {:.2f}'.format(inss))
print('Desconto Sindicato = {:.2f}'.format(sindc))
print('Salário Líquido = {:.2f}'.format(liquido))
print('Hora Líquida = {:.2f}'.format(hr_liquida))
