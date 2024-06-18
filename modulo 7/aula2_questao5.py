import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    
    for palavra in palavras:
        if len(palavra) >= 3:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])
            random.shuffle(letras_internas)
            palavra_embaralhada = primeira_letra + ''.join(letras_internas) + ultima_letra
            nova_frase.append(palavra_embaralhada)
        else:
            nova_frase.append(palavra)
    
    return ' '.join(nova_frase)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
