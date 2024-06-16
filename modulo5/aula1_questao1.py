def main():
    num1 = float(input("Insira o primeiro número decimal: "))
    num2 = float(input("Insira o segundo número decimal: "))
    
    diff = abs(num1 - num2)
  
    diff_rounded = round(diff, 2)
    
    print(f"A diferença absoluta entre os números é: {diff_rounded}")
l
if __name__ == "__main__":
    main()
