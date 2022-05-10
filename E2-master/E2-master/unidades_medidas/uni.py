metros = float(input())

jarda = (metros/91.44)*100
pes = 3 * jarda
pol = (36 * pes) / 3

print('Jardas: {:.3f} yd'.format(jarda))
print('Pés: {:.3f} ft'.format(pes))
print('Polegadas: {:.3f} in'.format(pol))
