def intercalar_listas(lista1, lista2):
    resultado = []
    tamanho1 = len(lista1)
    tamanho2 = len(lista2)
    i = 0
    j = 0
 
    while i < tamanho1 and j < tamanho2:
        resultado.append(lista1[i])
        resultado.append(lista2[j])
        i += 1
        j += 1
   
    while i < tamanho1:
        resultado.append(lista1[i])
        i += 1
    
    while j < tamanho2:
        resultado.append(lista2[j])
        j += 1
    
    return resultado

def receber_lista():
    quantidade = int(input("Digite a quantidade de elementos da lista: "))
    lista = []
    for _ in range(quantidade):
        elemento = int(input("Digite um elemento da lista: "))
        lista.append(elemento)
    return lista

print("Para a primeira lista:")
lista1 = receber_lista()

print("\nPara a segunda lista:")
lista2 = receber_lista()

lista_intercalada = intercalar_listas(lista1, lista2)

print("\nLista intercalada:", ' '.join(map(str, lista_intercalada)))
