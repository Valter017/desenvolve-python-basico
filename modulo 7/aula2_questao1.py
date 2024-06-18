def main():
    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril',
        'Maio', 'Junho', 'Julho', 'Agosto',
        'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
    partes = data_nascimento.split('/')
    dia = partes[0]
    mes_numero = int(partes[1])  
    ano = partes[2]

    nome_mes = meses[mes_numero - 1]
    
    print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")

if __name__ == "__main__":
    main()
