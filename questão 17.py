soma = 0
quantidade = 0

while True:
    idade = int(input("Digite uma idade (0 para parar): "))

    if idade == 0:
        break

    soma += idade
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média das idades é {media:.2f}")
else:
    print("Nenhuma idade foi digitada.")
    