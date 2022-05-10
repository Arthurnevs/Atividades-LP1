def distribui_materia_prima(esteira,n):
  f = []
  aux = []
  for j in range(n):
    for i in range(j,len(esteira),n):
      aux.append(esteira[i])
    f.append(aux)
    aux = []
  
  return f

esteira_de_materia_prima = ['camera', 'fone', 'microfone', 'processador', 'tela']
assert distribui_materia_prima(esteira_de_materia_prima, 3) == [['camera', 'processador'],['fone', 'tela'], ['microfone']]
