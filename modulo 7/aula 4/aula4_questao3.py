import os

caminho_arquivo = r'C:\Users\Administrador\OneDrive\Área de Trabalho\modulo 7'

if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    print(f'Primeiras 25 linhas do arquivo "{caminho_arquivo}":')
    for linha in linhas[:25]:
        print(linha.strip())

    numero_linhas = len(linhas)
    print(f'\nNúmero total de linhas do arquivo: {numero_linhas}')

    maior_linha = max(linhas, key=len)
    print(f'\nLinha com maior número de caracteres:')
    print(maior_linha.strip())

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

else:
    print(f'O arquivo "{caminho_arquivo}" não foi encontrado.')
