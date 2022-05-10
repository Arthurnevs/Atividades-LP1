'''
UFCG
PROGRAMAÇÃO 1
JOSE ARTHUR NEVES DE BRITO - 119210204 
Caixa Alta'''

def caixa_alta(frase):
    nova_frase = ''
    palavra = ''

    for indice in range(len(frase)):
        if frase[indice] != ' ':
            if indice != 0:
                if frase[indice - 1 ] == ' ':
                    palavra += frase[indice].upper()
                else:
                    palavra += frase[indice]
            else:
                palavra += frase[indice].upper()

        else:
            if len(palavra) == 1:
                nova_frase += palavra.lower()
                palavra = ''

            elif len(palavra) > 1:
                nova_frase += palavra
                palavra = ''

            nova_frase += frase[indice]
    
    if palavra != '':
        if len(palavra) == 1:
            palavra = palavra.lower()
        nova_frase += palavra

    return nova_frase
