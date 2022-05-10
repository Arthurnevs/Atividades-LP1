nome = input()
qtd_hora = float(input())
var_salario = float(input())
var_hora = float(input())


hora_extra = var_hora * qtd_hora

bruto = 4 * var_salario + hora_extra
desconto_inss = 0.12 * bruto
desconto_ir = 0.2 * bruto
liquido = bruto - desconto_inss - desconto_ir

print('O Salário Bruto de {} é de R$ {:.2f}'.format(nome,bruto))
print('O Salário Líquido de {} é de R$ {:.2f}'.format(nome,liquido))
