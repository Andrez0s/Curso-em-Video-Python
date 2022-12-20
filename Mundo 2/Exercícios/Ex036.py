# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Lendo informações do usuário e declarando variáveis
valor_casa = float(input('Digite o valor da casa a ser comprada: '))
salario = float(input('Digite o valor do seu salário: '))
anos_a_pagar = float(input('Digite em quantos anos deseja pagar: '))
prestacao_mensal = valor_casa / (anos_a_pagar * 12)

# Condição para decidir se aprova ou não o empréstimo
if prestacao_mensal > salario * 0.30:
    print(f'Empréstimo negado pois o valor da prestação excede 30% do seu salário\nR${prestacao_mensal:.2f}')
else:
    print(f'''Empréstimo aprovado! Segue abaixo os dados do emprétimo:
Valor da Casa R${valor_casa:.2f}
Prazo para pagar {anos_a_pagar:.0f} anos
O valor das prestações será de R${prestacao_mensal:.2f}
''')

