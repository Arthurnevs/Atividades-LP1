'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Segundo 
'''



a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('Considerando os números {}, {}, {} e {}'.format(a,b,c,d))
if a <= b and a <= c and a <= d:
    if b <= c and b <= d:
        segmenor = b
    elif c <= b and c <= d:
        segmenor = c
    else:
        segmenor = d
elif b <= a and b <=  c and b <= d:
    if a <= c and a <= d:
        segmenor = a
    elif c <= d and c <= a:
        segmenor = c
    else:
        segmenor = d
elif c <= a and c <= b and c <= d:
    if a <= b  and a <= d:
        segmenor = a
    elif b <= a and b <= d:
        segmenor = b
    else:
        segmenor = d
else:
    if a <= b and a <= c:
        segmenor = a
    elif b <= a and b <= c:
        segmenor = b
    else:
        segmenor = c

if a >= b and a >= c and a >= d:
    if b >= c and b >= d:
        segundomaior = b
    elif c >= b and c >= d:
        segundomaior = c
    else:
        segundomaior = d
elif b >=a and b >= c and b >= d:
    if a >= c and a >= d:
        segundomaior = a
    elif c >= d and c >= a:
        segundomaior = c
    else:
        segundomaior = d
elif c >= a and c >= b and c >= d:
    if a >= b  and a >= d:
        segundomaior = a
    elif b >= a and b >= d:
        segundomaior = b
    else:
        segundomaior = d
else:
    if a >= b and a >= c:
        segundomaior = a
    elif b >= a and b >= c:
        segundomaior = b
    else:
        segundomaior = c

print('O segundo menor número é {}'.format(segmenor))
print('O segundo maior número é {}'.format(segundomaior))
