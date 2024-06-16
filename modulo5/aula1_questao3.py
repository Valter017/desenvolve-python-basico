import random

numero_secreto = random.randint(1, 10)

while True:
     palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número.")
        break  
