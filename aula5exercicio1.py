
filme1 = "era do gelo"
filme2 = "extraordinario"
filme3 = "batman"
filme4 = "marvel"
filme5 = "liga da justiça"

filmes = ["era do gelo", "extraordinario", "batman", "marvel", "liga da justiça"]
print(filmes)

print(filmes[0])
print(filmes[1])
print(filmes[2])
print(filmes[3])
print(filmes[4])

filmes.append("extraordinario")
print(filmes)

filmes.remove("batman")
print(filmes)

quantidade = len(filmes)
print(f"temos {quantidade} filmes cadastrados.")

for filme in filmes:
    print(f"ola, {filmes}!")
for contador in range(2):
    print(filmes[contador])
        