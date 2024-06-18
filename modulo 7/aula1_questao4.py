def formatar_numero(numero):
       numero = numero.strip()
   
    numero = ''.join(filter(str.isdigit, numero))
    
    if len(numero) == 8:
        numero_completo = '9' + numero[:5] + '-' + numero[5:]
    elif len(numero) == 9:
        if numero[0] == '9':
            numero_completo = numero[:5] + '-' + numero[5:]
        else:
            numero_completo = numero[:5] + '-' + numero[5:]
    else:
        print("Número inválido. Por favor, digite um número de celular válido.")
        return
    
    return numero_completo

numero = input("Digite o número de celular: ")
numero_formatado = formatar_numero(numero)
if numero_formatado:
    print(f"Número completo: {numero_formatado}")
