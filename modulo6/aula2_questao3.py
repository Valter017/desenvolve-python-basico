import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(set(lista1).intersection(lista2))

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")
print(f"Interseccao - {interseccao}")
print("Contagem")
for num in interseccao:
    count_lista1 = contagem_lista1[num]
    count_lista2 = contagem_lista2[num]
    print(f"{num}: (lista1={count_lista1}, lista2={count_lista2})")
