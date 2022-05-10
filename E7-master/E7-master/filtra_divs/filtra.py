# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Filtra Divisores'''

def filtra_divisores(l):
  for e in range(len(l)-1,-1,-1):
    s = str(l[e])
    soma = 0
    for i in range(len(s)):
      soma += int(s[i])
    
    if l[e] % soma != 0:
      l.pop(e)
  
  print(l)

lista1 = [333, 121, 81]
assert filtra_divisores(lista1) == None
assert lista1 == [333,81]
