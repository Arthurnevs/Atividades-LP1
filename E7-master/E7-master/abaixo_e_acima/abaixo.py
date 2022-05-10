# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Abaixo e Acima'''

def organiza_por_media(l):
  if len(l) == 0:
    return l

  soma = 0
  for e in l:
    soma += e

  media = soma / len(l)

  for i in range(len(l)-1,-1,-1):
    if l[i] > media:
      for j in range(i,len(l)-1):
        if l[j+1] > media:
          break
        else:
          l[j],l[j+1] = l[j+1],l[j]

  return l

p1 = [1, 2, 4, 1, 3, 4, 56, 7, 7, 4, 3, 67]
assert organiza_por_media(p1) == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]
assert p1 == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]
