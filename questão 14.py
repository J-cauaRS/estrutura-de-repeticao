import random

segredo = random.randint(1, 20)
tentativa = 0
acertou = False

while not acertou:
    tentativa = int(input("Tente adivinhar o número (1 a 20): "))
    
    if tentativa == segredo:
        print("Parabéns! Você acertou!")
        acertou = True
    elif tentativa < segredo:
        print("O número é MAIOR que isso.")
    else:
        print("O número é MENOR que isso.")