n = float(input("Digite um valor para n: "))

maior=0

while n>0:
    x = float(input("Digite um valor para x: "))
    while x>maior:
        maior=x
    else:
        n=n-1

else:
    print(maior)
