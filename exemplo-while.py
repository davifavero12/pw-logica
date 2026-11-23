contador = 1

while contador <= 5:

    print("ola, mundo!")

    contador = contador + 1 

    while True:

        idade = int(input("digite sua idade "))

        if idade <= 0:
            break
        print("idade invalida! tente novamente.")

print("idade registrada!")