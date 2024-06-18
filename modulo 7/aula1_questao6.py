def encontrar_anagramas(frase, objetivo):
    objetivo_normalizado = ''.join(sorted(objetivo.lower()))
    
    anagramas = []
 
    palavras = frase.split()
    
    for palavra in palavras:
        palavra_normalizada = ''.join(sorted(palavra.lower()))
        
        if palavra_normalizada == objetivo_normalizado:
            anagramas.append(palavra)
    
    return anagramas

def main():
     frase = input("Digite uma frase: ")
    objetivo = input("Digite a palavra objetivo: ")
    
    anagramas = encontrar_anagramas(frase, objetivo)
   
    print("Anagramas:", anagramas)

if __name__ == "__main__":
    main()
