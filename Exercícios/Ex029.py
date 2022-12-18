# Leia a velocidade de um carro, se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa custa R$7.00 por cada km acima do limite
vel = float(input('Digite a velocidade do carro: '))
if vel <= 80:
    print('Você está dentro do limite.')
else:
    multa = (vel - 80) * 7
    print(f'Você foi multado em R${multa:.2f}')
