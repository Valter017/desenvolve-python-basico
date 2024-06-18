def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False
   
    digitos = list(map(int, cpf))

    soma = 0
    for i in range(9):
        soma += digitos[i] * (10 - i)
    resto = soma % 11
    if resto < 2:
        primeiro_verificador = 0
    else:
        primeiro_verificador = 11 - resto
    
    if primeiro_verificador != digitos[9]:
        return False
    
    soma = 0
    for i in range(10):
        soma += digitos[i] * (11 - i)
    resto = soma % 11
    if resto < 2:
        segundo_verificador = 0
    else:
        segundo_verificador = 11 - resto
   
    if segundo_verificador != digitos[10]:
        return False
    
    return True

cpf_valido = "545.315.761-52"
cpf_invalido = "545.315.761-12"

if validar_cpf(cpf_valido):
    print(f"O CPF {cpf_valido} é válido.")
else:
    print(f"O CPF {cpf_valido} é inválido.")

if validar_cpf(cpf_invalido):
    print(f"O CPF {cpf_invalido} é válido.")
else:
    print(f"O CPF {cpf_invalido} é inválido.")
