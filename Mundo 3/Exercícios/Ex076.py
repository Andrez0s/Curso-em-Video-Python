# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
# No final mostre uma listagem de preços, organizando os dados em forma tabular

tabela_precos = ('Lápis', 1.50, 'Pão', 2.50, 'Cartão', 10.00, 'Frango', 25)
variavel = 'Listagem de Preços'
print(f'{variavel:=^40}')
for item in range(0, len(tabela_precos)):
    if item % 2 == 0:
        print(f'{tabela_precos[item]:.<30}', end='')
    else:
        print(f'R${tabela_precos[item]:>7.2f}')
