import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

maior_qtd_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

qtd_negativos_atual = 0
inicio_atual = 0

for i, num in enumerate(lista):
    if num < 0:
        qtd_negativos_atual += 1
        if qtd_negativos_atual == 1:
            inicio_atual = i
        if qtd_negativos_atual > maior_qtd_negativos:
            maior_qtd_negativos = qtd_negativos_atual
            inicio_intervalo = inicio_atual
            fim_intervalo = i
    else:
        qtd_negativos_atual = 0

if maior_qtd_negativos > 0:
    del lista[inicio_intervalo:fim_intervalo + 1]

print("Editada:", lista)
