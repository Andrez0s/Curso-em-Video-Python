# Calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque > 10% de desconto, a vista no cartão > 5% de desconto, em até 2x no cartão > preço normal
# 3x ou mais no cartão 20% de juros

preco_produto = float(input('Digite o valor do produto: '))
forma_de_pagamento = int(input('''
Digite 1 para - À vista Dinheiro ou Cheque
Digite 2 para - À vista no cartão
Digite 3 para para em 2x no cartão
Digite 4 para pagar em 3x ou mais no cartão
Digite a forma de pagamento desejada: '''))

if forma_de_pagamento <= 4:
    if forma_de_pagamento == 1:
        preco_produto -= (preco_produto * 0.10)
    elif forma_de_pagamento == 2:
        preco_produto -= (preco_produto * 0.05)
    elif forma_de_pagamento == 3:
        valor_parcelas = preco_produto / 2
        print(f'Você pagará 2 parcelas de {valor_parcelas:.2f}')
    elif forma_de_pagamento == 4:
        parcelas = int(input('Quantas parcelas? '))
        preco_produto += (preco_produto * 0.20)
        valor_parcelas = preco_produto / parcelas
        print(f'Você pagará {parcelas} parcelas de {valor_parcelas:.2f}')
else:
    print('Opção de forma de pagamento inválida')

print(f'O preço total a ser pago será R${preco_produto:.2f}')
