def main():
    print("Digite pelo menos 4 números inteiros (digite 'fim' para encerrar):")
    numeros = []
    
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros ou 'fim' para encerrar.")
    
    if len(numeros) < 4:
        print("Você digitou menos de 4 números. Programa encerrado.")
        return
    
    print("Lista original:", numeros)
    
    print("Os 3 primeiros elementos:", numeros[:3])
    
    print("Os 2 últimos elementos:", numeros[-2:])
 
    print("Lista invertida:", numeros[::-1])
    
    print("Elementos de índice par:", numeros[::2])
    
    print("Elementos de índice ímpar:", numeros[1::2])

if __name__ == "__main__":
    main()
