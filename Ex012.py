print('Cálculo de desconto do produto')
preco = float(input('Digite o preço do produto: '))
novoPreco = preco - (preco * 0.05)
print(f'Seu preço com desconto é: R${novoPreco:.2f}')
