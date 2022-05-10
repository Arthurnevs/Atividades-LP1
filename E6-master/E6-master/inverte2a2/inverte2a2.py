# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Inverte 2a2'''
def inverte2a2_condicional(seq):
  if len(seq) % 2 == 0:
    for i in range(0,len(seq),2):
      if seq[i] > seq[i+1]:
        seq[i],seq[i+1] = seq[i+1],seq[i]
  else:
    for i in range(0,len(seq)-1,2):
      if seq[i] > seq[i+1]:
        seq[i],seq[i+1] = seq[i+1],seq[i]
  return seq
