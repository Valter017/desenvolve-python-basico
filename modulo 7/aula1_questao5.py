def contar_vogais_e_indices(frase):
    vogais = "aeiouAEIOU"
    vogais_encontradas = []
    indices_vogais = []
    
    for i, char in enumerate(frase):
        if char in vogais:
            vogais_encontradas.append(char)
            indices_vogais.append(i)

    print(f"{len(vogais_encontradas)} vogais")
    print(f"Índices {indices_vogais}")

frase = input("Digite uma frase: ")

contar_vogais_e_indices(frase)
