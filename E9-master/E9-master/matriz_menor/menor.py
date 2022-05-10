def matriz_menor(m1, m2):
  
  l = []
  aux = []

  for i in range(len(m1)):
    aux = []
    for j in range(len(m1[i])):
      if m1[i][j] < m2[i][j]:
        aux.append(m1[i][j])
      else:
        aux.append(m2[i][j])
    l.append(aux)

  return l
