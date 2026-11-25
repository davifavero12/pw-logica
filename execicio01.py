if numero  <= 0:
    print("erro, tem que ser positivo!")

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

senha_correta = "123456"
tentativas = 0
while tentativas < 0:
    senha = input("digite uma senha: ")

    if senha == senha_correta:
    print("bem-vindo.")
    break
else:
    tentativas += 1
    print("conta bloqueada!")

if tentativas == 3:
    print("numero maximo de tentativas atingido. acesso bloqueado!")



quantidade = 0
total = 0
preco = float(input("digite o preço do produto: \n"
                   "(digite 0 para encerrar) \n",
                   "r$ "))

while preco != 0:
    total += preco
    quantidade += 1
    preto = float(input("digite o proximo produto: \n",
                        "(digite 0 para encerrar) \n",
                        "r$ "))
print(f"total da compra: r$ {total:.2f}")
print(f"quantidade de produto: {quantidade}")
                       



numero = int(input("digite um numero entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("numero invalido! tente novamente.")
    numero = int(input("digite um numero entre 1 e 10: "))

print("numero invalido:", "numero aceito!")


import random

numero_secreto = random.randint(1, 20)
tentativas = 0
palpite = int(input(
    "tente adivinhar um numero entre 1 e 20:"))

while palpite != numero_secreto:
    tentativas += 1
    if palpite < numero_secreto:
        print("numero_secreto e maior!")
    else:
        print("o numero secreto e manor!")
    palpite = int(input("tente novamente: "))
tentativas += 1
print("parabens! voce acertou!")
print(f"o numero secreto era: {numero_secreto}")
print(f"voce utilizou {tentativas} tentatives.")

preco = float(input("digite o preço do produto(ou 0 para encerrar): "))

while preco != 0:
    print("preço registrado:", preco)

    preco = float(input("digite o preço do proximo produto (ou 0 para encerrar)"
    ""))

    print("registro de protrudos encerrado!")