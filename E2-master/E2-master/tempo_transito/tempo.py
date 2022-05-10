d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

total = d1 + d2 +d3 +d4 + d5
media = total / 5

porcent = (100 * total) / 7200

ep = total // 50

print('Você perdeu {} min na semana (média de {:.1f} min por dia).'.format(total,float(media)))
print('Isso significa {:.2f}% da sua semana produtiva.'.format(float(porcent)))
print('Daria para assistir {} episódio(s) de House.'.format(ep))
