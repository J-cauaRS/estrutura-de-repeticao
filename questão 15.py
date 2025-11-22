soma = 0

while True:
    n = int(input("Digite um número (negativo para parar): "))

    if n < 0: 
        break

    soma += n  

print("A soma dos números positivos é:", soma)