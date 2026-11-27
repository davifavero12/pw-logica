produtos = "teclado"
produtos = "mouse"
produtos = "monitor"

produtos = ["teclado", "mouse", ",monitor"]
print(produtos)

print(produtos(0))
print(produtos(1))
print(produtos(2))

produtos.append("control e sabao")
print("produtos")


produtos.remove("mouse")
print(produtos)

quantidade = len(produtos)
print(f"temos {quantidade} produtos cadastrados.")

for produtos in produtos:
    print(f"ola, {produtos}!")
for contador in range(2):
    print(produtos[contador])















## lista -> [] - permite alteraçoes
## tupla -> () nao permite alteraçoes
## dicionario -> {}

alunos = {
    "joao": 8,
    "maria": 9,
    "pedro": 5, 
}
   alunos.app