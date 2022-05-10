
def verifica_esteira(l1,l2):

  aux = []

  for i in range(len(l2)):
    for j in range(len(l1)):
      if l2[i] == l1[j]:
        aux.append(j)
        break
  
  if len(l2) != len(aux):
	  return False
	  
  e_crescente = True
  for i in range(len(aux)-1):
    if aux[i] > aux[i+1]:
      e_crescente = False
      break
    else:
      e_crescente = True

  return e_crescente


l1 = [2,1,3,4]
l2 = [0]
print(verifica_esteira(l1,l2))


