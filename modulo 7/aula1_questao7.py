import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    
    nomes_criptografados = []
    
    for nome in nomes:
        nome_criptografado = ''
        for char in nome:
            novo_char = chr(ord(char) + chave_aleatoria)
            if ord(novo_char) > 126:
                novo_char = chr(33 + (ord(novo_char) - 127))
            nome_criptografado += novo_char
        
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)

print("Nomes criptografados:", nomes_criptografados)
print("Chave de criptografia:", chave)
