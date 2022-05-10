def transposta(m):
  l = []
  aux = []

  k = 0
  while k <= len(m[0])-1:
    aux = []
    for i in range(len(m)):
      aux.append(m[i][k])
    l.append(aux)
    k += 1

  return l
