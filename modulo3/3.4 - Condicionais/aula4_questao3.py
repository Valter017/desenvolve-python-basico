ano = int(input("Insira um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
anos_teste = [1900, 2000, 2016, 2017]
for ano_teste in anos_teste:
    if (ano_teste % 4 == 0 and ano_teste % 100 != 0) or (ano_teste % 400 == 0):
        print(f"{ano_teste}: Bissexto")
    else:
        print(f"{ano_teste}: Não Bissexto")
