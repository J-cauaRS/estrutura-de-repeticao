par=0
impar=0

for i in range(10):
    num= int(input(f"escreva o {i+1} numero"))
    if(num% 2 ==  0):
        par= num+ 1
    else: 
        impar= num+1
print(f" a soma dos pares é {par}")
print(f"a soma dos numeros impares é {impar}")