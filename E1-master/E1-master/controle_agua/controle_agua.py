'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
CONTROLE DE AGUA

'''
import math

vel_vazao = float(input())
diam = float(input())
temp = int(input())

seccao = (math.pi * (diam/2)**2)
vazao = vel_vazao * seccao * 1000

qtd_agua = vazao * temp

print("Quantidade de água = {:.10f} litros.".format(qtd_agua))
