# Pergunte a distância da viagem em KM, calcule o preço da passagem de ônibus, cobrando R$ 0.50 por km em viagens ate 200km
# e R$ 0.45 para viagens mais longas
dist_viagem = float(input('Digite a quantidade de km viajados: '))
if dist_viagem <= 200:
    preco = dist_viagem * 0.50
else:
    preco = dist_viagem * 0.45
print(f'Sua viagem custará R${preco:.2f}')
