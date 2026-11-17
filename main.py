idade = int(input("sua idade: "))

if idade >= 18:
    print(" maior de idade")
else: 
    print("menor de idade")

    print(f"nota == 10? {nota == 10}")
    print(f"nota != 0? {nota != 0}")
    print(f"nota >= 7? {nota >= 7}")

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
    peso = input("tenho 52 de peso")
    altura = input("sua altura 1,58")

    imc = peso / (altura ** 2)



