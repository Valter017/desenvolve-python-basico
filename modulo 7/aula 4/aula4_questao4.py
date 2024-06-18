# Dados dos livros
livros = [
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1178},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417},
    {"Título": "Orgulho e Preconceito", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 279},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "O Hobbit", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1937, "Número de páginas": 310},
    {"Título": "Dom Quixote", "Autor": "Miguel de Cervantes", "Ano de publicação": 1605, "Número de páginas": 863},
    {"Título": "A Divina Comédia", "Autor": "Dante Alighieri", "Ano de publicação": 1320, "Número de páginas": 712},
    {"Título": "Moby Dick", "Autor": "Herman Melville", "Ano de publicação": 1851, "Número de páginas": 585},
    {"Título": "Guerra e Paz", "Autor": "Liev Tolstói", "Ano de publicação": 1869, "Número de páginas": 1225}
]

with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
 
    for livro in livros:
        linha = f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso!")

