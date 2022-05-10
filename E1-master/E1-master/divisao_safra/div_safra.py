'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
SAFRA

'''

qtd_soja = int(input())
qtd_atac = int(input())
qtd_var = int(input())

cli_atac = qtd_soja // qtd_atac

resto_atc = qtd_soja%qtd_atac

cli_var = (resto_atc)/qtd_var

print('Clientes no atacado = {}kg cada.'.format(cli_atac))
print('Clientes no varejo = {:.2f}kg cada.'.format(cli_var))
