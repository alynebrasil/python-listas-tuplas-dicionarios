carrinho_de_compras = {'arroz 5kg':19.99, 'feijão':9.99, 'carne 1kg':29.98, 'alface':1.99, 'tomate 1kg':5.99, 'batata 1/2kg':4.99}

soma = 0

for item in carrinho_de_compras.values():
    soma += item 

print(f'O total da sua compra é: {soma:.2f}')