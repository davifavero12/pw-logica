print("=== calculadora de desconto ===")
produto = input("nome do produto: ")
preco = float(input("preço: r$"))
desconto = float(input("desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"\nproduto: {produto}")
print(f"preço original: r$ {preco:.2f}")
print(f"desconto: r$ {valor_desconto:.2f}")
print(f"preço final: r$ {preco_final:.2f}")