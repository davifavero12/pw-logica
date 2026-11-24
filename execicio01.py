numero = int(input("digite um numero inteiro positivo: "))

soma = 0
conta = ""

for i in range("1, numero + 1"):
    soma += i
    if i == numero:
        conta += str(i)
    else:
        conta += str(i) + "+"
    print(f"{conta} = {soma}")

    senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("digite a senha: ")

    if senha != senha_correta:
        print("senha incorreta")

print("acesso permitido!")
