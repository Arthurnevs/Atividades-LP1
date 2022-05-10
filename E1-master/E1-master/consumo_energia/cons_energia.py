potencia = int(input())
tempo = int(input())

qw = potencia / 1000
hr = tempo / 60

kwh = hr * qw

print('{:.1f} kWh'.format(kwh))
