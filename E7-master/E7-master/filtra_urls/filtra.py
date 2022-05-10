def filtra_urls(p1):
  palavra = 'google'
  l = []

  for i in range(len(p1)):
    for j in range(len(p1[i])- len(palavra)):
      if p1[i][j] + p1[i][j+1] + p1[i][j+2] + p1[i][j+3] + p1[i][j+4] + p1[i][j+5] == palavra:
        l.append(p1[i])
        break
  return l
