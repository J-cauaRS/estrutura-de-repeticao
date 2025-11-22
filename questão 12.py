a, b=0, 1
termos=10

print("primeiros 10  termos da sequência de fibonacci ")

for _ in range(termos):
    print(a, end=" ")
    a, b=a, b + b
print( )