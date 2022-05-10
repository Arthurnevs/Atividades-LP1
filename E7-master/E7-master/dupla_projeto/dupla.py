def insere_nome(a1,duplas,a2):
  nome_encontrado = False
  for i in range(len(duplas)):
    if duplas[i] == a2:
      duplas.append(a1)
      nome_encontrado = True
      for j in range(len(duplas)-1,i,-1):
        duplas[j],duplas[j-1] = duplas[j-1],duplas[j]
      break
  if nome_encontrado == False:
    duplas.append(a1)

