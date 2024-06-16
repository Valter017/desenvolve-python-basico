# Função para calcular o percentual
def calcular_percentual(valor, total):
    return (valor / total) * 100

# Total de experimentos
N = int(input())

# Inicialização dos contadores
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Processamento dos dados
for _ in range(N):
    entrada = input().split()
    quantidade = int(entrada[0])
    tipo = entrada[1]
    
    total_cobaias += quantidade
    
    if tipo == 'S':
        total_sapos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'C':
        total_coelhos += quantidade

# Cálculo dos percentuais
percentual_sapos = calcular_percentual(total_sapos, total_cobaias)
percentual_ratos = calcular_percentual(total_ratos, total_cobaias)
percentual_coelhos = calcular_percentual(total_coelhos, total_cobaias)

# Impressão dos resultados
print("Total: {} cobaias".format(total_cobaias))
print("Total de sapos: {}".format(total_sapos))
print("Total de ratos: {}".format(total_ratos))
print("Total de coelhos: {}".format(total_coelhos))
print("Percentual de sapos: {:.2f} %".format(percentual_sapos))
print("Percentual de ratos: {:.2f} %".format(percentual_ratos))
print("Percentual de coelhos: {:.2f} %".format(percentual_coelhos))
