t = int(input())

msg = t // 400 

print('Serão necessárias {} página(s) para visualizar os tweets.'.format(msg))

porcent = ((msg * 400) - t)/100

print('{}% dos tweets serão perdidos.'.format(porcent))
