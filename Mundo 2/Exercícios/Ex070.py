# Leia o nome e preço de vários produtos, o prorama deverá perguntar se o usuário vai continuar
# no final mostre: A > qual o total gasto na compra, B > Quantos produtos custam mais de R$ 1000,
# C > Qual é o nome do produto mais barato

total_compra = 0
mais_que_1000 = 0
produto_mais_barato = ''
preco_mais_barato = 0
opcao = ' '
while opcao not in 'n':
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = int(input('Digite o preço do produto: '))
    total_compra += preco_produto
    while preco_mais_barato == 0:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    if preco_produto >= 1000:
        mais_que_1000 += 1
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    opcao = input('Deseja continuar? S/N: ')
    if opcao == 'n':
        break
print(f'''O total da compra foi R${total_compra:.2f}
Temos {mais_que_1000} produtos que custam mais de R$1000.00
O produto mais barato foi {produto_mais_barato} custando R${preco_mais_barato:.2f}''')
