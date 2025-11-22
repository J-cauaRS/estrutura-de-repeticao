quantidade = 0
pares = 0
maior = None
menor = None

while True:
    n = int(input("Digite um número (0 para parar): "))

    if n == 0:
        break

    quantidade += 1


    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n


    if n % 2 == 0:
        pares += 1

print("\nRESULTADOS:")
print("Quantidade de números digitados:", quantidade)
print("Maior número:", maior)
print("Menor número:", menor)
print("Quantidade de números pares:", pares)