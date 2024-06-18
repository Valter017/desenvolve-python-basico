# Nome do arquivo baixado do link fornecido
nome_arquivo = "estomago.txt"

# Abrindo o arquivo para leitura
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# Imprimindo as primeiras 25 linhas
print(f'Primeiras 25 linhas do arquivo "{nome_arquivo}":')
for linha in linhas[:25]:
    print(linha.strip())

# Contando o número total de linhas
numero_linhas = len(linhas)
print(f'\nNúmero total de linhas do arquivo: {numero_linhas}')

# Encontrando a linha com maior número de caracteres
maior_linha = max(linhas, key=len)
print(f'\nLinha com maior número de caracteres:')
print(maior_linha.strip())

# Contando o número de menções aos nomes dos personagens "Nonato" e "Íria"
# Vamos considerar todas as variações de maiúsculas e minúsculas
nome_personagem1 = "Nonato"
nome_personagem2 = "Íria"
contador_nonato = 0
contador_iria = 0

for linha in linhas:
    contador_nonato += linha.lower().count(nome_personagem1.lower())
    contador_iria += linha.lower().count(nome_personagem2.lower())

print(f'\nNúmero de menções aos nomes dos personagens:')
print(f'{nome_personagem1}: {contador_nonato}')
print(f'{nome_personagem2}: {contador_iria}')
