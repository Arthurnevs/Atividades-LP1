# coding: utf-8
'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Inverte 3a3'''

def inverte3a3(s):
  n = ''
  for i in range(len(s)-3,-1,-3):
    n += s[i]+s[i+1]+ s[i+2]
  
  return n
  
