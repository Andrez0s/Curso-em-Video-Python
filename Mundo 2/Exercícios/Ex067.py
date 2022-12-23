# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# o programa será interrompido quando número solicitado for negativo

while True:
    numero = int(input('Digite o numero desejado para a tabuada 0 para sair: '))
    n = 1
    if numero > 0:
        while n < 11:
            print(f'{numero} x {n} = {numero * n}')
            n += 1
    else:
        print('Tabuada encerrada')
        break
