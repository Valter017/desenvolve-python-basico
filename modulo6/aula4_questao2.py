frase = input("Digite uma frase: ")

vogais = "aeiou"

vogais_na_frase = [letra.lower() for letra in frase if letra.lower() in vogais]
consoantes_na_frase = [letra for letra in frase if letra.isalpha() and letra.lower() not in vogais]

vogais_ordenadas = sorted(vogais_na_frase)

print(f"Vogais: {vogais_ordenadas}")
print(f"Consoantes: {consoantes_na_frase}")
