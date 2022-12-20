print('Cálculo de quantidade de tinta necessária')
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
qtdTinta = area / 2
print(f'A área da sua parede é {area}M²')
print(f'Você precisará de {qtdTinta} Litros de tinta')
