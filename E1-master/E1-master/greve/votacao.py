'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Greve
'''


abst = int(input())
afav = int(input())
contra = int(input())

total = abst + afav + contra

print('Resultado da Votação')
print('')
print('{} abstenções ({:.2f}%)'.format(abst, (abst * 100) / total))
print('{} a favor ({:.2f}%)'.format(afav, (afav * 100) / total))
print('{} contra ({:.2f}%)'.format(contra, (contra * 100) / total))
