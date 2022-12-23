# Computador pensa em um número entre 0 e 10, O jogador precisa tentar adivinhar até acertar, mostrando no final quantas
# tentativas foram necessárias para vencer

from random import randint

num_random = randint(0, 10)
tentativas = 0
palpite = 0
while palpite != num_random:
    tentativas += 1
    palpite = int(input('Digite um número de 0 a 10: '))
    if palpite > num_random:
        print('Menos... Tente novamente')
    elif palpite < num_random:
        print('Mais... Tente novamente')
print(f'Você acertou! o número escolhido pelo computador foi {num_random} e você digitou {palpite}')
print(f'Foram necessárias {tentativas} tentativas')
