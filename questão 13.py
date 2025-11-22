num = int(input("Digite um número inteiro: "))

if num <= 1:
    print("Esse número NÃO é primo.")
else:
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("Esse número é PRIMO.")
    else:
        print("Esse número NÃO é primo.")
