print('== Estágio 1 ==')
p1 = float(input('Peso? '))
n1 = float(input('Nota? ')) 
print('== Estágio 2 ==')
p2 = float(input('Peso? '))
n2 = float(input('Nota? '))
print('== Estágio 3 ==')
p3 = float(input('Peso? '))
n3 = float(input('Nota? '))
print('== Resultados ==')
mp = n1 * p1 + n2 * p2 +n3 * p3
nota_final_min = (mp * 0.6 - 5)/-0.4
nota_final_sete = (mp * 0.6 - 7) /-0.4

print('Média parcial: {:.1f}'.format(mp))
print('Nota na final, pra média 5.0 = {:.1f}'.format(nota_final_min))
print('Nota na final, pra média 7.0 = {:.1f}'.format(nota_final_sete))
