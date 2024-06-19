import csv

usuarios = {}#Dados de usuários

produtos = []#dados de produtos

# Funções de Usuários

def carregar_usuarios():
    # Leiturade dados de usuários já existentes.
    try:
        with open("usuarios.csv", "r") as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) == 3:
                    id, nome, nivel = linha
                    usuarios[int(id)] = {"nome": nome, "nivel": nivel}
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Criando novo arquivo.")
        open("usuarios.csv", "w").close()

def salvar_usuarios():# Adição de novos usuários
    with open("usuarios.csv", "w") as file:
        writer = csv.writer(file)
        for id, dados in usuarios.items():
            writer.writerow([id, dados['nome'], dados['nivel']])

def adicionar_usuario():
    # Dados de novos usuários
    id = int(input("Digite o ID do usuário: "))
    nome = input("Digite o nome do usuário: ")
    nivel = input("Digite o nível do usuário: ")
    usuarios[id] = {"nome": nome, "nivel": nivel}
    salvar_usuarios()
    print("Usuário adicionado com sucesso!")

def ler_usuario():
    # Leitura e visualização de informações de um usuário específico pelo ID.
    id = int(input("Digite o ID do usuário: "))
    usuario = usuarios.get(id)
    if usuario:
        print(usuario)
    else:
        print("Usuário não encontrado")

def atualizar_usuario():
    # Atualização de informações de um usuário específico pelo ID.
    id = int(input("Digite o ID do usuário: "))
    if id in usuarios:
        nome = input("Digite o novo nome do usuário (ou pressione Enter para manter o atual): ")
        nivel = input("Digite o novo nível do usuário (ou pressione Enter para manter o atual): ")
        if nome:
            usuarios[id]["nome"] = nome
        if nivel:
            usuarios[id]["nivel"] = nivel
        salvar_usuarios()
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def deletar_usuario():
    # exclusão de usuário específico pelo ID.
    id = int(input("Digite o ID do usuário: "))
    if id in usuarios:
        del usuarios[id]
        salvar_usuarios()
        print("Usuário deletado com sucesso!")
    else:
        print("Usuário não encontrado.")


def carregar_produtos():# Dados de produtos armazenados
    try:
        with open("produtos.csv", "r") as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) == 4:
                    codigo, nome, preco, quantidade = linha
                    produtos.append({"codigo": int(codigo), "nome": nome, "preco": float(preco), "quantidade": int(quantidade)})
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Criando novo arquivo.")
        open("produtos.csv", "w").close()

def salvar_produtos(): #Salva produtos da lista
       with open("produtos.csv", "w") as file:
        writer = csv.writer(file)
        for produto in produtos:
            writer.writerow([produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']])

def adicionar_produto():
    # Adição de novos produtos.
    codigo = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos()
    print("Produto adicionado com sucesso!")

def ler_produto():
   # Informações de protuto específico
    codigo = int(input("Digite o código do produto: "))
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(produto)
            return
    print("Produto não encontrado.")

def atualizar_produto():
    # Edição de informações de produtos armazenados.
    codigo = int(input("Digite o código do produto: "))
    for produto in produtos:
        if produto["codigo"] == codigo:
            nome = input("Digite o novo nome do produto (ou pressione Enter para manter o atual): ")
            preco = input("Digite o novo preço do produto (ou pressione Enter para manter o atual): ")
            quantidade = input("Digite a nova quantidade do produto (ou pressione Enter para manter o atual): ")
            if nome:
                produto["nome"] = nome
            if preco:
                produto["preco"] = float(preco)
            if quantidade:
                produto["quantidade"] = int(quantidade)
            salvar_produtos()
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto():
    # Exclusão de produto.
    codigo = int(input("Digite o código do produto: "))
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            salvar_produtos()
            print("Produto deletado com sucesso!")
            return
    print("Produto não encontrado.")

def buscar_produto_por_nome():
    # Pesquisa de produto por nome.
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(produto)
            return
    print("Produto não encontrado.")

def imprimir_produtos_por_nome():
    # Lista de produtos em ordem alfabética
    produtos_ordenados = sorted(produtos, key=lambda x: x["nome"])
    for produto in produtos_ordenados:
        print(produto)

def imprimir_produtos_por_preco():
    # Lista de produtos em ordem de preço
    produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
    for produto in produtos_ordenados:
        print(produto)


def main():# Menu de Opções ao usuário
    carregar_usuarios()
    carregar_produtos()

    while True:
        print("\nMenu:")
        print("1. Adicionar Usuário")
        print("2. Ler Usuário")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Adicionar Produto")
        print("6. Ler Produto")
        print("7. Atualizar Produto")
        print("8. Deletar Produto")
        print("9. Buscar Produto por Nome")
        print("10. Imprimir Produtos Ordenados por Nome")
        print("11. Imprimir Produtos Ordenados por Preço")
        print("12. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            ler_usuario()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            adicionar_produto()
        elif opcao == "6":
            ler_produto()
        elif opcao == "7":
            atualizar_produto()
        elif opcao == "8":
            deletar_produto()
        elif opcao == "9":
            buscar_produto_por_nome()
        elif opcao == "10":
            imprimir_produtos_por_nome()
        elif opcao == "11":
            imprimir_produtos_por_preco()
        elif opcao == "12":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
