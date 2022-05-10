letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def get_indice(objeto, lista):
  for indice in range(len(lista)):
    if lista[indice] == objeto:
      return indice 

def adiciona_item(item, lista):  
  valor_item = get_indice(item[0], letras)
  # se precisar comparar outras letras é so mudar esse valor no item[]
  lista.append(item)
  
  for indice in range(len(lista)):
    valor_palavra = get_indice(lista[indice][0], letras)
    # se precisar comparar outras letras é so mudar esse valor no lista[indice][]
    if valor_item < valor_palavra:
      for i in range(len(lista)-1, indice, -1):
        lista[i], lista[i-1] = lista[i-1], lista[i]
      break

