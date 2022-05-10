'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Percentagem de aprovados
'''

print('Análise da Turma')
print('===')
ap = int(input('Número de aprovados? ')) 
re = int(input('Número de reprovados? '))
print('---')

total = ap + re
porcent_ap = (ap * 100) / total
porcent_re = (re * 100) / total

print('Total de alunos na turma: {}'.format(total))
print('Aprovados: {} = {:.1f}%'.format(ap,porcent_ap))
print('Reprovados: {} = {:.1f}%'.format(re,porcent_re))
