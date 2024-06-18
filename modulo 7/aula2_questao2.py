def substituir_vogais_por_asterisco(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ""
    for letra in frase:
        if letra in vogais:
            frase_modificada += "*"
        else:
            frase_modificada += letra
    return frase_modificada

frase_original = input("Digite uma frase: ")

frase_modificada = substituir_vogais_por_asterisco(frase_original)

print("Frase modificada:", frase_modificada)
