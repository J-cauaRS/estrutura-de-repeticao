num=int(input("digite um numero inteiro não negativo"))
if num < 0:
    print("fatorial não definido para números negativos.")
else:
    f= 1
    for i in range(2,num+1):
       f*= i
    print(f"o fatorial de {num} é {f}")
