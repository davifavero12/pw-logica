idade = int(input("sua idade: "))

if idade >= 18:
    print(" maior de idade")
else: 
    print("menor de idade")

    print(f"nota == 10? {"nota == 10"}")
    print(f"nota != 0? {"nota != 0"}")
    print(f"nota >= 7? {"nota >= 7"}")

nota = int(input("Informe o conceito do aluno: "))

if nota >= 9:
    print("Conceito A! Excelente")
elif nota >= 7:
    print("Conceito B! Bom")
elif nota >= 5:
    print("Conceito C! Regular")
else:
    print("Conceito D! Reprovado")

    
    print("=== quilogramas e de altura")
    peso = float(input("Informe seu peso atual: "))
    altura = float(input("Informe sua altura: "))

    imc = peso/(altura ** 2)

    if imc <= 18.5:
        print("abaixo de peso")
    elif imc <= 25:
        print("peso normal")
    elif imc <= 30:
        print("Sobrepeso")
    else:
        print("obesidade")

    
    print("Exercício 6")
    
    n1 = float(input("Informe um número: ")).replace( "," , ".")
    n2 = float(input("Informe outro número: ")).replace( "," , ".")
    op = input("Operação: ( + , - , * , / ): ")

    if op == "+":
        print(f"Resultado: {n1 + n2}")    
    elif op == "-":
        print(f"Resultado: {n1 - n2}")
    elif op == "*":
        print(f"Resultado: {n1 * n2}")
    elif op == "/":
        if n2 != 0:
            print(f"Resultado: {n1 / n2:.2f}")
        else:
            print("Erro! Não pode dividir por zero!")
    else:
        print("operaçao invalida")
        
    
    print("Exercício 7")

    import random

    print("=" * 35)
    print("pedra, papel ou tesoura")
    print("=" * 35)

    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    jogador = input("\nescolha (pedra/papel/tesoura): ").lower()

    print(f"\nvoce: {jogador}")
    print(f"computador: {computador}")

    if jogador == computador:
        print("\nempate!")
    elif jogador == "pedra" and computador == "tesoura":
        print("\nvoce ganhou!")
    elif jogador == "papel" and computador == "pedra":
        print("\nvoce ganhou!")
    elif jogador == "tesoura" and computador == "papel":
        print("\nvoce ganhou!")
    else:
        print("\nvoce perdeu!")

    idade = int(input("numero inteiro"))
    
    if idade <= 0:
        print("idade invalidade!")

    elif idade <= 12:
        print("criança")

    elif idade <= 13:
        print("adolescente")

    elif idade >= 18:
        print("adulto")

    else: 
        print(" 60 idoso")

        ("exercicio 9")
        print("=== par ou impar ===")
        nome1 = input("nome do jogador 1: ")
        nome2 = input("nome do jogador 2: ")
        escolha = input(f"{nome1}. voce escolheu (par/impar): ").lower()

        n1 = int(input(f"{nome1}, seu numero: "))
        n2 = int(input(f"{nome2}, seu numero: "))

        soma = n1 + n2
        resultado = "par" if soma % 2 == 0 else "impar"

        print(f"\n{n1} + {n2} = {soma} ({resultado})")

        if escolha == resultado:
            print(f"{nome1} ganhou! ")
        else:
            print(f"{nome2} ganhou!")


    print("exercicio 10")
    idade = int(input("digite a idade do cliente: "))
    dia = input("digite o dia da semana (seg, ter, qua, qui, sex, sab, dom)").lower()
    ingresso = 40.00
    #etapa 1
    if idade <= 12:
        ingresso = ingresso * 0.5
        print("meia entrada - criança!")

    elif idade >= 60:
        ingressso = ingresso * 0.5
        print("meia entrada - criança!")
    elif idade >= 60:
        ingresso = ingresso * 0.5
        print("meia entrada - idoso!")
    elif idade <= 21:
        ingresso = ingresso * 0.5
        print("meia entrada - estudante!")
    #etapa 2 
    if dia == "qua":
        ingresso = ingresso * 0.5
        print("promoçao de quarta!")

    print(f"valor final do ingresso: r$ {ingresso:.2f}")


    print("exercicio 11")

    a = int(input("digite o lado a: "))
    b = int(input("digite o lado b: "))
    c = int(input("digite o lado c: "))

    #etapa 1
    if a < b + c and b < a + c and c < a + b:

        print("forma um triangulo!")

        #etapa 2
        if a == b and b == c:
            print("triangulo equilatero!")
        elif a == b or a == c or b == c:
            print("triangulo isoceles!")
        else:
            print("triangulo escaleno!")
    else:
         print("nao forma um triangulo!")
        

    print("exercicio 12")
operaçao = input(
    "escolha a conversao: \n"
    "1 - celsius para fahrenheit\n"
    "2 - quilometros para milhas \n"
    "3 - reais para dolar\n"
    "4 - quilogramas para libras\n"
)
valor = float(input("digite o valor que deseja converter: "))
if operaçao == "1":
    resultado = (valor * 9 / 5) + 32
    print(f"resultado: {resultado:.1f} ºf")

elif operaçao == "2":
    resultado = valor / 1.609
    print(f"resultado: {resultado:.2f} ºf")

elif operacao == "3":
    resultado = valor / 5.93
    print(f"resultado: {resultado:.2f} ºf")

    contador = 1

    while contador <= 5:

        print("ola, mundo!")

        contador = contador + 1 