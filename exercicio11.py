numero = int(input("digite um numero inteiro positivo: "))
pares = 0
impares = 0

for contador in range(1, numero + 1)

    if contador % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"quantidade de numeros pares {pares}")
print(f"quantidade de numeros impares {impares}")