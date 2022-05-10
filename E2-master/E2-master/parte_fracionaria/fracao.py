'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
PARTE FRACIONARIA

'''

import math

num = float(input())
inti = math. floor ( num ) 
frac = float(num) - float(inti)

print('{:.1f}'.format(frac))
