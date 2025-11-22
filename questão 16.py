positivo=0
negativo=0
for i in range (1,11):
    num=int(input(f"digite o {i}° numero"))
    if num>0:
        positivo+= 1
    else:
        negativo += 1
print(f"a quantidade de numeros positivos é {positivo}")
print(f"a quantidade de numeros negativos é {negativo}")