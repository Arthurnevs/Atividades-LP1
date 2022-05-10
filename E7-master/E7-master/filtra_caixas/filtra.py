# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Inverte 3a3'''

def lista_so_com_oposto(l):
  tem_oposto = False
  for i in range(len(l)-1,-1,-1):
    for j in range(len(l)-1,-1,-1):
      if l[i] + l[j] == 0:
        tem_oposto = True
        break
      else:
        tem_oposto = False
    if tem_oposto == False:
      l.pop(i)
  return None
  
lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
assert lista_so_com_oposto(lista1) == None
assert lista1 == [1, 1, 3, -1, -3]
