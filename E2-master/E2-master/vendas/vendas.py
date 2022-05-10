total = int(input())
teresa = int(input())
carla = int(input())

porcen_carla = (carla * 100)/total
porcen_teresa = (teresa * 100)/total

joaquim = total - (carla + teresa)
porcen_joaquim = 100 -(porcen_carla + porcen_teresa)

print('Teresa vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(teresa,total,porcen_teresa))
print('Joaquim vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(joaquim,total,porcen_joaquim))
print('Carla vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(carla,total,porcen_carla))
