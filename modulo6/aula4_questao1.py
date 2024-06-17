numeros_pares = [num for num in range(20, 51) if num % 2 == 0]
print("Números pares entre 20 e 50:", numeros_pares)

quadrados = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print("Quadrados dos valores de 1 a 9:", quadrados)

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Números entre 1 e 100 que são divisíveis por 7:", divisiveis_por_7)

par_ou_impar = ['par' if num % 2 == 0 else 'ímpar' for num in range(0, 30, 3)]
print("Paridade para cada valor em range(0, 30, 3):", par_ou_impar)
