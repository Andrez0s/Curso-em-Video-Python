print('Aluguel de Carros')
print('')
dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km foram rodados? '))
preco = (dias_alugados * 60) + (km_rodados * 0.15)
print(f'O total a pagar será R${preco:.2f}')

