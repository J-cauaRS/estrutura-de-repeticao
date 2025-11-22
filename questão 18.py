opcao = 0

while opcao != 3:
    print("\n=== MENU ===")
    print("(1) Somar dois números")
    print("(2) Subtrair dois números")
    print("(3) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("A soma é:", n1 + n2)

    elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("A subtração é:", n1 - n2)

    elif opcao == 3:
        print("Saindo...")

    else:
        print("Opção inválida! Tente novamente.")