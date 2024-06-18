frase = input("Digite a frase: ")

contagem_espacos = 0

for caractere in frase:
 
    if caractere == ' ':
        contagem_espacos += 1

print(f"Espaços em branco: {contagem_espacos}")
