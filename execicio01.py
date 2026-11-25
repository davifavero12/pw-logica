if numero <= 0:
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

    if senha == senha_correta
    print("bem-vindo.")
    break
else:
    tentativas += 1
    print("conta bloqueada!")

if tentativas == 3:
    print("numero maximo de tentativas atingido. acesso bloqueado!")



    quantidade = int(input("quantas notas serao informadas?"))  

    soma = 0

for i in range(quantidade):
        nota = float(input("digite a nota: "))
        soma += nota

media = soma / quantidade


print("a media da turma e:", media)



numero = int(input("digite um numero entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("numero invalido! tente novamente.")
    numero = int(input("digite um numero entre 1 e 10: "))

print("numero invalido:", numero)



