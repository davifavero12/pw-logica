opcao = 0
while opcao != 4:
    print("\n===== menu de operaçoes =====")
    print("1 - mostrar mensagem de boas-vindas!")
    print("2 - mostrar a tabuada de um numero")
    print("3 - informar se um numero e par ou impar")
    print("4 - sair")
    opcao = int(input("escolher uma opçao: "))

    if opcao == 1:
        print("\nseja bem vindo ao programa!")
    elif opcao == 2:
        numero = int(input("digite um numero para ver a tabuada: "))

        for contador in range(1, 11) :
            print("{numero} x {contador} = {numero * contador}")
    elif opcao == 3:
        numero = int(input("digite um numero: "))
        if numero % 2 == 0:
            print(f"o nunmero {numero} e par!")
        else:
            print(f"o numero {numero} e impar!")
    elif opcao == 4:
        print("\n encerrando o programa... ate mais!")
    else:
        print("opçao invalida!")
   