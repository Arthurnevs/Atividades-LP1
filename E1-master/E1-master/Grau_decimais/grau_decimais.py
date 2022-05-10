grau = float(input())
min = float(input())
seg = float(input())

conversor = seg / 60
min = min + conversor
conversor = min / 60 
grau = grau + conversor

print('graus = {:.4f}'.format(grau))
