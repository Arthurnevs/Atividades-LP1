def soma_linha_e_coluna(m,i,j):
  soma = 0
  for k in range(len(m)):
    for l in range(len(m[k])):
      if k == i and l == j:
        continue
      if k == i:
        soma += m[k][l]
      if l == j:
        soma += m[k][l]

  return soma
